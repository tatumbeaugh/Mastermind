#Tatum Beaugh
#11/4/2021
import random

#codemaker
code= []
for i in range(4):
  num1= random.randint(0,9)
  code.append(num1)

#codebreaker:
glist = []
tries = 0

#compares lists:
def comparelist(code,glist):
  if code != glist:
   if (code[0] == glist[0]):
      print("Your first number is correct")
   else:
      print("Your first number is incorrect")
   if (code[1] == glist[1]):
      print("Your second number is correct")
   else:
      print("Your second number is incorrect")
   if (code[2] == glist[2]):
      print("Your third number is correct")
   else:
      print("Your third number is incorrect")
   if (code[3] == glist[3]):
      print("Your fourth number is correct")
   else:
      print("Your fourth number is incorrect")
  else:
    print("Correct! It took you " + str(tries) + " tries!")

#gets input and makes glist:
while glist != code:
  glist = []
  tries = tries + 1
  for i in range(4):
    guess = int(input("guess a number: "))
    glist.append(guess)
  comparelist(code, glist)