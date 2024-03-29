from random import randint
number=randint(1,1000)
chances=5
while chances>0:
    n=int(input("Guess the number? "))
    chances-=1
    if n==number:
        print("YOU WON THE GAME!!")
        break
    elif n>number:
        print("Guessed number is greater than the actual number")
        print("You have",chances,"left")
    else:
        print("Guessed number is lesser than the actual number")
        print("You have",chances,"left")
    
    
else:
    print("The number is :",number)
    print("YOU LOST")
