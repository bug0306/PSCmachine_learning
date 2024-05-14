import joblib
import pandas as pd
cs_value = 1
fa_value = 0
i_value = 3
Device_structure_value = 1
BG_value =1.53
substrate_value = 'ITO'
ETL_value = 'SnO2'
HTL_value = 'spiro'
electrode_value = 'Ag'
depositionProcedure_value = 'one-step'
depositionMethod_value = 'spin'
Anti_solvent_value = 'CB'
PrecursorSolvent_value = 'DMF/DMSO'
AnnealingTem_value = 120
AnnealingTime_value = 20
data = {'Cs': [cs_value], 'FA': [fa_value], 'I': [i_value],'structure':[Device_structure_value],
        'bandgap':[BG_value],'substrate':[substrate_value],'ETL':[ETL_value],'HTL':[HTL_value],
        'electrode':[electrode_value],'depositionProcedure':[depositionProcedure_value],
        'depositionMethod':[depositionMethod_value],'Anti-solvent':[Anti_solvent_value],
        'PrecursorSolvent':[PrecursorSolvent_value],'AnnealingTemperature':[AnnealingTem_value],
        'AnnealingTime':[AnnealingTime_value]}

df = pd.DataFrame(data)
print(df)
df.iloc[:, [0, 1,2, 4]] = df.iloc[:, [0, 1,2, 4]].astype('float64')
df.iloc[:, [3, 13, 14]] = df.iloc[:, [3, 13, 14]].astype('int64')
df.iloc[:, [5,6,7,8,9,10,11,12]] = df.iloc[:, [5,6,7,8,9,10,11,12]].astype('object')
encoder = joblib.load('encoder_fold_5.joblib')
encoded_columns = encoder.transform(df.iloc[:, [5,6,7,8,9,10,11,12]])

encoded_df = pd.DataFrame(encoded_columns, columns=encoder.get_feature_names_out(df.columns[5:13]))


df = pd.concat([df.iloc[:, :5], df.iloc[:, 13:],encoded_df], axis=1)
model = joblib.load('model_fold_5.joblib')

prediction = model.predict(df)
print(prediction[0])