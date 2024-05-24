# create a method for turning the TV on/off. 
# create a method for setting the channel.
# create a method for the volume level of the TV.
# create another file for the TV Test named "TestTV" to call the function on TV.


# Define a class called TV
class TV():
    # Constructor method to initialize a TV instance
    def __init__(self, number_of_tv: str) -> None:
        # attributes
        self.on = False
        self.number_of_tv = number_of_tv
        self.channel = 1
        self.volume_level = 0
    # Method to turn on the TV
    def turn_on(self):
        self.on = True
    # Method to turn off the TV
    def turn_off(self):
        self.on = False
    # Method to display the current state of the TV
    def display_state(self):
        state = "on" if self.on else "off"
        print("The " + self.number_of_tv + " is " + state)
    # Method to set the preferred channel for the TV
    def prefer_channel (self, channel: int):
        self.channel = channel
     # Method to set the volume level for the TV
    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume_level = volume
        else:
            print("The volume must be between 0 and 100")
    #Method to display the current settings of the TV (channel and volume level)
    def display_settings(self):
        print ("The " + self.number_of_tv + " is set to channel " + str(self.channel) + "and the volume level is " + str(self.volume_level))
