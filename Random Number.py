from random import randint
count = 0
n = int(input())
for x in range(1,n+1):
    guessNumber = int(input("Guess the number between 1 to n: "))
    randomNumber = randint(1,n)

    if guessNumber == randomNumber:
        print("You Have Won!")
        break
    else:
        print("No")
        print("Random number was: ", randomNumber)
        count = count + 1

        if(count==n):
            print("You Have Lost!")




