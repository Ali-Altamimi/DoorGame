from door import Door
from random import randint


class DoorGame:
    global doors
    global selected_door

    def __init__(self, number_of_doors=3):
        self.selected_door = 0
        self.doors = number_of_doors
        self.list_of_doors = [Door() for i in range(self.doors)]
        self.list_of_doors[randint(0, self.doors - 1)].set_is_car(True)

    def play(self):
        self.select_door()
        while (self.doors - 1) != 1:
            self.open_door()
            self.switch_doors()
        return self.results()

    def select_door(self):
        random_number = randint(0, self.doors - 1)
        self.selected_door = random_number
        self.list_of_doors[random_number].set_is_selected(True)

    def open_door(self):
        random_number = randint(0, self.doors - 1)
        if self.list_of_doors[random_number].get_is_selected() or self.list_of_doors[random_number].get_is_car():
            self.open_door()
        else:
            if random_number <= self.selected_door:
                self.selected_door -= 1
            self.doors -= 1
            self.list_of_doors.pop(random_number)

    def switch_doors(self):
        random_number = randint(0, self.doors - 1)
        if self.list_of_doors[random_number].get_is_selected():
            self.switch_doors()
        else:
            self.list_of_doors[random_number].set_is_selected(True)
            self.list_of_doors[self.selected_door].set_is_selected(False)
            self.selected_door = random_number

    def results(self):
        if self.list_of_doors[0].get_is_selected() and self.list_of_doors[0].get_is_car():
            return True
        elif self.list_of_doors[1].get_is_selected() and self.list_of_doors[1].get_is_car():
            return True
        else:
            return False
