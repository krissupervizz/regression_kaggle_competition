import pandas as pd
import numpy as np

def noise_level(df: pd.DataFrame):
    level_noise = []
    area = df['MSZoning']
    cond1 = df['Condition1']
    cond2 = df['Condition2']
    five_cond = ['I', 'RH', 'C', 'Artery', 'RRNh', 'RRAn', 'RRNe', 'RRAe']
    four_cond = ['A', 'FV', 'RM', 'Feedr']
    three_cond = ['RL', 'Norm']
    two_cond = ['RP', 'PosN', 'PosA']
    for i in area.index:
        if ((area[i] in five_cond) or (cond1[i] in five_cond) or (cond2[i] in five_cond)):
            level_noise.append(5)
        elif ((area[i] in four_cond) or (cond1[i] in four_cond) or (cond2[i] in four_cond)):
            level_noise.append(4)
        elif ((area[i] in three_cond) or (cond1[i] in three_cond) or (cond2[i] in three_cond)):
            level_noise.append(3)  
        elif ((area[i] in two_cond) or (cond1[i] in two_cond) or (cond2[i] in two_cond)):
            level_noise.append(2)     
    df['noise_level'] = level_noise
    df['noise_level'] = df['noise_level'].astype(np.int8)
    return df