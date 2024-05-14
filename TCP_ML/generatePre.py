"""
'Cs', 'FA', 'I', 'structure', 'bandgap', 'substrate', 'ETL-1', 'ETL-2',
       'HTL', 'electrode', 'depositionProcedure', 'depositionMethod',
       'Anti-solvent', 'PrecursorSolvent', 'AnnealingTemperature',
       'AnnealingTime',
有这么几列，其中Cs列数值在0-0.19之间变化，变化刻度为0.01；FA在0.81-1之间变化，变化刻度为0.01；
I在2.59-3之间变化，变化刻度为0.01；structure为0或者1；bandgap数值在1.5到1.63之间变化，变化刻度为0.01；
substrate为ITO或者FTO;ETL-1为SnO2、c-TiO2;ETL-2为mp-TiO2、unused；HTL在'PTAA','spiro', 'SAMs',  'NiOx'这几个；
electrode为Au、Ag；depositionProcedure为one-step、two-step；depositionMethod为spin；Anti-solvent为CB；
PrecursorSolvent为DMF/DMSO、DMF/DMSO/GBL、DMF:DMSO:NMP、DMF/NMP；AnnealingTemperature>17，小于125，变化刻度为1；
AnnealingTime为30，60；另外要求Cs和FA的和不超过1；请按照这几个条件，将这几个组合起来，输出到一个excel里面
"""

import pandas as pd
from itertools import product

# 定义各个参数的取值范围
Cs_range = [i/1000 for i in range(44,56)]
FA_range = [0.85+i/1000 for i in range(10)]
I_range = [2.88 + i/1000 for i in range(10)]
structure_range = [0, 1]
bandgap_range = [1.57+i/100 for i in range(10)]
substrate_range = ["ITO", "FTO"]
ETL_1_range = ["BCP", "c-TiO2","PCBM"]
ETL_2_range = ["mp-TiO2","C", "BCP"]
HTL_range = ["PTAA", "spiro", "SAMs", "NiOx"]
electrode_range = ["Au", "Ag"]
depositionProcedure_range = ["one-step"]
depositionMethod_range = ["spin"]
Anti_solvent_range = ["CB"]
PrecursorSolvent_range = ["DMF/DMSO", "DMF/NMP"]
AnnealingTemperature_range = [100]
AnnealingTime_range = [15,30, 60]

# 生成所有可能的组合
combinations = list(product(
    Cs_range, FA_range, I_range, structure_range, bandgap_range, substrate_range, 
    ETL_1_range, ETL_2_range, HTL_range, electrode_range, depositionProcedure_range,
    depositionMethod_range, Anti_solvent_range, PrecursorSolvent_range,
    AnnealingTemperature_range, AnnealingTime_range
))

# 筛选符合条件的组合
valid_combinations = [comb for comb in combinations if comb[0] + comb[1] <= 1]

# 创建 Pandas DataFrame 并保存到 Excel
df = pd.DataFrame(valid_combinations, columns=[
    'Cs', 'FA', 'I', 'structure', 'bandgap', 'substrate', 'ETL-1', 'ETL-2',
    'HTL', 'electrode', 'depositionProcedure', 'depositionMethod',
    'Anti-solvent', 'PrecursorSolvent', 'AnnealingTemperature', 'AnnealingTime'
])
df.to_excel("perovskite_combinations.xlsx", index=False)

print("符合条件的钙钛矿组合已保存到 perovskite_combinations.xlsx")





# import pandas as pd
# import itertools
# import numpy as np

# # Define ranges and steps for each parameter
# cs_values = np.arange(0.02, 0.2, 0.01)
# fa_values = np.arange(0.81, 1.01, 0.01)
# i_values = np.arange(2.59, 3.0, 0.01)
# structure_values = [0, 1]
# bandgap_values = np.arange(1.5, 1.63, 0.01)
# substrate_values = ['ITO', 'FTO']
# etl_1_values = ['SnO2', 'c-TiO2']
# etl_2_values = ['mp-TiO2',  'unused']
# htl_values = ['PTAA',  'spiro',  'SAMs','NiOx', ]
# electrode_values = ['Au', 'Ag']
# deposition_procedure_values = ['one-step', 'two-step']
# deposition_method_values = ['spin']
# anti_solvent_values = ['CB']
# precursor_solvent_values = ['DMF/DMSO', 'DMF/DMSO/GBL', 'DMF:DMSO:NMP', 'DMF/NMP']
# annealing_temperature_values = [100]
# annealing_time_values = [30,45,60]

# # Generate all possible combinations
# combinations = list(itertools.product(
#     cs_values,
#     fa_values,
#     i_values,
#     structure_values,
#     bandgap_values,
#     substrate_values,
#     etl_1_values,
#     etl_2_values,
#     htl_values,
#     electrode_values,
#     deposition_procedure_values,
#     deposition_method_values,
#     anti_solvent_values,
#     precursor_solvent_values,
#     annealing_temperature_values,
#     annealing_time_values,
# ))

# # Convert combinations into a Pandas DataFrame
# combinations_df = pd.DataFrame(combinations, columns=[
#     'Cs',
#     'FA',
#     'I',
#     'Structure',
#     'Bandgap',
#     'Substrate',
#     'ETL-1',
#     'ETL-2',
#     'HTL',
#     'Electrode',
#     'DepositionProcedure',
#     'DepositionMethod',
#     'Anti-solvent',
#     'PrecursorSolvent',
#     'AnnealingTemperature',
#     'AnnealingTime',
# ])

# # Export the DataFrame to an Excel file (It will be VERY large)
# combinations_df.to_excel('combinations.xlsx', index=False)


