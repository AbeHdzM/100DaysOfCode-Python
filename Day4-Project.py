import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to rock, paper and scissors.")
usersChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computersChoice = random.randint(0,2)
if usersChoice == 0:
    print(f"You chose: {usersChoice}\n {rock}")
elif usersChoice == 1:
    print(f"You chose: {usersChoice}\n {paper}")
else:
    print(f"You chose: {usersChoice}\n {scissors}")

if computersChoice == 0:
    print(f"Computer chose: {computersChoice}\n {rock}")
elif computersChoice == 1:
    print(f"Computer chose: {computersChoice}\n {paper}")
else:
    print(f"Computer chose: {computersChoice}\n {scissors}")

if usersChoice == 0 and computersChoice == 2:
    print("You won!!")
elif usersChoice == 2 and computersChoice == 1:
    print("You won!!")
elif usersChoice == 1 and computersChoice == 0:
    print("You won!!")
elif usersChoice == computersChoice:
    print("It's a draw")
else:
    print("You lose")