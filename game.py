import random
win_num=random.randint(1,100)
##print(win_num)
guess=1
num=int(input("Enter your number between 1 and 100:"))

game_over=False
while not game_over:
    if(win_num==num):
        print(f"Game Over !! and you guessed this number in {guess} times")
        game_over=True
    else:
        if(win_num>num):
            print("Value too low !!")
            guess=guess+1
            num=int(input("Enter your number again:"))
        
        else:
            print("Value too high !!")
            guess=guess+1
            num=int(input("Enter your number again:"))
