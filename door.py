class Door:

    def __init__(self, is_car=False, is_selected=False):
        self.is_car = is_car
        self.is_selected = is_selected

    def get_is_car(self):
        return self.is_car

    def set_is_car(self, is_there_a_car):
        self.is_car = is_there_a_car

    def get_is_selected(self):
        return self.is_selected

    def set_is_selected(self, is_selected):
        self.is_selected = is_selected
