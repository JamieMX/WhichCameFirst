#Class that models an item used in the WhichCameFirst game

class Item:
    """A class modelling an item in the WhichCameFirst game"""
    
    def __init__(self, item_name, item_year, item_fact=''):
        self.name = item_name
        self.year = item_year
        self.age = (2022 - item_year)
        self.fact = item_fact

    def get_name(self):
        """returns name value"""
        return self.name
    
    def get_year(self):
        """returns year value"""
        return self.year
    
    def get_age(self):
        """returns age value"""
        return self.age
    
    def get_fact(self):
        """returns fact value"""
        return self.fact

    