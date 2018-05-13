import pyglet as pg             #to use Pyglet in this program, need to install abvin
import speech_recognition as sr
import subprocess


def play_short_audio(filename):
    tune = pg.resource.media(filename,streaming= False)  #streaming set to false to lower cpu speed as file is short
    tune.play()
    pg.clock.schedule_once(loop_exit, 2)
    pg.app.run()

# play_short_audio('resources/to-the-point.mp3') #testing function


def loop_exit(dt):
    pg.app.exit()


def say(text):
    subprocess.call('say ' + text, shell= True)


recorder = sr.Recognizer()


def init_speech():
    print("Listening...")
    play_short_audio('resources/to-the-point.mp3')
    # print("reached here")

    with sr.Microphone() as mic:                # recording here
        # print("Start")
        audio = recorder.listen(mic)

    play_short_audio('resources/decay.mp3')    # indicates the recording has been completed

    command = ""
    try:
        command = recorder.recognize_google(audio)   # use google to understand command
    except:
        print("Sorry, unable to understand")        # error message

    print(command)
    say("You said " + command)

init_speech()
