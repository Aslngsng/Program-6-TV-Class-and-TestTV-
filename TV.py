# create a method for turning the TV on/off. 
# create a method for setting the channel.
# create a method for the volume level of the TV.
# create another file for the TV Test named "TestTV" to call the function on TV.

class TV():
    def __init__(self, number_of_tv: str) -> None:
        self.on = False
        self.number_of_tv = number_of_tv
        self.channel = 1
        self.volume_level = 0

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def display_state(self):
        state = "on" if self.on else "off"
        print("The " + self.number_of_tv + " is " + state)

    def prefer_channel (self, channel: int):
        self.channel = channel

    def set_volume(self, volume):
        if volume <= 0 or volume > 100:
            self.volume_level = volume
        else:
            print("The volume must be between 0 and 100")
    
    def display_settings(self):
        print ("The " + self.number_of_tv + " is set to channel " + str(self.channel) + "and the volume level is " + self.volume_level)