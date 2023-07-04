#user input
#checking whether user input is digit or not if it is, storing in a variable as a random limit
#checking whether guess num is digit or not...
#checking number and guess num are equal or not....
import random
guesses=0
top=input('enter a  num:')
if top.isdigit():
    top=int(top)
else:
    print('enter valid input')
number=random.randint(0,top)
while True:
    guesses+=1
    guess_num=input('enter a num:')

    if guess_num.isdigit():
      guess_num=int(guess_num)
    else:
       print('enter valid input')
       continue
    if number==guess_num:
       print('you guessed it correctlyy')

       break
    else:
      print('please try again!!')
      continue
    
print('no of times u guessed:',guesses)