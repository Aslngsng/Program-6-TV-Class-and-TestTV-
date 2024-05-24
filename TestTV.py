# Import the TV class from the “TV”
from TV import TV

# Create an instance of TV named 'tv1' with the identifier 'tv1'
tv1 = TV("tv1")
tv1.turn_on()
tv1.prefer_channel(30)
tv1.set_volume(3)
# Create another instance of TV named 'tv2' with the identifier 'tv2'
tv2 = TV("tv2")
tv2.turn_on()
tv2.prefer_channel(3)
tv2.set_volume(2)

# Display the settings of tv1 and tv2
tv1.display_settings()
tv2.display_settings()
