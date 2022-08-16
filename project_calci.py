l = []
while True:
    print("*"*50)
    
    print("Welcome to calculator project")
    print("*"*50)
    print()
    print('''
                     Menu
                          1. + for Addition
                          2. - for subtraction
                          3. * for multiplcation
                          4. / for Division
                          5. ** for Exponsite
                          ''')
    print()
    choice = input("Enter your choice operator:")
    num1 = eval(input("Enter your first number:"))
    num2  = eval(input("Enter your second number:"))
    if choice == '+':
        t = num1,choice,num2,num1+num2
        l.append(t)
        print("Addition of",num1,'and',num2, 'is', num1 + num2)
        
    elif choice =='-':
        t = num1,choice,num2,num1-num2
        l.append(t)
        print("Subtraction of",num1,'and',num2, ' is', num1 - num2)
    elif choice =='*':
        t = num1,choice,num2,num1*num2
        l.append(t)
        print("Multiplication of",num1,'and',num2, 'is', num1 * num2)
    elif choice =='/':
        t = num1,choice,num2,num1/num2
        l.append(t)
        print("Division of",num1,'and',num2, 'is', num1 / num2)
    elif choice == '**':
        t = num1,choice,num2,num1**num2
        l.append(t)
        print("Exponsite of",num1,'and',num2, 'is', num1 ** num2)
    else:
        print("Invaild Choice.pls try agian")
    print('--'*50)
    
    ch = input("Do you want to continue y/n:") # Y/N
    ch = ch.lower()
    
    if ch != 'y':
        print("Your last operations ")
        for i in l:
            print(i)
        break
     