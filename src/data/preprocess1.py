from cmath import nan
import src.config1 as cfg
import pandas as pd
import numpy as np

def drop_id(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(cfg.ID_COL, axis=1)
    return df

def extract_target(df: pd.DataFrame):
    df, target = df.drop(cfg.TARGET_COL, axis=1), df[cfg.TARGET_COL]
    return df, target 

def preprocess_real_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.REAL_COL[0]] = df[cfg.REAL_COL[0]].fillna(value=0.0)
    selected_rows = df[df[cfg.REAL_COL[1]].isnull()].index.to_list()
    df = df.drop(selected_rows, axis=0)
    df = df.drop(cfg.REAL_COL[2], axis=1)
    cfg.REAL_COL.remove(cfg.REAL_COL[2])
    df[cfg.REAL_COL] = df[cfg.REAL_COL].astype(np.float32)

    return df
def preprocess_int_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.INT_COL] = df[cfg.INT_COL].astype(np.int32)
    return df

def clear_col_list(lst: list, clear_lst:list) -> list:
    for i in clear_lst:
        lst.remove(i)
    return lst

def preprocess_obj_col(df: pd.DataFrame) -> pd.DataFrame:
    drop_column = df[cfg.OBJ_COL].loc[:, (df[cfg.OBJ_COL].isna().sum() > 200).values].columns.to_list()
    df = df.drop(drop_column, axis=1)

    return df

def preprocess_ohe_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.OHE_COL[0]] = df[cfg.OHE_COL[0]].replace(['Pave', 'Grvl'], [1, 0]).astype(np.int8)
    df[cfg.OHE_COL[1]] = df[cfg.OHE_COL[1]].replace(['Y', 'N'], [1, 0]).astype(np.int8)
    return df

def preprocess_order_nan_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.ORDER_COL_NAN] = df[cfg.ORDER_COL_NAN].replace(['Ex', 'Gd', 'TA', 'Fa', 'Po', nan], [5, 4, 3, 2, 1, 0]).astype(np.int8)
    return df
def preprocess_order_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.ORDER_COL] = df[cfg.ORDER_COL].replace(['Ex', 'Gd', 'TA', 'Fa', 'Po'], [5, 4, 3, 2, 1]).astype(np.int8)
    return df
def preprocess_order_an_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.ORDER_COL_AN] = df[cfg.ORDER_COL_AN].replace(['Gd', 'Av', 'Mn', 'No', nan], [4, 3, 2, 1, 0]).astype(np.int8)
    return df
def preprocess_order_bsmt_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.ORDER_COL_BSMT] = df[cfg.ORDER_COL_BSMT].replace(['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', nan], [6, 5, 4, 3, 2, 1, 0]).astype(np.int8)
    return df
def preprocess_order_garage_col(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.ORDER_COL_CARAGE] = df[cfg.ORDER_COL_CARAGE].replace(['Fin', 'RFn', 'Unf', nan], [3, 2, 1, 0]).astype(np.int8)
    return df

def preprocess_cat_col(df: pd.DataFrame) -> pd.DataFrame:
    selected_rows = df[df['GarageType'].isnull()].index.to_list()
    df = df.drop(selected_rows, axis=0)
    selected_rows = df[df['Electrical'].isnull()].index.to_list()
    df = df.drop(selected_rows, axis=0)
    df[cfg.CAT_COL] = df[cfg.CAT_COL].astype('category')
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = drop_id(df)
    df = preprocess_real_col(df)
    df = preprocess_int_col(df)
    df = preprocess_obj_col(df)
    df = preprocess_ohe_col(df)
    df = preprocess_order_nan_col(df)
    df = preprocess_order_col(df)
    df = preprocess_order_an_col(df)
    df = preprocess_order_bsmt_col(df)
    df = preprocess_order_garage_col(df)
    df = preprocess_cat_col(df)
    return df


