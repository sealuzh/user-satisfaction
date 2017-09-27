from utils import *
from correlations import *
import metrics as m
import pandas as pd
import os

folder_name = '/user_rating'
not_to_consider = ['Entertainment', 'Personalization', 'Tools', 'Social']


def correlation_user_rating(user_metrics, versions, plot):
    frame = pd.read_csv(user_metrics)
    get_categories(pd.read_csv(versions))

    # Compute without the distinction per category
    total_rho, total_p = \
        compute_overall_correlations(frame, ['av. rating'] + m.user_metrics, folder_name)

    header = ['All']
    for filename in os.listdir(categories):
        if filename.endswith('.csv'):
            category = filename[:-4]
            if category not in not_to_consider:
                # Get category name, filter frame and calculate correlations
                category_ids = pd.read_csv(categories + '/' + filename)['id']
                print 'Elaborating ', category
                header.append(category)

                aux = frame[frame['id'].isin(category_ids)]
                rho, p_values = calculate_correlation(aux, ['av. rating'] + m.user_metrics)

                # Remove empty columns
                rho = rho.dropna(how='all').dropna(axis=1, how='all')
                p_values = p_values.dropna(how='all').dropna(axis=1, how='all')

                # Save files
                path_to_save = correlations + '/user_rating'
                rho.to_csv(path_to_save + '/rho_' + category + '.csv')
                p_values.to_csv(path_to_save + '/p_' + category + '.csv')

                total_rho[category] = rho.loc['av. rating']
                total_p[category] = p_values.loc['av. rating']

                if plot:
                    pass
                # todo: add the creation of the map

    total_pd_rho = total_rho.ix[m.pd_metrics, header]
    total_pd_p = total_p.ix[m.pd_metrics, header]

    total_fr_rho = total_rho.ix[m.fr_metrics, header]
    total_fr_p = total_p.ix[m.fr_metrics, header]

    total_pd_rho.to_csv(path_to_save + '/rho_PD.csv')
    total_pd_p.to_csv(path_to_save + '/p_PD.csv')

    total_fr_rho.to_csv(path_to_save + '/rho_FR.csv')
    total_fr_p.to_csv(path_to_save + '/p_FR.csv')

    if plot:
        cols = ['All', 'Books', 'Communic.', 'Educat.', 'Finance', 'Games', 'Lifest.', 'Music', 'Photog.', 'Product.', 'Travel', 'Video']
        generate_heatmap(total_pd_rho, total_pd_p, cols, m.pd_rows, 'problem_discovery')
        generate_heatmap(total_fr_rho, total_fr_p, cols, m.fr_rows, 'feature_requests')

