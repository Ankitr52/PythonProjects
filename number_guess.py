import random
top_of_range=input("type a number :")
if top_of_range.isdigit():
    top_of_range= int(top_of_range)

    if top_of_range<=0:
        print('Enter a number larger than 0:')
        quit()
else:
    print('Please Enter a number next time:')
    quit()

random_number=random.randrange(0,top_of_range)
guesses=0
while True:
    guesses+=1
    
    user_input= input('Enter a number:')
    if user_input.isdigit():
        user_input= int(user_input)
    else:
        print('Enter a number next time:')
        continue

    if user_input==random_number:
         print('you got it!')
         break
    elif user_input>random_number:
            print('you were above the number!')
    else:
            print('you were below the number!')

print('you got it',guesses,'guesses')
        
