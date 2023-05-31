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
import random

rpslist = [rock, paper, scissors]

userschoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
userschoicee = rpslist[userschoice]

computerschoice =  random.randint(0, 2)
computerschoicee = rpslist[computerschoice]

print(userschoicee)
print("Computer chose:")
print(computerschoicee)

if userschoice == 0 and computerschoice == 0:
  print("It's a draw")
elif userschoice == 1 and computerschoice == 0:
  print("You win")
elif userschoice == 2 and computerschoice == 0:
  print("You lose")
elif computerschoice == 1 and userschoice == 0:
  print("You lose")
elif computerschoice == 2 and userschoice == 0:
  print("You win")
elif userschoice == 1 and computerschoice == 1:
  print("It's a draw")
elif userschoice == 2 and computerschoice == 1:
  print("You win")
elif computerschoice == 2 and userschoice == 1:
  print("You lose")
elif userschoice == 2 and computerschoice == 2:
  print("It's a draw")

#Day 4
#Rock-Paper-Scissors
#100DaysOfCode
#Angela Yu
#Joseph Adoga