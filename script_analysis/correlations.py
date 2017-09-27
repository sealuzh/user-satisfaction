import pandas as pd
import scipy.stats as st
import numpy as np
import os
import math

import plotly.plotly as py
import plotly.graph_objs as go

from settings import *


def calculate_correlation(metric_frame, metrics):
    """
    Calculate spearman correlations for the given frame and for the given metrics
    :param metric_frame:            the frame of values
    :param metrics:                 the metrics to use
    :return:                        two dataframe:
                                        one with the rho values
                                        one with the p-values
    """
    rho, p_values = st.spearmanr(metric_frame.loc[:, lambda x: metrics])
    rho_frame = pd.DataFrame(rho, index=metrics, columns=metrics)
    p_frame = pd.DataFrame(p_values, index=metrics, columns=metrics)
    return rho_frame, p_frame


def compute_overall_correlations(frame, metrics, folder_name):
    rho, p_values = calculate_correlation(frame, metrics)

    # Save files
    path_to_save = correlations + folder_name
    if os.path.exists(path_to_save):
        os.system('rm -rf ' + path_to_save)
    os.mkdir(path_to_save)

    rho.rename(columns={'av. rating': 'All'}, inplace=True)
    p_values.rename(columns={'av. rating': 'All'}, inplace=True)

    return rho, p_values


def generate_heatmap(correlation_frame, p_values, x_axes, y_axes, filename='heatmap'):
    """Creates an heat map
    @:param correlation_frame: pandas frame that contains the values to plot
    @:param p_values: the pandas frame that contains the p-values
    @:param x_axes: the axes to render to the x axis
    @:param y_axes: the axes to render to the y axis
    @:param filename: the file for the image to plot out
    @:return it saves the image to the specified path with the name as argument
    """

    x_axes = [x[:10] for x in x_axes]
    y_axes = [x[:10] for x in y_axes]

    matrix = correlation_frame.as_matrix()
    matrix = np.around(matrix, decimals=2)

    ps = p_values.as_matrix()
    ps = np.around(ps, decimals=2)
    np.set_printoptions(formatter={'float': '{: 0.2f}'.format})

    annotations = []
    for n, row in enumerate(matrix):
        for m, val in enumerate(row):
            p = ps[n][m]
            if p >= 0.10 or abs(val) < 0.39:
                aux = '~'
            else:
                if val > 0:
                    aux = str(val)[:4]
                else:
                    aux = str(val)[:5]
                if p >= 0.05:
                    aux = aux+'*'

            if math.isnan(val):
                aux = '/'
            annotations.append(
                dict(
                    text=str(aux),
                    x=x_axes[m], y=y_axes[n],
                    font=dict(color='gray' if aux == '/' else 'white', size=50),
                    showarrow=False)
                )
    data = [
    go.Heatmap(
        z=matrix,
        x=x_axes,
        y=y_axes,
        zmin=-1,
        zmax=1,
        showscale=False
    )]
    layout = go.Layout(
        annotations=annotations,
        xaxis=dict(
            tickangle=45,
            tickfont=dict(
                size=50
                ),
            ),
        yaxis=dict(
            tickangle=0,
            tickfont=dict(
                size=50
                ),
            ),
        autosize=False,
        width=3000,
        height=2000,
        margin=go.Margin(
            l=250,
            r=50,
            b=260,
            t=10,
            pad=4
        )
        )
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename=images + filename+'.pdf')
