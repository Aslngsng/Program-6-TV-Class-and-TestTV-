# create a method for turning the TV on/off. 
# create a method for setting the channel.
# create a method for the volume level of the TV.
# create another file for the TV Test named "TestTV" to call the function on TV.

class TV():
    def __init__(self) -> None:
        self.on = False
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
tv1 = TV()
tv1.turn_on()
if tv1.on: 
    print("On")
else:
    print("off")
tv2 = TV()
tv2.turn_on()
if tv2.on: 
    print("On")
else:
    print("off")