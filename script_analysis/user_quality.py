from utils import *
from correlations import *
import metrics as m
import pandas as pd
import os

folder_name = '/user_quality'
not_to_consider = ['Entertainment', 'Personalization', 'Tools', 'Social', 'Education']


def correlation_user_quality(code_metrics, user_metrics, versions, plot):
    user_frame = pd.read_csv(user_metrics)
    code_frame = pd.read_csv(code_metrics)

    code_frame = code_frame.merge(user_frame, left_on='id', right_on='id')
    get_categories(pd.read_csv(versions))

    # Compute without the distinction per category
    total_rho, total_p = \
        compute_overall_correlations(code_frame, ['av. rating'] + m.code_metrics + m.user_metrics, folder_name)

    pd_rho = total_rho.ix[m.pd_metrics, m.code_metrics]
    pd_p = total_p.ix[m.pd_metrics, m.code_metrics]
    fr_rho = total_rho.ix[m.fr_metrics, m.code_metrics]
    fr_p = total_p.ix[m.fr_metrics, m.code_metrics]

    path_to_save = correlations + folder_name

    pd_rho.to_csv(path_to_save + '/pd_rho.csv')
    fr_rho.to_csv(path_to_save + '/fr_rho.csv')
    pd_p.to_csv(path_to_save + '/pd_p_value.csv')
    fr_p.to_csv(path_to_save + '/fr_p_value.csv')

    if plot:
        generate_heatmap(pd_rho, pd_p, m.code_metrics, m.pd_rows, 'pd_quality')
        generate_heatmap(fr_rho, fr_p, m.code_metrics, m.fr_rows, 'fr_quality')

    for filename in os.listdir(categories):
        if filename.endswith('.csv'):

            # Get category name, filter frame and calculate correlations
            category = filename[:-4]
            if category not in not_to_consider:
                category_ids = pd.read_csv(categories + '/' + filename)['id']
                print 'Elaborating ', category
                aux = code_frame[code_frame['id'].isin(category_ids)]
                rho, p_values = calculate_correlation(aux, ['av. rating'] + m.code_metrics + m.user_metrics)

                # Remove empty columns
                rho = rho.dropna(how='all').dropna(axis=1, how='all')
                p_values = p_values.dropna(how='all').dropna(axis=1, how='all')

                pd_rho = rho.ix[m.pd_metrics, m.code_metrics]
                pd_rho = pd_rho.dropna(how='all').dropna(axis=1, how='all').dropna(axis=0, how='all')
                pd_p = p_values.ix[m.pd_metrics, m.code_metrics]
                pd_p = pd_p.dropna(how='all').dropna(axis=1, how='all').dropna(axis=0, how='all')

                fr_rho = rho.ix[m.fr_metrics, m.code_metrics]
                fr_rho = fr_rho.dropna(how='all').dropna(axis=1, how='all').dropna(axis=0, how='all')
                fr_p = p_values.ix[m.fr_metrics, m.code_metrics]
                fr_p = fr_p.dropna(how='all').dropna(axis=1, how='all').dropna(axis=0, how='all')

                # Save files
                path_to_save = correlations + folder_name

                pd_rho.to_csv(path_to_save + '/pd_rho_' + category + '.csv')
                pd_p.to_csv(path_to_save + '/pd_p_' + category + '.csv')

                fr_rho.to_csv(path_to_save + '/fr_rho_' + category + '.csv')
                fr_p.to_csv(path_to_save + '/fr_p_' + category + '.csv')

                if plot:
                    pd_rows = [x.replace('PD + ', '')[:7] for x in pd_rho.index]
                    fr_rows = [x.replace('FR + ', '')[:7] for x in fr_rho.index]
                    generate_heatmap(pd_rho, pd_p, pd_rho.columns, pd_rows, 'PD_' + category)
                    generate_heatmap(fr_rho, fr_p, fr_rho.columns, fr_rows, 'FR_' + category)

