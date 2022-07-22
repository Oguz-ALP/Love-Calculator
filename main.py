print("Welcome to the Oguz's Love Calculator!")
name1 = input("What is your full name? \n") .lower()
name2 = input("Who is the lucky one? \n") .lower()

name = name1 + name2

T = name .count("t")
R = name .count("r")
U = name .count("u")
E1 = name .count("e")
L = name .count("l")
O = name .count("o")
V = name .count("v")
E2 = name .count("e")


TRUE = (T + R + U + E1)
LOVE = (L + O + V + E2)

result = str(TRUE) + str(LOVE)

if TRUE >= 7 and TRUE < 10:
  print("Your score is " + result + '% I think she might be the one dude')
elif TRUE >= 4 and TRUE < 7:
  print("Your score is " + result + "% lets slow things down a little bit")
elif TRUE >= 0 and TRUE < 4:
  print("Your score is " + result + "% she better have the best boo... I mean eyes")
else:
  print("Your score is " + result + "% Where is my wedding invitation")
