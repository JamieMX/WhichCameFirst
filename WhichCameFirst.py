#Class that models the game itself. Uses the Item class for its content.

import Item
import random
class WhichCameFirst:
    def __init__(self):
        self.running = True
        self.playing = True
        self.game_start_message = "The game will present you with option A and B.\nChoose whichever you think is older"\
            " to get a point."
        self.score = 0
        #some default examples for testing
        mark_twain = Item.Item("Mark Twain", 1835)
        bicycle = Item.Item("The bicycle", 1817)
        mayonnaise = Item.Item("Mayonnaise", 1756)
        self.item_list = [mark_twain, bicycle, mayonnaise]

    #method called when an item is added to the game
    #basically functional
    def add_item(self):
        """Method used to add new item to game. Appends created item to list."""
        print("Enter a name for the item to add \n")
        item_name = self.get_input()
        print("Enter the year the item was created or born \n")
        item_year = self.get_input()
        print("Enter a fact about the item")
        item_fact = self.get_input()
        new_item = Item.Item(item_name, item_year, item_fact)
        self.item_list.append(new_item)

    #method called to determine what is correct answer
    def compare_age(self, item_one, item_two):
        if item_one.get_age() > item_two.get_age():
            return item_one
        else:
            return item_two

    def get_input(self):
        user_input = input()
        return user_input

    def pick_items(self):
        """Method called by play game function to select two random items to play the game with"""
        positions = []
        for i in range(0, 2):
            positions.append(random.randint(0, len(self.item_list)-1))
        chosen_items = []
        chosen_items.append(self.item_list[positions[0]])
        chosen_items.append(self.item_list[positions[1]])
        return(chosen_items)
        print("A) " + chosen_items[0])
        print("Or...")
        print("B) " + chosen_items[1])
        


    def play_game(self):
        """Method called when user chooses run game option."""
        print(self.game_start_message)
        score = 0
        while self.playing:
            print("You currently have " + str(self.score) + " points.")
            print("Enter A or B to make a choice or X to quit the game")
            print("Which came first?: ")
            options = self.pick_items()
            if options[0].age > options[1].age:
                correct = "A"
            else:
                correct = "B"
            print("A) " + options[0].get_name())
            print("Or...")
            print("B) " + options[1].get_name())
            print("(Press X to quit.)")
            response = self.get_input()
            print("You chose: " + response)
            if response.upper() == correct:
                score = score + 1
                print("Correct!")
            elif response.upper() == "X":
                print("Thanks for playing.")
                break
            else:
                print("Incorrect!")
        pass

        """
            print rules and instructions
            while running:
                show question
                    if correct add point
                    if wrong pass
                    if end game, end game
                show new question
            """

    #Use this method just to show item names
    #functional
    def show_items(self):
        print("The following items are part of the game: \n")
        for item in self.item_list:
            print(item.get_name() + "\n")

    #functional
    def kill_program(self):
        self.running = False

    def start_program(self):
        while self.running:
            print("Which came first? \nPlease enter a number to make your choice from the list below \n"\
                "1. Play game \n2. Add a new item to the game \n3. Show all items present in the game \n"\
                    "4. Close the game.\n")
            user_choice = self.get_input()
            if user_choice == "1":
                self.play_game()
            elif user_choice == "2":
                self.add_item()
            elif user_choice == "3":
                self.show_items()
            elif user_choice == "4":
                self.kill_program()

            
    
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
    


