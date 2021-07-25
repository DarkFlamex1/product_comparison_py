import pandas as pd

class info_struct:
    """
    This class represents the info for each product comparison.
    """

    # Dictionary storing all the scraped information
    def __init__(self):
        self.flavor_info = {
            "Flavor": '',
            "ABV": '',
            "Calories": '',
            "Can_Size": '',
            "Sugar": '',
            "Sizes_Costs": {},
        }
    
    """
    Helper function that sets the value in flavor info given a key and value.
    No error checking, can be implemented later.
    """
    def set(self, key, value):
        self.flavor_info.update({key:value})

    """
        Helper function that sets the value in of the sizes list given a value.
        No error checking, can be implemented later.
    """
    def set_costs_sizes(self, size, cost):
        self.flavor_info["Sizes_Costs"].update({size:cost})

    '''
    Return a pandas dataframe
    '''
    def get_dict_as_df(self):
        return pd.DataFrame.from_dict(self.flavor_info, orient='index')

    """
        Helper function that gets the value in flavor info given a key and value.
        No error checking, can be implemented later.
    """
    def get(self, key):
        return self.flavor_info.get(key)