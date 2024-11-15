print("Welcome To My Quiz")

play=input('Do you want to play? ')
if play.lower() != "yes":
    quit()
print("Lets play!")
score=0
answer= input('what is the capital of india? ')
if answer.lower()== 'delhi':
    print('correct!')
    score+=1
else:
    print('incorrect!') 
answer= input('who is the captain of india male cricket team ')
if answer.lower()== 'rohit sharma':
    print('correct!')
    score+=1
else:
    print('incorrect!') 
answer= input('where is qutub minar located? ')
if answer.lower()== 'delhi':
    print('correct!')
    score+=1
else:
    print('incorrect!') 
answer= input('who is the pm of india? ')
if answer.lower()== 'narendra modi':
    print('correct!')
    score+=1
else:
    print('incorrect!')
print('you got '+ str(score) + " question correct!")
print('you got '+ str((score/4)*100) + "%")


    

   
