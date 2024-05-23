# create a method for turning the TV on/off. 
# create a method for setting the channel.
# create a method for the volume level of the TV.
# create another file for the TV Test named "TestTV" to call the function on TV.

class TV():
    def __init__(self, number_of_tv: str) -> None:
        self.on = False
        self.number_of_tv = number_of_tv
        self.channel = None
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def display_state(self):
        state = "on" if self.on else "off"
    def prefer_channel (self, channel: int):
        self.channel = channel
        print (self.number_of_tv + "is set to channel " + self.channel)