import random
import time
def game(comp , you): #made a functuon to choose winner or returns who wins
    if comp == you:
        return None
    if comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    if comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    if comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

print('''A wild COMPUTER wants to battle!

    ''')





    
    

print('''What do you choose
''')

you = input("Snake(s) Gun(g) or Water(w)?\n") #taking input from user 

rand= random.randint(1,3) #using randint from random module
if rand == 1:
    comp = 's'
elif rand == 2:
    comp = 'g'
elif rand == 3:
    comp = 'w'
time.sleep(0.5)
print(f'''
Computer choosed {comp} and you choosed {you}''')

a = game(comp, you)
if a == None:
    print("The game is tie!")
elif a:
    print('''
Lucky FAM 
You won!
Enojy''')
else:

    print('''
Ouch you lost better luck next time bro 
You lost! Go and die ''')

