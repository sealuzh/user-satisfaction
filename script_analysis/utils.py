from settings import *


def get_categories(versions_file):
    """
    Save all the single files for the categories with more than 10 versions
    :param versions_file:       the frame all the apps with more versions
    :return:                    save the resulting frames in category folder
                                returns a list of categories
    """
    list_categories = versions_file.cat.unique()
    for category in list_categories:
        category_frame = versions_file[versions_file.cat == category]
        if len(category_frame) >= min_number_cat:
            category_frame.to_csv(categories + '/' + category + '.csv', index=False)
    return list_categories
