# Two tortoises named A and B must run a race. 
# A starts with an average speed of 720 feet per hour. 
# Young B knows she runs faster than A, 
# and furthermore has not finished her cabbage.

# When she starts, 
# at last, she can see that A has a 70 feet lead 
# but B's speed is 850 feet per hour. 
# How long will it take B to catch A?

# More generally: 
# given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) 
# and a lead g (integer > 0) how long will it take B to catch A?
#
# The result will be an array hour, min, sec which is the time needed in hours, 
# minutes and seconds (round down to the nearest second) or a string in some languages.
#
# If v1 >= v2 then return -1, -1, -1.

def time_transform(sec):
    return [sec//3600, sec%3600//60, int(sec%60)]

def race(v1, v2, g):
    diff = v2 - v1
    return time_transform(g/diff*3600) if diff > 0 else [-1, -1, -1]

def test():
    print(race(720, 850, 70)) #[0, 32, 18]
    print(race(80, 91, 37)  )#[3, 21, 49]
    print(race(80, 100, 40) )#[2, 0, 0]

if __name__ == "__main__":
    test()