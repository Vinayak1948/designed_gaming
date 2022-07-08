import random
def gameWin():
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Computer turn: Rock(r) Paper(p) or Scissor(s) ?")
RandomNo = random.randint(1,3)

if RandomNo==1:
    comp='r'
elif RandomNo==2:
    comp = 'p'
elif RandomNo == 3:
    comp = 's'
you= input("Your's turn: Rock(r) Paper(p) or Scissor(s) ?")
a = gameWin()

print(f"Computer Chose {comp}")
print(f"You Chose {you}")

if a== None:
    print("The Game is TIE!")
elif a:
    print("You Won!")
else :
    print("You Lose!")