from os import rename
from time import sleep

# Constants
MSG_PATH = "hddledsfmsg.txt"
FOLDER_A_PATH = "C:/Users/Ben Alford/Desktop/hddledsfa"
FOLDER_B_PATH = "C:/Users/Ben Alford/Desktop/hddledsfb"
MOVE_DATA_PATH = "hddledsfmvdat"
BIT_SLEEP_TIME = 6 
ONE_SLEEP_TIME = 2
SECURITY_BIT_REPEATS = 3
SECURITY_BIT_SLEEP_TIME = 4

f = open(MSG_PATH,"r")
msg = list(f.read())
f.close()
m2state = "a"
fap = FOLDER_A_PATH + "/" + MOVE_DATA_PATH
fbp = FOLDER_B_PATH + "/" + MOVE_DATA_PATH

def move(m2state):
    if m2state == "a":
        rename(fap,fbp)
    elif m2state == "b":
        rename(fbp,fap)

print("Starting in 5 seconds...")
sleep(5)
try:
    for bit in msg:
        for i in range(SECURITY_BIT_REPEATS):
            if bit == "0":
                print("0====================")
            elif bit == "1":
                print("1============================================================")
            move(m2state)
            if m2state == "a":
                m2state = "b"
            elif m2state == "b":
                m2state = "a"
            if bit == "1":
                sleep(ONE_SLEEP_TIME)
                print("========================================")
                move(m2state)
                if m2state == "a":
                    m2state = "b"
                elif m2state == "b":
                    m2state = "a"
            sleep(SECURITY_BIT_SLEEP_TIME)
        sleep(BIT_SLEEP_TIME)

# Cleanup
finally:
    if m2state == "b":
        move("b")
