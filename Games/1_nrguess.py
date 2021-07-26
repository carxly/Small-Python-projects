import random
print('--------------------------')
print('Welcome to the number guessing game!')
print('--------------------------')
print('You need to guess the correct number between 1-100.')
print('For that, you will have a certain amount of tries that you will be choosing yourself.')
play = True
while(play == True):
    lives = int(input('How many tries do you want for the game? '))
    win = False
    answer = random.randint(1, 100)
    print(answer)
    while(lives != 0) and (win == False):
        userGuess = int(input('Guess the number! '))
        lives = lives - 1
        if(userGuess == answer):
            print('WOW! You won! The answer really was', answer, 'and you had', lives, 'tries left!')
            win = True
        elif(answer > userGuess):
            print('The answer is bigger than your guess..')
        else:
            print('The answer is smaller than your guess..')
    playAgain = input('Do you want to play again? [y/n] ')
    if(playAgain == 'n'):
        play = False
        print('See you next time!')


