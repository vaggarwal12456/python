while(1):
    a = []
    while 1:
        result =0
        a = input().split()
        print(a)
        if(a[1]=='='):
            print("invalid")
        if(a[1]=='+'):
            result = a[0] + a[2]
        elif(a[1]=='-'):
            result = a[0] - a[2]
        elif(a[1]=='*'):
            result = a[0] * a[2]
        elif(a[1]=='/'):
            result = a[0] / a[2]
        elif(a[1]=='%'):
            result = a[0] % a[2]
        elif(a[1]=='^' or a[1]=='**'):
            result = a[0] ** a[2]
        else:
            print('undefined operation, choose between +,-,*,/,%,^')

        for i in range(1,len(a)//3):
            if(a[2*i+1]=='='):
                print("result")
                break
            elif(a[2*i+1]=='+'):
                result+= a[2*i+2]
            elif(a[2*i+1]=='-'):
                result-= a[2*i+2]
            elif(a[2*i+1]=='*'):
                result*= a[2*i+2]
            elif(a[2*i+1]=='/'):
                result/= a[2*i+2]
            elif(a[2*i+1]=='%'):
                result %= a[2*i+2]
            elif(a[2*i+1]=='^' or a[2*i+1] =='**'):
                result = result**a[2*i+2]
            else:
                print('undefined operation, choose between +,-,*,/,%,^')
            print(result)
