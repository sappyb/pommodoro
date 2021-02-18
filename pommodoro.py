import pyttsx3
import time

ctime = int(input("Enter the amount of time : "))
break_time_short = (3 // 20) * ctime
break_time_long = (30 // 20) * ctime
cycles = int(input("Enter number of cycles : "))

while True:
	engine = pyttsx3.init()
	engine.say("Start Pommodoro")
	engine.runAndWait()
	for i in range(cycles):
		time.sleep(ctime)
		engine.say("Break")
		engine.runAndWait()
		time.sleep(break_time_short)
		engine.say("Resume")
		engine.runAndWait()
	time.sleep(ctime)
	engine.say("Break for 30 min, end of Pomerade")
	engine.runAndWait()
	time.sleep(break_time_long)

