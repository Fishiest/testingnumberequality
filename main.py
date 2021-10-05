
#This is my first peice of python don't judge it :)

def isgood():
    print("Is my code good? [Y/N]")
    if input() == "N":
        print("Wrong")
        isgood()
    else:
        print("Yes that is correct :)")

def checkinganswer():
    #Checking if the user meant what they meant
    if input() == "Y":
        () #Do nothing
    else:
        if input() == "N":
            getnumbers()
        else:
            print ("Your answer to is that correct was not 'Y' or 'N', assuming 'N'.") #I was too dumb to figure out how to start this bit of code over
            checkinganswer()

def checkansweragain():
    # Checking if the user meant what they meant: part two, electric boogaloo
    if input() == "Y":
        () #Do nothing
    else:
        if input() == "N":
            getnumbers()
        else:
            print ("Your answer to is that correct was not 'Y' or 'N', assuming 'N'.") #I was too dumb to figure out how to start this bit of code over
            getnumbers()
def getnumbers():
    print ("What will your first number be? (MUST BE NON WRITTEN AND WITHOUT COMMAS):")
    firstnumber = int(input())
    #checkinganswer()
    print("You said",firstnumber,", is that correct? [Y/N]")
    checkinganswer()
    print ("What will your second number be? (MUST BE NON WRITTEN AND WITHOUT COMMAS):")
    secondnumber = int(input())
    #checkingansweragain()
    print("You said",secondnumber,", is that correct? [Y/N]")
    checkansweragain()
    #finally testing the numbers for equality or inequality
    if firstnumber > secondnumber:
        print ("Your first number is greater than your second number!")
    else:
        if firstnumber < secondnumber:
            print ("Your first number is less than your second number!")
        else:
            if firstnumber == secondnumber:
                print ("Your first number and second number are equal!")

#haha this needs to be here otherwise the code will die
getnumbers()
isgood()