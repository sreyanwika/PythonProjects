from tkinter.messagebox import YES


print('hey guys!!please read the follow instructions, to play quyiz...and have fun')
print('there will be 5 set of questions ,\n each question carries 2 marks \nif you answer incorrectly there will be 1 negative mark, if you dont know answer then skip ')
print('shall we satrt playing??')
x=input('enter yes or no:')
print(x)
if x=='no':
    quit()
count=0
print('here it goes your first question')
print('which country has the highest population?')
answer=input('enter the answer:')
if answer=='china':
    print('correct!!! hurrrey')
    count+=1
elif answer!='china' or 'skip':
    count-=1
print('what is full form of html?')
answer=input('enter the answer:')
if answer=='hypertext markup language':
    print('correct!!! hurrrey')
    count+=1
elif answer!='hypertext markup language' or 'skip':
    count-=1
print('what is the toughest exam in the world?' )
answer=input('enter the answer:')
if answer=='iit' or 'upsc' or 'gre':
    print('correct!!! hurrrey')
    count+=1
elif answer!='iit' or 'upsc' or  'gre' or 'skip':
    count-=1
print('What flies without wings?')
answer=input('enter the answer:')
if answer=='time':
    print('correct!!! hurrrey')
    count+=1
elif answer!='time' or  'skip':
    count-=1
print('Which word in the dictionary is spelled incorrectly?')
answer=input('enter the answer:')
if answer=='incorrectly':
    print('correct!!! hurrrey')
    count+=1
elif answer!='incorrectly' or 'skip':
    count-=1
print('the points you scored are:',count)
print('you answered'+str(count)+'questions correctly')