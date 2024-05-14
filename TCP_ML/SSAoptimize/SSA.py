import numpy as np
import matplotlib.pyplot as plt
import shap
from sklearn.ensemble import RandomForestRegressor
dffill=pd.read_excel("TCP_ML\datasets\TCP_dataset.xlsx")
cols = ['substrate', 'ETL', 'HTL', 'electrode', 'depositionProcedure',
        'depositionMethod', 'Anti-solvent', 'PrecursorSolvent']

for col in cols:
    zipcodes = dffill[col].value_counts().keys().tolist()
    counts = dffill[col].value_counts().tolist()
    for (zipcode, count) in zip(zipcodes, counts):
        if count < 2:
            idxs = dffill[dffill[col] == zipcode].index
            dffill.drop(idxs, inplace=True)

# 重置索引
dffill.reset_index(drop=True, inplace=True)
dffil=dffill.drop(['Jsc','Voc','FF'],axis=1)
def split_dataset(dataset, test_ratio=0.2):
  test_indices = np.random.rand(len(dataset)) < test_ratio
  return dataset[~test_indices], dataset[test_indices]
train_ds_pd, valid_ds_pd = split_dataset(dffill)
label = 'PCE'
train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(train_ds_pd, label=label, task=tfdf.keras.Task.REGRESSION)
valid_ds = tfdf.keras.pd_dataframe_to_tf_dataset(valid_ds_pd, label=label, task=tfdf.keras.Task.REGRESSION)
tuner = tfdf.tuner.RandomSearch(num_trials=20)
rf1 = tfdf.keras.RandomForestModel(task = tfdf.keras.Task.REGRESSION,tuner=tuner)
rf1.compile(metrics=["mae"]) 
rf1.fit(x=train_ds)
valid_ds_pd['predictions'] = rf1.predict(valid_ds)
rmse = np.sqrt(mean_squared_error(valid_ds_pd[label], valid_ds_pd['predictions']))
mae = mean_absolute_error(valid_ds_pd[label], valid_ds_pd['predictions'])
r2 = r2_score(valid_ds_pd[label], valid_ds_pd['predictions'])

rmse_str = "{:.4f}".format(rmse)
mae_str = "{:.4f}".format(mae)
r2_str = "{:.4f}".format(r2)



print(rmse)
print(mae)
print(r2)
all_rmse.append(rmse)
all_mae.append(mae)
all_r2.append(r2)
