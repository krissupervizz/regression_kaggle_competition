# load train dataset and val_idx
# filter by val_idx
# after look at https://github.com/iterative/example-get-started/blob/main/src/evaluate.py

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import sys
sys.path.insert(0, 'C:\\Users\\Кристина\\regression_kaggle_competition')
from src.utils import save_as_pickle
import pandas as pd
import src.config as cfg
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error
from catboost import CatBoostRegressor, Pool
from sklearn.tree import DecisionTreeRegressor



@click.command()
@click.argument('input_data_filepath', type=click.Path(exists=True))
@click.argument('input_target_filepath', type=click.Path(exists=True))
@click.argument('input_idx_filepath', type=click.Path())
@click.argument('input_catboost_model', type=click.Path())
@click.argument('input_sklearn_model', type=click.Path())
@click.argument('output_metrics_filepath', type=click.Path())

def main(input_data_filepath, input_target_filepath, input_idx_filepath, input_catboost_model, input_sklearn_model, output_metrics_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    train_data = pd.read_pickle(input_data_filepath)
    train_target = pd.read_pickle(input_target_filepath)
    val_index = pd.read_pickle(input_idx_filepath)
    print()

    sklearn_model = pickle.load(open(input_sklearn_model, 'rb'))
    catboost_model = pickle.load(open(input_catboost_model, 'rb'))

    catboost_prediction = catboost_model.predict(train_data.loc[val_index])
    sklearn_prediction = sklearn_model.predict(train_data.loc[val_index])

    rmse_catboost = mean_squared_error(train_target.loc[val_index], catboost_prediction, squared=False)
    rmse_sklearn = mean_squared_error(train_target.loc[val_index], sklearn_prediction, squared=False)
    mae_catboost = mean_absolute_error(train_target.loc[val_index], catboost_prediction)
    mae_sklearn = mean_absolute_error(train_target.loc[val_index], sklearn_prediction)


    metrics = {

        'rmse_catboost': rmse_catboost,
        'rmse_sklearn': rmse_sklearn,
        'mae_catboost': mae_catboost,
        "mae_sklearn": mae_sklearn

    }

    pickle.dump(metrics, open(output_metrics_filepath, 'wb'))




if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()