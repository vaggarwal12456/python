from math import sin , cos , tan , log , pi

def opr(a,b,c):
    if(c == '+'):
        return a+b
    elif(c=='-'):
        return a-b
    elif(c=='*'):
        return a*b
    elif(c=='/'):
        return a/b
    elif(c=='^'):
        return a**b
    else:
        print("operator not defined")


def sci(t):

    if(t[:3]=='sin'):
        return sin(int(t[3:])*(pi/180))
    elif(t[:3]=='cos'):
        return cos(int(t[3:])*(pi/180))
    elif(t[:3]=='tan'):
        return tan(int(t[3 :])*(pi/180))
    elif(t[:3]=='log'):

        return log(int(t[3:]))
    else:
        print('error')

def check(t):
    if(t[:3]=='sin'):
        return sin(int(t[3:])*(pi/180))
    elif(t[:3]=='cos'):
        return cos(int(t[3:])*(pi/180))
    elif(t[:3]=='tan'):
        return tan(int(t[3:])*(pi/180))

    elif(t[:3]=='log'):
        return log(int(t[3:]))
    else:
        return t

#entry point
def calculate(ar):
    print(''' \nenter expression
for trignometric functition enter like sin45 etc\n''')
    ar = ar.split()

    for i in range(len(ar)):
        if(ar[i]=='minus' or ar[i]=='subtract'):
            ar[i] = '-'
        elif(ar[i]=='multiply'):
            ar[i]='*'
        elif(ar[i]=='divide'):
            ar[i]='/'
        elif(ar[i]=='plus'):
            ar[i]= '+'


    if(len(ar)<=1):
        re = sci(ar[0])
        return re

    temp = ar.copy()
    for i in range(len(ar)):
        temp[i] = check(temp[i])

    result = temp[0]

    for i in range(len(temp)//2):

        result = opr(int(result),int(temp[2*i+2]),temp[2*i+1])

    return result
    #print("\ndo you want to continue(y/n):")
    #condition = input()
