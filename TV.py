# create a method for turning the TV on/off. 
# create a method for setting the channel.
# create a method for the volume level of the TV.
# create another file for the TV Test named "TestTV" to call the function on TV.

class TV():
    def __init__(self, number_of_tv: str) -> None:
        self.on = False
        self.state = number_of_tv
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def display_state(self):
        state = "on" if self.on else "off"