# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import sys
sys.path.insert(0, 'C:\\Users\\Кристина\\regression_kaggle_competition')
from src.utils import save_as_pickle
import pandas as pd
from feature1 import noise_level


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_data_filepath', type=click.Path())
def main(input_filepath, output_data_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from interim data')

    df = pd.read_pickle(input_filepath)
    df = noise_level(df)
    save_as_pickle(df, output_data_filepath)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()