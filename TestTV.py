from TV import TV

tv1 = TV("tv1")
tv1.turn_on() 
tv1.prefer_channel(30)
tv1.set_volume(3)
tv2 = TV("tv2")
tv2.turn_on()
tv2.prefer_channel(3)
tv2.set_volume(2)

tv1.display_settings()
tv2.display_settings()