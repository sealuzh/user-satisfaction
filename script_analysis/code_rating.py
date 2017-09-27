from utils import *
from correlations import *
import metrics as m
import pandas as pd
import os

folder_name = '/code_rating'


def correlation_code_rating(code_metrics, user_metrics, versions, plot):
    user_frame = pd.read_csv(user_metrics)
    code_frame = pd.read_csv(code_metrics)

    code_frame['av. rating'] = user_frame['av. rating']

    get_categories(pd.read_csv(versions))

    # Compute without the distinction per category
    total_rho, total_p = \
        compute_overall_correlations(code_frame, ['av. rating'] + m.code_metrics, folder_name)

    header = ['All']
    for filename in os.listdir(categories):
        if filename.endswith('.csv'):

            # Get category name, filter frame and calculate correlations
            category = filename[:-4]
            category_ids = pd.read_csv(categories + '/' + filename)['id']
            print 'Elaborating ', category
            header.append(category)

            aux = code_frame[code_frame['id'].isin(category_ids)]
            rho, p_values = calculate_correlation(aux, ['av. rating'] + m.code_metrics)

            # Remove empty columns
            rho = rho.dropna(how='all').dropna(axis=1, how='all')
            p_values = p_values.dropna(how='all').dropna(axis=1, how='all')

            # Save files
            path_to_save = correlations + folder_name
            rho.to_csv(path_to_save + '/rho_' + category + '.csv')
            p_values.to_csv(path_to_save + '/p_' + category + '.csv')

            total_rho[category] = rho.loc['av. rating']
            total_p[category] = p_values.loc['av. rating']

            if plot:
                pass
            # todo: add the creation of the map

    total_rho = total_rho.ix[m.code_metrics, header]
    total_p = total_p.ix[m.code_metrics, header]

    total_rho.to_csv(path_to_save + '/rho.csv')
    total_p.to_csv(path_to_save + '/p.csv')

    if plot:
        cols = ['All', 'Books', 'Communic.', 'Educat.', 'Entert.', 'Finance', 'Games', 'Lifest.', 'Music', 'Personal.', 'Photog.', 'Product.', 'Social', 'Tools', 'Travel', 'Video']
        generate_heatmap(total_rho, total_p, cols, total_rho.index, 'code_rating')