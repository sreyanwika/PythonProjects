print('welcome to palace adventure..r u ready to statrt!!')
print('if you are ready for adventure please say yes/no')
x=input('enter:')
if (x=='yes'):
    print('here you go choose right path to reach palace')
    print('please enter in which direction you wanna start your journey(left/right/straight)')
    x=input('enter:')
    if (x=='left'):
        print('you reached towards the river you wanna swim or you will wait for the boat which comes at 7 pm(swim,boat)')
        x=input('enter:')
        if(x=='swim'):
            print('oops there z crocodile....')
            print('heyy stop!!! i wont allow you to move anywhere until you answer my question?? ')
            print('here it goes your question in sun and moon which is bigg??')
            x=input('enter(sun/moon):')
            if(x=='moon'):
                print('you are right, you can go ahead')
                x=input('enter(left/right):')
                if(x=='right'):
                    print('the road is covered mud holeee!!answer to the question and get shoes to cross the numd hole')
                    print('what is the the mistake in a,b,c,d...')
                    x=input('enter(the/b):')
                    if(x=='the'):
                        print('you are right')
                        print('you reached night stay home it is already dark stay here for night again start your journey morning')
                        print('heyy good morning,its time to wake up and start your journey')
                        x=input('enter(left/right):')
                        if(x=='left'):
                            print('congratsss you reached palaceee')
                            quit()
                        else:
                            quit()
                    else:
                        print('sorry you are wron you didnt win shoes sorry....')
                        quit()
                else:
                    print('your journey ends here...')
                    quit()
            else:
                print('you are wrongg!! i m gonna eat you')
                quit()
        else:
            print('here your both arrives')
            print('oopsss something went wrong with the boat boat is about to sink!!')
            print('you are dead')
            quit()     
    elif(x=='right'):
        print('heyyy you reached towards hanging ladder,its halfbroken you wanna continue or wait until it got repaired')
        x=input('enter(continue/repair):')
        if x=='continue':
            print('oops u fell down!!')
            quit()
        elif('repair'):
            print('finally you crossed the bridge ladder')
            x=input('enter(left/right):')
            if x=='left':
                print('dead end')
                quit()
            else:
                print('you reached to hill area...')
                x=input('enter(left/right):')
                if x=='left':
                    print('you reached night stay home it is already dark stay here for night again start your journey morning')
                    print('heyy good morning,its time to wake up and start your journey')
                    x=input('enter(left/right):')
                    if(x=='right'):
                            print('congratsss you reached palaceee')
                            quit()
                    else:
                            quit()
                else:
                    print('game overr!!')   
             
    elif(x=='straight'):
        print('you reached towards the forest.....it is almost eve sun is moving from east to west...')
        x=input('enter(left/right):')
        if x=='left':
            print('you reached night stay home it is already dark stay here for night again start your journey morning')
            print('heyy good morning,its time to wake up and start your journey')
            x=input('enter(left/right):')
            if(x=='right'):
                            print('congratsss you reached palaceee')
                            quit()
            else:
                            quit()
        else:
            print('dead end')
            quit()

else:
    quit()