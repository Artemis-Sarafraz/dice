import random

while True: 
    player=input("what do you want to do ?   1.play or 2.exit    pleas choose one ! \n enter : " )
    if (player == "play" or 1):
        result = random.randint(1 ,6)
        print("your number is : " , result)
        if (result == 6):
            print ("you can play again")
        else:
            break
        print("your number is : ")
    elif (player == "exit" or 2) :
        print("Thank you for join us!" )
        break
    else :
        print("sorry ! your number is not correct !")
        
    gitbash