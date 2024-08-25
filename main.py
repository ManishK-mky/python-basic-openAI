import pyttsx3

moon = pyttsx3.init()


# "RATE"
rate = moon.getProperty('rate')
print(rate)
moon.setProperty('rate' , 177)


# """VOLUME"""

volume = moon.getProperty('volume')
print(volume)
moon.setProperty('volume' , 1.0)

# """VOICE"""
voices = moon.getProperty('voices')
moon.setProperty('voice' , voices[1].id)

moon.say("How are you")
moon.say('My current speaking rate is '+ str(rate))
moon.say('hare krishna')
moon.say('hello anand how are u')
moon.runAndWait()

moon.stop()