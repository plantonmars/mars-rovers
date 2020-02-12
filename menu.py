from rover import Rover

""" 
    A work-in-progress application, using APIs derived from NASA to display data about the multiple
    Rovers that have explored Mars.
    
    version: 1.0
    
    author: plantonmars
"""

class Menu:
    def __init__(self):
        # Rover instances
        self.curiosity = Rover('curiosity')
        self.opportunity = Rover('opportunity')
        self.spirit = Rover('spirit')

        # Flags
        self.main_flag = True
        self.rover_flag = True

        self.choice = 0

    def display_menu(self):

        while self.main_flag:
            self._main_prompt()

    def _main_prompt(self):
        """ Helper function to display the main menu, this menu will be returned to after leaving other menus
        and will only stop when the user ends the application. """

        print("\nMARS ROVER APPLICATION")
        print("----------------------")
        print("Please select a Mars rover to learn more about!\n")
        print("1 - Curiosity")
        print("2 - Opportunity")
        print("3 - Spirit")
        print("4 - Exit")
        self._check_choice()
        self.rover_flag = True  # Allows user to re-enter a rover menu.
        if self.choice == 1:
            while self.rover_flag:
                self._rover_prompt(self.curiosity)
        elif self.choice == 2:
            while self.rover_flag:
                self._rover_prompt(self.opportunity)
        elif self.choice == 3:
            while self.rover_flag:
                self._rover_prompt(self.spirit)
        elif self.choice == 4:
            self.main_flag = False
        else:
            print("error: Please enter a choice provided!")

    def _rover_prompt(self, rover_obj):
        """ Helper function to display the menu of each individual rover """

        print(f"\n{rover_obj.name.upper()}")
        print("---------")
        print("1 - View Stats")
        print("2 - Search Captured Photos")
        print("3 - Photo Analysis")
        print("4 - Exit")
        self._check_choice()
        if self.choice == 1:
            rover_obj.describe_rover()
        elif self.choice == 2:
            print(f"\n{rover_obj.name.upper()} GALLERY")
            date = input("Enter a date in format (mm/dd/yyyy): ")
            rover_obj.search_photo(date)
        elif self.choice == 3:
            rover_obj.photo_analysis()
        elif self.choice == 4:
            self.rover_flag = False

    def _check_choice(self):
        try:
            self.choice = int(input("Enter Choice: "))
        except ValueError:
            print("\nOnly numbers can be entered.")



if __name__ == '__main__':
    menu = Menu()
    menu.display_menu()