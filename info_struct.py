
class info_struct:
    """
    This class represents the info for each product comparison.
    """

    # Dictionary storing all the scraped information
    flavor_info = {
        "Flavor": '',
        "ABV": '',
        "Calories": '',
        "Can_Size": '',
        "Gluten_Free": '',
        "Carbs": '',
        "Sugar": '',
        "Sizes": [],
        "Costs": [],
    }

    """
    Helper function that sets the value in flavor info given a key and value.
    No error checking, can be implemented later.
    """
    def set(self, key, value):
        self.flavor_info.update({key:value})

    """
        Helper function that gets the value in flavor info given a key and value.
        No error checking, can be implemented later.
    """
    def get(self, key):
        return self.flavor_info.get(key)