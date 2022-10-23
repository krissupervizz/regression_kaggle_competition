# take test.csv -> make_dataset -> build_features 
# predict using saved model from train_model.py

from cgi import test
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
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from catboost import CatBoostClassifier, Pool
from sklearn.tree import DecisionTreeClassifier
from src.data.preprocess1 import *
from src.features.feature1 import *


@click.command()
@click.argument('input_data_filepath', type=click.Path(exists=True))
@click.argument('input_catboost_model', type=click.Path())
@click.argument('input_sklearn_model', type=click.Path())
@click.argument('output_predictions_filepath', type=click.Path())

def main(input_data_filepath, input_catboost_model, input_sklearn_model, output_predictions_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # preprocess
    test_data = pd.read_csv(input_data_filepath)
    test_data = preprocess_data(test_data)
    # feature engineering

    sklearn_model = pickle.load(open(input_sklearn_model, 'rb'))
    catboost_model = pickle.load(open(input_catboost_model, 'rb'))

    catboost_prediction = catboost_model.predict(test_data)
    sklearn_prediction = sklearn_model.predict(test_data)

    predictions = {

        'catboost_prediction': catboost_prediction,
        'sklearn_prediction': sklearn_prediction,

    }

    pickle.dump(predictions, open(output_predictions_filepath, 'wb'))




if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()