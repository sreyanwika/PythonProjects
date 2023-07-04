'''from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key
    with open ("key,key","wb") as ky:
        ky.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)'''

import getpass
user = getpass.getuser()
password = getpass.getpass()
def add():
    id=input('enter your id/account name:')
    password=input('enter your password:')
    with open ('passy.txt','a') as p:
        p.write(id+"|"+password+"\n")
        '''fer.decrypt(passw.encode()).decode())'''
def view():
    with open ('passy.txt','r') as pt:
        for lines in pt.readlines():
            data=lines.rstrip()
            user,pswrd=data.split("|")
            print('user:'+user+',passy:'+pswrd)
            '''fer.decrypt(passw.encode()).decode())'''

            


        
while True:
    a=input('if you wanna see then please enter view ,if you wanna add then enter add,if you wanna quit then enter quit(add,view,quit):')
    if a=='quit':
        break
    elif a=='add':
        add()
    elif a=='view':
       x=input('enter the password:')
       if x==password:
             view()
    else:
        print('please enter valid input')
        continue
        
