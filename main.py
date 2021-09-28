#Getting the numbers
print ("What will your first number be? (MUST BE NON WRITTEN):")
firstnumber = input()
print ("What will your second number be? (MUST BE NON WRITTEN):")
secondnumber = input()
#Testing the numbers
if firstnumber > secondnumber:
    print ("Your first number is greater than your second number!")
else:
    if firstnumber < secondnumber:
        print ("Your first number is less than your second number!")
    else:
        if firstnumber == secondnumber:
            print ("Your first number and second number are equal!")