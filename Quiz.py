a = 0
print("Hi! I am Quiz-Bot. Initializing quiz...")
print("If there are any word answers, capitalize it.")
answer1 = input("What is 1 + 1? ")
if answer1 == "2":
    print("Correct!")
    a = a + 1
else:
    print("Wrong!")
answer2 = input("What is 1 + 4? ")
if answer2 == "5":
    print("Correct!")
    a = a + 1
else:
    print("Wrong!")
answer3 = input("What is my name? ")
if answer3 == "Quiz-Bot":
    print("Correct!")
    a = a + 1
else:
    print("Wrong!")
answer4 = input("What lanquage is this? ")
if answer4 == "Python":
    print("Correct!")
    a = a + 1
else:
    print("Wrong!")
answer5 = input("Is this a cool program? ")
if answer5 == "Yes":
    print("Correct!")
    a = a + 1
else:
    print("Wrong!")    
print ("You got", a, "/5")
if a == 5:
    print("Perfect!")
if a == 0:
    print("You're not great at this...")