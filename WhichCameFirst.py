#Class that models the game itself. Uses the Item class for its content.

import Item
class WhichCameFirst:
    def __init__(self):
        self.item_list = []

    #method called when an item is added to the game
    def add_item(self, new_item_name, new_item_year):
        """Method used to add new item to game. Appends created item to list."""
        new_item = Item(new_item_name, new_item_year)
        self.item_list.append(new_item)

    #method called to determine what is correct answer
    def compare_age(self, item_one, item_two):
        if item_one.get_age() > item_two.get_age():
            return item_one
        else:
            return item_two
    
    """while running
            if input = add item
                run add item
            if input = view items
                run view items
            if input = play game
                run game
                    pick X and Y from list of items
                    which came first X or Y
                        if entry = x and x = correct
                            give point
                            next round
                        else
                            no point
                            next round 
                """
    

