import click
import logging
from pathlib import Path
import sys
sys.path.insert(0, 'C:\\Users\\Кристина\\regression_kaggle_competition')
from dotenv import find_dotenv, load_dotenv
from catboost.utils import eval_metric
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor, Pool
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import *
from sklearn.preprocessing import *
from sklearn.compose import *
from sklearn.pipeline import *
from sklearn.impute import *
from sklearn.multioutput import *
from src.utils import save_as_pickle
import pandas as pd
import src.config1 as cfg
import pickle
import category_encoders as ce


@click.command()
@click.argument('input_data_filepath', type=click.Path(exists=True))
@click.argument('input_target_filepath', type=click.Path(exists=True))
@click.argument('output_model_catboost_filepath', type=click.Path())
@click.argument('output_model_sklearn_filepath', type=click.Path())
@click.argument('output_validx_filepath', type=click.Path())
def main(input_data_filepath, input_target_filepath, output_model_catboost_filepath, output_model_sklearn_filepath, output_validx_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    train_data = pd.read_pickle(input_data_filepath)
    train_target = pd.read_pickle(input_target_filepath)

    train_idx, val_idx = train_test_split(train_data.index, test_size=0.2, random_state=7)

    train_pool = Pool(
        data=train_data.loc[train_idx],
        label=train_target.loc[train_idx],
        cat_features=cfg.CAT_COL
    )
    val_pool = Pool(
        data=train_data.loc[val_idx],
        label=train_target.loc[val_idx],
        cat_features=cfg.CAT_COL
    )

    clf = CatBoostRegressor(
        subsample= 0.5,
        loss_function='RMSE',
        iterations=10000,
        silent=True,
        depth=6,
        l2_leaf_reg=2.0,
        learning_rate=0.01,
        early_stopping_rounds=100,
        random_seed=5
    )

    clf.fit(train_pool, eval_set=val_pool, plot=False)
    pickle.dump(clf, open(output_model_catboost_filepath, 'wb'))
    pickle.dump(val_idx.tolist(), open(output_validx_filepath, 'wb'))

    real_pipe = Pipeline([
        ('imputer', SimpleImputer()),
        ('scaler', StandardScaler())
    ]
    )
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='NA')),
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ])
    """train_data = ColumnTransformer(transformers=[
        ('real_cols', real_pipe, cfg.REAL_COL),
        ('cat_cols', cat_pipe, cfg.CAT_COL),
        ('ohe_cols', 'passthrough', cfg.OHE_COL)
    ]
    ).fit_transform(train_data, train_target)"""

    preprocess_pipe = ColumnTransformer(transformers=[
        ('real_cols', real_pipe, cfg.REAL_COL),
        ('cat_cols', cat_pipe, cfg.CAT_COL),
        ('ohe_cols', 'passthrough', cfg.OHE_COL)
    ]
    )
    sklearn_model = DecisionTreeRegressor(
        criterion='squared_error',
        splitter='random',
        max_depth=40,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features='auto',

    )
    
    model_pipe = Pipeline([
        ('preprocess', preprocess_pipe),
        ('model', sklearn_model)
    ]
    )
    model_pipe.fit(X=train_data.loc[train_idx], y=train_target.loc[train_idx])
    #model_pipe=sklearn_model.fit(X=train_data.loc[train_idx], y=train_target.loc[train_idx])
    pickle.dump(model_pipe, open(output_model_sklearn_filepath, 'wb'))

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()