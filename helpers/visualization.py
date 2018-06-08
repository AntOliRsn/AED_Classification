import os
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt


def pyplot_latent_space_atypial_events(x_proj, calendar_info, a_score, path_folder_out=None, name=None):
    """

    :param x_proj:
    :param calendar_info:
    :param path_folder_out:
    :param name:
    :return:
    """

    #Different possible colormap: seismic

    mask_isweekday = False
    mask_ishd = False

    if 'is_weekday' in calendar_info.columns:
        mask_isweekday = calendar_info.is_weekday.astype('bool')

    if 'is_hd' in calendar_info.columns:
        mask_ishd = calendar_info.is_hd.astype('bool')

    plt.figure(figsize=(17, 15))
    plt.scatter(x_proj[mask_isweekday, 0], x_proj[mask_isweekday, 1], marker='.', lw=2,
                c=a_score[mask_isweekday], cmap=plt.cm.get_cmap('seismic'), label='Week days')

    plt.scatter(x_proj[mask_ishd, 0], x_proj[mask_ishd, 1], marker='x', lw=2,
                c=a_score[mask_ishd], cmap=plt.cm.get_cmap('seismic'),label='Holiday Days')

    plt.scatter(x_proj[np.invert(mask_isweekday), 0], x_proj[np.invert(mask_isweekday), 1], marker='+', lw=2,
                c=a_score[np.invert(mask_isweekday)], cmap=plt.cm.get_cmap('seismic'), label='Weekend')

    plt.colorbar(label='a_score')
    #plt.clim(-0.5, 11.5)


    plt.legend()
    plt.title('Projection on the latent space')

    if name is None:
        name = 'latent_space_proj'

    if path_folder_out is not None:
        plt.savefig(os.path.join(path_folder_out, name + '.png'))

    plt.show()



def pyplot_latent_space_selected_atypial_events(x_proj, calendar_info, a_score, nb_events,
                                                path_folder_out=None, name=None):
    """

    :param x_proj:
    :param calendar_info:
    :param path_folder_out:
    :param name:
    :return:
    """

    #Different possible colormap: seismic

    mask_isweekday = False
    mask_ishd = False

    if 'is_weekday' in calendar_info.columns:
        mask_isweekday = calendar_info.is_weekday.astype('bool')

    if 'is_hd' in calendar_info.columns:
        mask_ishd = calendar_info.is_hd.astype('bool')

    # getting most atypical days
    lim_value = a_score.sort_values(ascending=False).reset_index(drop=True)[nb_events-1]
    mask_aed = a_score >= lim_value

    plt.figure(figsize=(17, 15))
    plt.scatter(x_proj[mask_isweekday, 0], x_proj[mask_isweekday, 1], marker='.', lw=2,
                c='blue', label='Week days')

    plt.scatter(x_proj[mask_ishd, 0], x_proj[mask_ishd, 1], marker='s', lw=3,
                c='blue', label='Holiday Days')

    plt.scatter(x_proj[np.invert(mask_isweekday), 0], x_proj[np.invert(mask_isweekday), 1], marker='+', lw=2,
                c='blue', label='Weekend')

    plt.scatter(x_proj[mask_aed, 0], x_proj[mask_aed, 1], marker='o', lw=1,
                c='red', label='ae')

    #plt.colorbar(label='a_score')
    #plt.clim(-0.5, 11.5)


    plt.legend()
    plt.title('Projection on the latent space')

    print(lim_value)

    if name is None:
        name = 'latent_space_proj'

    if path_folder_out is not None:
        plt.savefig(os.path.join(path_folder_out, name + '.png'))

    plt.show()




