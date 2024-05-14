from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump

# 读取数据
dataset = pd.read_excel('triplePCE\\fill.xlsx')

# 定义分类和连续特征列
categorical_cols = dataset.columns[5:13]
continuous_cols = dataset.columns[:5].append(dataset.columns[13:15])
label = dataset.columns[15]

# 对分类列进行one-hot编码
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoded_categorical = encoder.fit_transform(dataset[categorical_cols])
encoded_categorical_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_cols))

# 将编码后的分类列与连续列合并
dataset = pd.concat([dataset[continuous_cols], encoded_categorical_df, dataset[label]], axis=1)

# 创建 KFold 对象
n_folds = 5
kfold = KFold(n_splits=n_folds, shuffle=True, random_state=42)

# 循环进行交叉验证
for fold, (train_index, val_index) in enumerate(kfold.split(dataset)):
    print(f"Fold {fold+1}")

    # 划分训练集和验证集
    train_ds = dataset.iloc[train_index]
    valid_ds = dataset.iloc[val_index]

    # 创建并训练模型
    model = RandomForestRegressor(random_state=42)
    model.fit(train_ds.drop(label, axis=1), train_ds[label])

    # 验证模型
    predictions = model.predict(valid_ds.drop(label, axis=1))
    mse = mean_squared_error(valid_ds[label], predictions)
    print(f"Fold {fold+1} MSE: {mse}")

    # 保存模型和encoder
    dump(model, f"model_fold_{fold+1}.joblib")
    dump(encoder, f"encoder_fold_{fold+1}.joblib")