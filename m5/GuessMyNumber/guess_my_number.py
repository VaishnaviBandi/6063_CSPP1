l = 0
h = 100
print("Enter a number between 0 to 100")
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while 1: 
    d = (l + h)//2
    print("Is"+ " " + str(d) + " " + "the number on your mind")
    answer = input() 
    if answer == "c":
        print("The nummber is" + " " + str(d))
        break
    elif answer == "h":
        l = d
    elif answer == "l":
        h = d 
