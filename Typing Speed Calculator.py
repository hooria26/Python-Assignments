from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput.split()) / time_R
    return round(speed, 2)

test = ["Computer Organization And Assembly Language", "Differential Equations", "Programming Fundamentals", "Numerical Computing", "Digital Logic Design", "Fundamentals Of Management","Maths","Physics","Calculus","Algebra","Social Studies"]
test1 = r.choice(test)
print("*****Typing Speed Calculator:*****")
print(test1)
print()
time_1 = time()
testinput = input("Enter: ")
time_2 = time()

print("Speed : ", speed_time(time_1, time_2, testinput), " w/s")
print("Errors:", mistake(test1, testinput))
