# day3: I learnt about control flow using if elif else and multiple and nested if else statements. 

# I also learnt how to use logical operators in Python and inbuilt string functions, i.e string manipulation

# Today's project is Treasure Island:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


#Additional questions:
  
 # Odd or Even checker:
num = int(input())

if num%2==0 :
  print("Even number")

else:
  print("Odd number")

#Leap year checker:
  

year = int(input())

if year%100==0:
  if year%400==0:
    print("Leap year")
  else:
    print("Not leap year")

else:
  if(year%4==0):
    print("Leap year")
  else:
    print("Not leap year")

#Love calculator:

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name1=name1.lower()
name2=name2.lower()

c1=name1.count("l")+name2.count("l")
c2=name1.count("o")+name2.count("o")
c3=name1.count("v")+name2.count("v")
c4=name1.count("e")+name2.count("e")

d1=name1.count("t")+name2.count("t")
d2=name1.count("r")+name2.count("r")
d3=name1.count("u")+name2.count("u")
d4=name1.count("e")+name2.count("e")

c=c1+c2+c3+c4
d=d1+d2+d3+d4

res=d*10+c

if res<10 or res>90:
  print(f"Your score is {res}, you go together like coke and mentos.")
elif res>=40 and res<=50:
  print(f"Your score is {res}, you are alright together.")
else:
  print(f"Your score is {res}.")



  
  
   

