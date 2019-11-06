# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. 

# The city provides its citizens with a Walk Generating App on their phones 
# -- everytime you press the button 
# it sends you an array of one-letter strings representing directions to walk (eg. 'n', 's', 'w', 'e'). 
# You always walk only a single block in a direction 
# and you know it takes you one minute to traverse one city block, 
# so create a function that will 
# return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, 
# of course, return you to your starting point. Return false otherwise.


def isValidWalk(walk:list):
    return False if len(walk) != 10 else True if walk.count('n') == walk.count('s') and walk.count("w") == walk.count('e') else False

def test():
    print(isValidWalk(['n','s','n','w','e','s','n','s','w','e'])        ) #True
    print(isValidWalk(['s','s','n','e','e','s','n','s','w','w'])        ) #False
    print(isValidWalk(['w','e','n','w','e','s','e','s','w','n','n','s'])) #False

if __name__ == "__main__":
    test()