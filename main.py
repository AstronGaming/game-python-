import random
def game(comp , you):
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





    
    
print("computer's turn snake(s) gun(g) or water(w?")
rand= random.randint(1,3)
if rand == 1:
    comp = 's'
elif rand == 2:
    comp = 'g'
elif rand == 3:
    comp = 'w'
you = input("your turn snake(s) gun(g) or water(w?")

a = game(comp, you)
if a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("You loose!")