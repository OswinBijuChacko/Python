import random as r
from oslow import *
num = r.randint(1,50)
counter=0
points=40
say("welcome to the number guessing game")
print("="*10+"\t\tNUMBER GUESSING GAME\t\t"+"="*10+"\n")
print("=> This is a number guessing game.You have to guess a number between 0 and 50\n\n => Each time you are unbale to gess the number , you will get a hint")
print("\n=>  BUT for every single hint, 10 points are deducted \n\n=>  Thus your goal is to guess the number in minimum hints")
def prime(num):
  pc=0
  for i in range(2,num//2):
      if num%i==0:
          pc+=1
  if pc==0:
      return True
  else:
      return False
      
        
        
while True:
    ask=int(input(":"))
    if ask == num:
        print("Yass Queeennn!!!");
        print("CONGRATZJULATIONS")
        print("score:"+str(points))
        break
    else:
       print("Nope")
       if counter ==1:
          points-=10
          if num%2==0:
            print("The number is even")
          elif num%2!=0:
            print("The number is odd")
       if counter ==2:
          points-=10
          if prime(num):
            print("The number is a Prime.")
          elif not prime(num):
            print("The number is not prime")
       if counter ==3:
         one = num%10
         onum=num//10
         nnum = 10*one+onum
         if nnum == num:
           print("The number is a pallindrome")
         else:
          print("the number is not a pallindrome")
       if counter ==4:
          points-=10
          if num%3==0:
            print("The number is a factor of 3.")
          if num%5==0:
            print("The number is a factor of 5")
          if num%7==0:
            print("The number is factor of 7")
          if num%3!=0:
            if num%5!=0:
              if num%7!=0:
                print("The number is not a multiple of 3 5 7")
       if counter == 5:
        #Numbers DOnt lie or do they
           points-=10
           if num%2!=0:
             one=num%10
             print("The ones digit of the number is one more than the twice of ",str((one-1)/2))
           else:
             one=num%10
             print("The ones digit of the number is twice more than the twice of ",str((one-2)/2))  
             
       if counter == 6:
          print("GAME OVER\n\n")
          print("The number was  "+str(num))
          print("Your score: "+str(points))
          break
       counter+=1
