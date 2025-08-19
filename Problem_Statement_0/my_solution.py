import math
print('====================')
print('+-?* CALCULATOR *?-+')
print('====================')
num1=int(input('enter number 1:'))
num2=int(input('enter number 2:'))
arthematic_operator=input('enter your logical operator:')


if arthematic_operator =='+':
    print(num1+num2)
elif arthematic_operator =='*':
    print(num1*num2)
elif arthematic_operator=='-':
    print(num1-num2)
elif arthematic_operator=='/':
    print(num1/num2)
elif arthematic_operator=='%':
    print(num1%num2)
elif arthematic_operator=='sqrt':
    
    choice=int(input('enter which number you would like to find the square root of(1/2)'))
    if choice==1:
        print(math.sqrt(num1))
    elif choice==2:
        print(math.sqrt(num2))

elif arthematic_operator=='**':
    choice2=int(input('enter which number you want to find the power of'))
    power=int(input('enter the power to which you want it to be raised'))
    if choice2==1:
        print(num1**power)
    if choice2==2:
        print(num2**power)    
else:
    print('invalid input')
