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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


#game = ["rock", "paper", "scissor"]
#computer = random.choice(game)

game_images = [rock, paper, scissor]

user = int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissor.\n"))
print(game_images[user])

# 0, 1, 2

computer = random.randint(0,2)
print(f"The computer chose")
print(game_images[computer])

if user == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user == 2: 
    print("You lose!")
elif user >=3 or user<0 :
    print("You typed an invalid number. You lose!")
elif computer > user: 
    print("You lose!") 
elif computer < user: 
    print("You win!")
elif computer == user: 
    print("It's a tie. Try again!")


## rock (0), paper(1), scissor (2)
## 0 wins 2 
## 1 wins 0 
## 2 wins 1
## 0 losses 1
## 1 losses 2
## 2 losses 0