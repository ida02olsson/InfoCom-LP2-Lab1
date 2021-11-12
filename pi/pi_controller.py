import requests
import time
import random
import click


def get_direction():
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
#    d_long = 0
#    d_la = 0
#    send_vel = False
#    c = click.getchar()
#    if c == '\x1b[D' or c =='a':
 #       click.echo('Left')
 #       send_vel = True
 #       d_long = -1
#        d_la = 0
 #   elif c == '\x1b[C' or c == 'd':
#        click.echo('Right')
#        send_vel = True
#        d_long = 1
#        d_la = 0
#    elif c == '\x1b[A' or c =='w':
#        click.echo('Up')
#        send_vel = True
#        d_long = 0
#        d_la = 1
#    elif c == '\x1b[B' or c == 's':
#        click.echo('Down')
 #       send_vel = True
 #       d_long = 0
 #       d_la = -1
##    else:
#        d_long = 0
 #       d_la = 0
#        click.echo('Invalid input :(')
#        send_vel = False
#    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
