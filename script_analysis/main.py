import click
import os

from rating_user_metrics import *
from code_rating import *
from user_quality import *

from settings import *


@click.group()
def execute():
    pass


def create_output_directories():
    if not os.path.exists(categories):
        os.mkdir(categories)
    if not os.path.exists(correlations):
        os.mkdir(correlations)
    if not os.path.exists(images):
        os.mkdir(images)


@execute.command()
@click.option('--user', '-u', default='../csv/user_metrics.csv', help='The csv file with all the listed user metrics')
@click.option('--version', '-v', default='../csv/versions.csv', help='The csv file with all the listed versions')
@click.option('--plot', '-p', is_flag=True, help='Whether export the map as image or not')
def user_rating(user, version, plot):
    correlation_user_rating(user, version, plot)


@execute.command()
@click.option('--code', '-c', default='../csv/code_metrics.csv', help='The csv file with all the listed code metrics')
@click.option('--user', '-u', default='.//csv/user_metrics.csv', help='The csv file with all the listed user metrics')
@click.option('--version', '-v', default='../csv/versions.csv', help='The csv file with all the listed versions')
@click.option('--plot', '-p', is_flag=True, help='Whether export the map as image or not')
def code_feature(code, user, version, plot):
    correlation_user_quality(code, user, version, plot)


@execute.command()
@click.option('--code', '-c', default='..csv/code_metrics.csv', help='The csv file with all the listed code metrics')
@click.option('--user', '-u', default='../csv/user_metrics.csv', help='The csv file with all the listed user metrics')
@click.option('--version', '-v', default='../csv/versions.csv', help='The csv file with all the listed versions')
@click.option('--plot', '-p', is_flag=True, help='Whether export the map as image or not')
def code_rating(code, user, version, plot):
    correlation_code_rating(code, user, version, plot)


if __name__ == '__main__':
    create_output_directories()
    execute()
