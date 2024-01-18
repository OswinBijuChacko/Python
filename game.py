import random 
num = random.randint(0,10)
players={}
4
def player():
	n = int(input("Enter the number of player:"))
	for i in range(n):
		name = input("Enter the player name:")
		players[name]=0;
def one(name):
    print("'Truth' (+10 points)")
    print("Confess a truth to the group......;)")
    ask = input("Did you do it(y/n):")
    if ask == 'y':
            players[name]+=10
    else:
            players[name]+=0
            pass
    
def two(name):
    print("'Dare' (+10 points)")
    print("Do a dare proposed by any other player......")
    ask = input("Did you chicken out(Y/N):")
    if ask == "Y":
        print("Oh! -20 for you then...")
        players[name]-=20
    else:
        print("Good! +20 for you...")
        players[name]+=20
        
def three(name):
    print("'Skip' (-10 points)")
    print("Get to skip a task......")
    players[name]-=10

def four(name):
    print("'Make a loud animal noice' (+30 points)")
    print("Make a loud noice of any animal recomended by the group......")
    ask = input("Did you do it(Y/N):")
    if ask == "N":
        print("Oh! -20 for you then...")
        players[name]-=20
    else:
        print("Nice +30 for you...")
        players[name]+=30
        pass
        
def five(name):
    print("'' (+30 points)")
    print("Make a loud noice of any animal recomended by the group......")
    ask = input("Did you do it(Y/N):")
    if ask == "N":
        print("Oh! -20 for you then...")
        players[name]-=20
    else:
        print("Nice +30 for you...")
        players[name]+=30
        pass

def six(name):
    print("'Say now...'(+30 points)")
    print("Just answer truley what i ask .....")
    print("Let me also have some fun to :D...")
    anum = random.randint(0,9)
    players[name]+=20
    if anum == 0:
            print("Whats your biggest regret")
    elif anum == 1:
            print("When was the last time you cried")
    elif anum == 2:
            print("Ever broke a law?")
    elif anum == 3:
            print("If you HAD to,who would you kiss in the room")
    elif anum == 4:
            print("Most disgusting thing ever done by you")
    elif anum == 5:
            print("Is your crush in the room ;)")
    elif anum == 6:
            print("Worst thing you said to anyone")
    elif anum == 7:
            print("Favourite character")
    elif anum == 8:
            print("Who do you hate in the room")
    elif anum == 9:
            print("What would be your 3 wishes")
    ask = input("Did you do it(y/n):")
    if ask == 'y':
            print("Nice")
    else:
            print("Do it then")
            
def seven(name):
    print("'Captain's Orders...'(+30 points)")
    print("DO These excersices .....")
    ex=input("Will you do the excercise (Y/N):")
    anum = random.randint(0,4)
    if ex =="y":
      players[name]+=30
      if anum == 0:
              print("5 squats. NOW")
      elif anum == 1:
             print("I like you so just smile for me :D")
      elif anum == 2:
             print("5 jumping jacks.NOW")
      elif anum == 3:
             print("Raise your arm for 10s")
    else:
           players[name]-=20

def eight(name):
    print("'Stone,Paper,Scissors'(+10 points)")
    print("play stone paper cissors with me")
    ui = input("What you picking(st,p,si):")
    anum = random.randint(1,3)
    if ui == 'st':
            if anum == 1:
                    print("Stone!!!!")
                    print("Ahh its a draw")
            elif anum == 2:
                    print("Paper!!!!")
                    print("Yay i won so -20 points for you :|")
                    players[name]-=20
            elif anum == 3:
                    print("Scissor!!!!")
                    print("Ahh +20 points for you")
                    players[name]+=20
    if ui == 'p':
            if anum == 1:
                    print("Stone!!!!")
                    print("Ahh +20 points for you")
                    players[name]+=20
            elif anum == 2:
                    print("Paper!!!!")
                    print("Ahh its a draw")
            elif anum == 3:
                    print("Scissor!!!!")
                    print("Yay i won so -20 points for you :|")
                    players[name]-=20
    if ui == 'si':
            if anum == 1:
                    print("Stone!!!!")
                    print("Yay i won so -20 points for you :|")
                    players[name]-=20
            elif anum == 2:
                    print("Paper!!!!")
                    print("Ahh +20 points for you")
                    players[name]+=20
            elif anum == 3:
                    print("Scissor!!!!")
                    print("Ahh its a draw")
    

player()
while True:
    num = random.randint(1,9)
    for name in players:
        if num == 1:
            one(name)
        elif num == 2:
            two(name)
        elif num == 3:
            three(name)
        elif num == 4:
            four(name)
        elif num == 5:
            five(name)
        elif num == 6:
            six(name)
        elif num == 7:
            seven(name)
        elif num == 8:
            eight(name)
        elif num==9:
            print("HEY here are the scores...")
            print(players)
    
