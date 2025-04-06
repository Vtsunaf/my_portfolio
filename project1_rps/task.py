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

user_choice= int(input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors"))
print(f"you choose {user_choice}")
computer_choice = random.randint(0,2)

if user_choice == 0:
    print(f"You chose: \n{rock}")
    if computer_choice == 1:
        print(f"computer chose: \n{paper}")
        print("you lose!!")
    elif computer_choice== 2:
        print(f"computer chose: \n{scissors}")
        print("you win!!")
    else:
        print(f"computer chose: \n{rock}")
        print("draw")
elif user_choice == 1:
    print(f"You chose: \n{paper}")
    if computer_choice == 1:
        print(f"computer chose: \n{scissors}")
        print("you lose!!")
    elif computer_choice== 2:
        print(f"computer chose: \n{rock}")
        print("you win!!")
    else:
        print(f"computer chose: \n{paper}")
        print("draw")
elif user_choice == 2:
    print(f"You chose: \n{scissors}")
    if computer_choice == 1:
        print(f"computer chose: \n{rock}")
        print("you lose!!")
    elif computer_choice == 2:
        print(f"computer chose: \n{paper}")
        print("you win!!")
    else:
        print(f"computer chose: \n{scissors}")
        print("draw")
else:
   print("you chose a invalid number. You lose!")
