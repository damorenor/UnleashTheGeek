import sys


class Pod:
    def __init__(self):
        self.x = 0
        self.y = 0


class Checkpoint:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dist = 0
        self.angle = 0


pod = Pod()
opp = Pod()
next = Checkpoint()

# game loop
while True:
    # game input
    pod.x, pod.y, next.x, next.y, next.dist, next.angle = [
        int(i) for i in input().split()
    ]
    opp.x, opp.y = [int(i) for i in input().split()]

    # game logic
    thrust = 100
    boost = True
    if next.angle > 90 or next.angle < -90:
        thrust = 10
    elif next.angle > 45 or next.angle < -45:
        thrust = 50
    elif next.dist < 700:
        thrust = 20
    elif next.dist > 1500 and boost:
        thrust = "BOOST"
        boost = False

    print(f"{next.x} {next.y} {thrust}")
