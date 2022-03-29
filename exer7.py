# import time
# from pygame import mixer
# n=5
# while True:
#
#     time.sleep(n)
#     # Starting the mixer
#     mixer.init()
#
#     # Loading the song
#     mixer.music.load("Drink water.mp3")
#
#     # Setting the volume
#     mixer.music.set_volume(0.7)
#
#     # Start playing the song
#     mixer.music.play()
#
#     print("if you drink water than type done to stop the music")
#     query = input("  ")
#
#     if query == 'done':
#
#         # Pausing the music
#         # mixer.music.pause()
#     # elif query == 'r':
#     #
#     #     # Resuming the music
#     #     mixer.music.unpause()
#     # elif query == 'e':
#     #
#     #     # Stop the mixer
#         mixer.music.stop()
#         n=n*2
# n=3
# while True:
#
#     time.sleep(n)
#
#     mixer.init()
#
#     mixer.music.load("Alarm.mp3")
#
#     # Setting the volume
#     mixer.music.set_volume(0.7)
#
#     # Start playing the song
#     mixer.music.play()
#
#     print("if you drink water than type done to stop the music")
#     query = input("  ")
#
#     if query == 'done':
#
#         # Pausing the music
#         # mixer.music.pause()
#     # elif query == 'r':
#     #
#     #     # Resuming the music
#     #     mixer.music.unpause()
#     # elif query == 'e':
#     #
#     #     # Stop the mixer
#         mixer.music.stop()
#         n=n*2
#

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs =10
    eyessecs = 15

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Drink water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('Alarm.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('Drink water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")


