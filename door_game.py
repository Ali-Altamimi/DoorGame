from door import Door
from random import randint


class DoorGame:
    
    def __init__(self, number_of_doors):
        self.list_of_doors = [Door() for i in range(number_of_doors)]
        self.list_of_doors[randint(0, 2)].set_is_car(True)


    def play(self):
        self.select_door()
        self.open_door()
        self.switch_doors()
        return self.results()

    def select_door(self):
        random_number = randint(0, 2)
        self.list_of_doors[random_number].set_is_selected(True)

    def open_door(self):
        random_number = randint(0, 2)
        if self.list_of_doors[random_number].get_is_selected() or self.list_of_doors[random_number].get_is_car():
            return self.open_door()
        else:
            self.list_of_doors.pop(random_number)
            return

    def switch_doors(self):
        if self.list_of_doors[0].get_is_selected():
            self.list_of_doors[0].set_is_selected(False)
            self.list_of_doors[1].set_is_selected(True)
        else:
            self.list_of_doors[0].set_is_selected(True)
            self.list_of_doors[1].set_is_selected(False)

    def results(self):
        if self.list_of_doors[0].get_is_selected() and self.list_of_doors[0].get_is_car():
            return True
        elif self.list_of_doors[1].get_is_selected() and self.list_of_doors[1].get_is_car():
            return True
        else:
            return False

