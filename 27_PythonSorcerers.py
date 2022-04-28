'''
   The Authors of this Mini Project for the CS101 Course are
   Gourang Pathak, Himanshu Gangwar and Prem Swarup
   TEAM NAME: Python Sorcerers
   TEAM ID: 27
   Implementing a Scientific calculator with following functions:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Basic expression
    6. Absolute Difference
    7. Modulo
    8. Square root
    9. Square
    10. Power
    11. Tenth power
    12. yth root of x
    13. Quadratic roots
    14. Factorial
    15. Exponential
    16. Percentage
    17. Trigonometric Functions
    18. Matrix operations
    19. Area
    20. Show History
    21. Clear History
'''

# Block Written By Gourang Pathak
import math
import circle as c          #user defined module
import square as s          #user defined module
import rectangle as r       #user defined module
import triangle as t        #user defined module

def addition():
    '''Will be used to add two numbers'''
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1 + num2)
    global result
    result = str(num1) + " + " + str(num2) + " = " + str(num1 + num2)
 
def subtract():
    '''Will be used for subtraction operation'''
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    print(num1 - num2)
    global result
    result = str(num1) + " - " + str(num2) + " = " + str(num1 - num2)
 
def absolute_difference():
    '''Will be used for absolute difference operation'''
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    if(num1>num2):
        res = (num1-num2)
    if(num1<num2):
        res = (num2-num1)
    if(num1==num2):
        res = 0
    global result
    result = "|"+str(num1) + " - " + str(num2) + "| = " + str(res)
    print(res)
 
def multiply():
    '''Will be used to multiply two numbers'''
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    res = num1*num2
    global result
    result = str(num1) + " x " + str(num2) + " = " + str(res)
    print(res)
 
def division():
    '''Will be used for the Division operation'''
    res = "Undefined"
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number to divide by : "))
    try:
        res = num1/num2
    except Exception:
        print("Can't divide by zero!")
    global result
    result = str(num1) + " / " + str(num2) + " = " + str(res)
    print(res)
 
def modulo():
    '''Will be used for the modulo (a % b) operation'''
    res = "Undefined"
    num1 = float(input("Enter dividend : "))
    num2 = float(input("Enter divisor  : "))
    try:
        res = num1%num2
    except Exception:
        print("Can't modulo with zero!")
    global result
    result = str(num1) + " % " + str(num2) + " = " + str(res)
    print(res)
 
def square_root():
    '''Will be used for the square root operation'''
    # Implemented using neton Raphson's Method
    num = float(input("Enter your number : "))
    if(num>=0):
      ans = num / 2.0 
      epsilon = .01 
      while abs(ans*ans - num) >= epsilon: 
        numr = ans**2 - num          # f(x)
        denom = 2 * ans              # f'(x)
        ans = ans - (numr / denom)   # Newton's guess
    else:
      print("Can't take squareroot of negative number! ")
      ans = "is not in the Real Number Domain"
    global result
    result = "Square root of " + str(num) + " = " + str(ans)
    print(ans)
 
def square():
    '''Will be used for the squaring operation'''
    num = float(input("Enter your number : "))
    global result
    result = str(num) + " square " +" = " + str(num**2)
    print(num**2)
 
def ten_power():
    '''Will be used to find out 10^x'''
    num = float(input("Enter your number : "))
    res = 10**num 
    global result
    result = "10 to the power "+ str(num)+" = " + str(res)
    print(res)
 
def yth_root_of_x():
    '''Will be used for finding out the yth root for the number x'''
    res = " is not possible to find out!"
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter which root you want : "))
    try:
      res = num1**(1/num2)
    except Exception:
      print("0th Root can't be found out!")
    global result
    result = str(num2) + " th root of " + str(num1) + " = " + str(res)
    print(res)
 
def quadratic_roots():
    '''Will be used for finding out the roots of a quadratic equation'''
    a = float(input("Enter a : "))
    b = float(input("Enter b : "))
    c = float(input("Enter c : "))
    if(a != 0):
        disc = b*b-4*a*c
        root_disc = math.sqrt(abs(disc))
        if(disc>0):
            res = "Roots are "+ str((-b+root_disc)/(2*a))+ " and "+ str((-b-root_disc)/(2*a)) 
        elif(disc==0):
            res = "Root is "+str(-b/(2*a))
        if(disc<0):
            res = "Roots are "+ str((-b)/(2*a))+"+ j "+ str(root_disc/(2*a))+" and "+ str((-b)/(2*a))+ " - j "+ str(root_disc/(2*a))
    else:
        print("Equation no longer Quadratic please enter non-zero a!")
        res = "Equation no longer Quadratic please enter non-zero a!"
    global result
    result = 'For '+str(a)+"x^2 + "+str(b)+'x + '+str(c)+" "+str(res)
    print(res)
 
def factorial():
    '''Will be used for the factorial operation'''
    res = "Undefined"
    try:
      num = int(input("Enter a number: "))
      if(num==0):
          res=1
      elif(num>0):
          f = 1
          for i in range(1,num+1):
              f = f*i
          res = (f)
      if(num<0):
          print("Factorial not found! ")
    except Exception:
        print("Factorial not found! ")
    global result
    result = str(num) + " ! = " + str(res)
    print(res)
 
def power():
    '''Will be used for the power (x^y) operation'''
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    res = num1**num2 
    global result
    result = str(num1) + " to the power of " + str(num2) + " = " + str(res)
    print(res)
 
def exponential():
    '''Will be used to find out e^x'''
    num = float(input("Enter a number : "))
    res = math.exp(num)
    global result
    result = " e to the power " + str(num) + " = " + str(res)
    print(res)
 
def percentage():
    '''Will be used to find out percentage of a number'''
    res = "can't find out"
    num1 = float(input("how much percent: "))
    num2 = float(input("of what number : "))
    if(num1>=0):
        res = (num1*num2)/100
    else:
        print("Enter positive value for how much percent you want!")
    global result
    result = str(num1) + " percent of " + str(num2) + " = " + str(res)
    print(res)
 
def sin():
    '''Will be used to find out sin(x)'''
    num = float(input("Enter angle in Radians "))
    res = math.sin(num)
    global result
    result = " sin of" + str(num) + " = " + str(res)
    print(res)
 
def cos():
    '''Will be used to find out cos(x)'''
    num = float(input("Enter angle in Radians "))
    res = math.cos(num)
    global result
    result = " cos of" + str(num) + " = " + str(res)
    print(res)
 
def tan():
    '''Will be used to find out tan(x)'''
    num = float(input("Enter angle in Radians "))
    res = "undefined"
    try:
        res = math.tan(num)
    except:
        print("Enter value in domain only")
    global result
    result = " tan of" + str(num) + " = " + str(res)
    print(res)
 
def arcsin():
    '''Will be used to find out arcsin(x)'''
    num = float(input("Enter number: "))
    res = "undefined"
    try:
        res = math.asin(num)
    except:
        print("Enter value in domain only")
    global result
    result = " arcsin of" + str(num) + " = " + str(res)
    print(res)
 
def arccos():
    '''Will be used to find out arccos(x)'''
    num = float(input("Enter number: "))
    res = "undefined"
    try:
        res = math.acos(num)
    except:
        print("Enter value in domain only")
    global result
    result = " arccos of" + str(num) + " = " + str(res)
    print(res)
 
def arctan():
    '''Will be used to find out arctan(x)'''
    num = float(input("Enter number: "))
    res = "undefined"
    try:
        res = math.atan(num)
    except:
        print("Enter value in domain only")
    global result
    result = " arctan of" + str(num) + " = " + str(res)
    print(res)

def sec():
    '''Will be used to find out sec(x)'''
    res = "Undefined"
    num = float(input("Enter angle in Radians "))
    try:
        res = 1/math.cos(num)
    except Exception:
        print("Can't find out")
    global result
    result = " sec of" + str(num) + " = " + str(res)
    print(res)
 
def cosec():
    '''Will be used to find out cosec(x)'''
    res = "Undefined"
    num = float(input("Enter angle in Radians "))
    try:
        res = 1/math.sin(num)
    except Exception:
        print("Can't find out")
    global result
    result = " cosec of" + str(num) + " = " + str(res)
    print(res)
 
def cot():
    res = "Undefined"
    num = float(input("Enter angle in Radians "))
    try:
        res = 1/math.tan(num)
    except Exception:
        print("Can't find out")
    global result
    result = " cot of" + str(num) + " = " + str(res)
    print(res)
 
# Block Written By Himanshu Gangwar
def matrix_add():
    # to add two matrices
    print("1st matrix")
    r1=int(input("enter no. of rows: "))
    c1=int(input("enter no. of columns: "))
    print("\n\n2nd matrix")
    r2=int(input("enter no. of rows: "))
    c2=int(input("enter no. of columns: "))
 
    
    if (r1==r2 and c1==c2):          #checking condition for addition
        print("\n\nmatrix 1 :")
        mat1=[]
        for i in range(r1):          #loop to take input for matrix 1
            temp=[]
            for j in range(c1):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat1.append(temp)
 
    
        print("\n\nmatrix 2: ")
        mat2=[]
        for i in range(r2):          #loop to take input for matrix 2
            temp=[]
            for j in range(c2):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat2.append(temp)
    
        print("\nmatrix 1 is: ")      #loop to print matrix 1
        for x1 in mat1:
            print(x1)
             
        print()
        print("\nmatrix 2 is: ")        #loop to print matrix 2
        for x1 in mat2:
            print(x1)
 
   
        print("\naddition matrix is: ")   #adding matrix 1 and matrix 2
        output=[]
        for i in range(len(mat1)):
            temp=[]
            for j in range(len(mat1[0])):
                temp.append(mat1[i][j]+mat2[i][j])
            output.append(temp)
 
        for x1 in output:                    #printing output matrices
            print(x1)
        
        global result                      #storing all the calculation in string form
        result=str(mat1)+"+"+str(mat2)+"="+str(output)
        
    else:
        print("condition for addition is not satisfied: ")
        return
    
                       
                       
'''       
   *******************
                      *********************************
                                                       *****************************
'''                                                       
 
    
def matrix_subtract():
    # to subtract two matrices
    print("1st matrix")
    r1=int(input("enter no. of rows: "))
    c1=int(input("enter no. of columns: "))
    print("\n\n2nd matrix")
    r2=int(input("enter no. of rows: "))
    c2=int(input("enter no. of columns: "))
 
    
    if (r1==r2 and c1==c2):          #checking condition for addition
        print("\n\nmatrix 1 :")
        mat1=[]
        for i in range(r1):          #loop to take input for matrix 1
            temp=[]
            for j in range(c1):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat1.append(temp)
 
    
        print("\n\nmatrix 2: ")
        mat2=[]
        for i in range(r2):          #loop to take input for matrix 2
            temp=[]
            for j in range(c2):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat2.append(temp)
    
        print("\nmatrix 1 is: ")      #loop to print matrix 1
        for x1 in mat1:
            print(x1)
             
        print()
        print("\nmatrix 2 is: ")        #loop to print matrix 2
        for x1 in mat2:
            print(x1)
 
   
        print("\nsubtraction matrix is: ")   #subtracting matrix 1 and matrix 2
        output=[]
        for i in range(len(mat1)):
            temp=[]
            for j in range(len(mat1[0])):
                temp.append(mat1[i][j]-mat2[i][j])
            output.append(temp)
 
        for x1 in output:                        #printing output matrices
            print(x1)
        
        global result                      #storing all the calculation in string form
        result=str(mat1)+"-"+str(mat2)+"="+str(output)
        
    else:
        print("condition for subtraction is not satisfied: ")
        return
 
 
 
 
'''       
   *******************
                      *********************************
                                                       *****************************
''' 
                       
 
 
def matrix_multiply():
    # to add two matrices
    print("1st matrix")
    r1=int(input("enter no. of rows: "))
    c1=int(input("enter no. of columns: "))
    print("\n\n2nd matrix")
    r2=int(input("enter no. of rows: "))
    c2=int(input("enter no. of columns: "))
 
    
    if (c1==r2):          #checking condition for multiplication
        print("\n\nmatrix 1 :")
        mat1=[]
        for i in range(r1):          #loop to take input for matrix 1
            temp=[]
            for j in range(c1):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat1.append(temp)
 
    
        print("\n\nmatrix 2: ")
        mat2=[]
        for i in range(r2):          #loop to take input for matrix 2
            temp=[]
            for j in range(c2):
                print("enter",i+1,"th"," row ",j+1,"th"," column value")
                x=int(input())
                temp.append(x)
            mat2.append(temp)
    
        print("\nmatrix 1 is: ")      #loop to print matrix 1
        for x1 in mat1:
            print(x1)
             
        print()
        print("\nmatrix 2 is: ")        #loop to print matrix 2
        for x1 in mat2:
            print(x1)
 
        output=[]                       #iniitialising values of output matrix elements as zero
        for i in range(r1):     
            temp=[]
            for j in range(c2):
                temp.append(0)
            output.append(temp)
 
                
        for i in range(r1):             #multiplying the matrices
            for j in range(c2):
                for k in range(c1):  
                    output[i][j]+=mat1[i][k]*mat2[k][j] 
 
 
        print("\nthe product of the matrices is: ")   #printing output matrices
        for x1 in output:
            print(x1)
 
        global result                      #storing all the calculation in string form
        result=str(mat1)+"*"+str(mat2)+"="+str(output)
      
        
    else:
        print("condition for multiplication is not satisfied: ")
        return



def area_circle():
    ''' for finding area of circle  '''
    
    radius=int(input("enter radius of circle :"))
    a_circle=c.area(radius)
    print("area of the circle is: ",a_circle)
    global result
    result="area of the circle with radius "+str(radius)+" is: "+str(a_circle)

def area_square():
    ''' for finding area of square '''

    side=int(input("enter side of square: "))
    a_square=s.area(side)
    print("area of square is: ",a_square)
    global result
    result="area of square with side "+str(side)+" is: "+str(a_square)

def area_rectangle():
    ''' for finding area of rectangle '''

    l=int(input("enter length of rectangle: "))
    b=int(input("enter breadth of rectangle: "))
    a_rec=r.area(l,b)
    print("area of rectangle is: ",a_rec)
    global result
    result="area of rectangle with length "+str(l)+" and breadth "+str(b)+" is: "+str(a_rec)

def area_triangle():
    ''' for finding area of triangle '''
    print("enter sides of traingle: ")
    s1=int(input("1st\n"))
    s2=int(input("2nd\n"))
    s3=int(input("3rd\n"))
    a_tri=t.area(s1,s2,s3)
    print("area of triangle is: ",a_tri)
    global result
    result="area of triangle with side1 ="+str(s1)+" ,side2 ="+str(s2)+" ,side3 ="+str(s3)+" is: "+str(a_tri)



# Block Written by Prem Swarup

import operators as op    #user defined module

symbol = {
    '+': op.summ,
    '-': op.diffrnc,
    '*': op.product,
    '/': op.divsn
}   
''' Creating a dictionary to call function 
    corresponding to the sign given by user '''
    
def compute(exprsn):
    '''This function computes the expression given by user using recursion.
    To find result using this call print(compute("expression"))'''

    
    if exprsn.isdigit():    #defining base case
         return float(exprsn)
    for i in symbol.keys():   #iterating over keys listed in dictionary in defined sequence
        x, sign, y = exprsn.partition(i)    #partitioning the expression to store value in tuple then assigning to resp. string
        if sign in symbol:  #for checking symbol in keys
            return symbol[sign](compute(x), compute(y))    #calling function corres. to the key and using recursion till strings are in float
    
         
''' to show menu and take operation type from user
user may enter index of operation or type operation in any case'''
operation = input('''Choose the operation you want to perform:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Basic expression
    6. Absolute Difference
    7. Modulo
    8. Square root
    9. Square
    10. Power
    11. Tenth power
    12. yth root of x
    13. Quadratic roots
    14. Factorial
    15. Exponential
    16. Percentage
    17. Trigonometric Functions
    18. Matrix operations
    19. Area
    20. Show History
    21. Clear History
    22. Exit
 
    ''')
operation = operation.lower()   #changing the input uniformly to lower case alphabets, to check condition easily
 
while True:
    '''calling function corresponding to the input from user'''
    try :    #handling exception of all mathematical function
        if operation == "addition" or operation == '1':  #it can match from index from menu or the name which is insensitive of case
            addition()
        elif operation == "subtraction" or operation == '2' :
            subtract()
        elif operation == "multiplication" or operation == '3' :
            multiply()
        elif operation == "division" or operation == '4' :
            division()
        elif operation == "basic expression" or operation == '5':
            expression = input("Enter the expression: ")  #taking input from user
            try:
                if expression[0] == '-' :
                    expression = '0' + expression  #inserting 0 at the start to avoid error
                print(str(compute(expression)))
                result = str(expression) + " = " + str(compute(expression))   #assigning result for history
            except:
                print("enter a valid mathematical expression using operator +,-,*,/")
                result=0
        elif operation == "absolute Difference" or operation == '6' :
            absolute_difference()
        elif operation == "modulo" or operation == '7' :
            modulo()
        elif operation == "square root" or operation == '8' :
            square_root()
        elif operation == "power" or operation == '10' :
            power()
        elif operation == "square" or operation == '9' :
            square()
        elif operation == "tenth power" or operation == '11' :
            ten_power()
        elif operation == "yth root of x" or operation == '12' :
            yth_root_of_x()
        elif operation == "quadratic roots" or operation == '13' :
            quadratic_roots()
        elif operation == "factorial" or operation == '14' :
            factorial()
        elif operation == "exponential" or operation == '15' :
            exponential()
        elif operation == "percentage" or operation == '16' :
            percentage()
        elif operation == "trigonometric Functions" or operation == '17' :
            trigo = input('''Enter trigonometric function
            i. sin
            ii. cos
            iii. tan
            iv. cosec
            v. sec
            vi. cot
            vii. arcsin
            viii. arccos
            ix. arctan
            ''')
            if trigo == "sin" or trigo == 'i' :
                sin()
            elif trigo == "cos" or trigo == 'ii' :
                cos()
            elif trigo == 'tan' or trigo == 'iii' :
                tan()
            elif trigo == 'cosec' or trigo == 'iv' :
                cosec()
            elif trigo == 'sec' or trigo == 'v' :
                cosec()
            elif trigo == 'cot' or trigo == 'vi' :
                cot()
            elif trigo == 'arcsin' or trigo == 'vii' :
                arcsin()
            elif trigo == 'arccos' or trigo == 'viii' :
                arccos()
            elif trigo == 'arctan' or trigo == 'ix' :
                arctan()
            else :
                print('Function currently unavialable!/n', 'Sorry for the inconvenience')
                result = 0
        elif operation == 'matrix operations' or operation == '18' :
            mat = input('''Enter matrix operation you want to perform:
            i. Addition 
            ii. Subtraction 
            iii. Multiplication 
            ''')
            mat = mat.lower()
            if mat == 'addition' or mat =='i' :
                matrix_add()
            elif mat == 'subtraction' or mat == 'ii' :
                matrix_subtract()
            elif mat =='multiplication' or mat == 'iii' :
                matrix_multiply()
            else :
                print("Sorry! Can't get what you want to perform")
                result = 0
        elif operation=='area' or operation=='19':
            print('''select whose area you want to find:
            i). Circle
            ii).Square
            iii).rectangle
            iv).triangle
            ''')
            ar=input()
            ar=ar.lower()
            if ar=='circle' or ar=='i':
                area_circle()
            elif ar=='square' or ar=='ii':
                area_square()
            elif ar=='rectangle' or ar=='iii':
                area_rectangle()
            elif ar=='triangle' or ar=='iv':
                area_triangle()
            else:
                print("wrong option") 
                result = 0
        elif operation == "exit" or operation == '22' :
            break     #breaking out of loop, then running program will get completed and exited
        elif operation == "show history" or operation == '#' or operation=='20' :
            History = open("calc_his.txt")    #opening history file in default read mode
            print(History.read())   # printing history
            History.close()   #closing file after task is done
            result = 0       #to avoid error assigning result as of int type
        elif operation == "clear history" or operation == "21" :
            import os                                   #in built module
            os.remove("calc_his.txt")                   #removing the file to clear the history
            History = open("calc_his.txt", "x")          #creating a new empty file
            History.close()
            result = 0                           # assigning result to int type to avoid error
        elif operation == 'menu' or operation == 'Menu' :
            print('''Choose the operation you want to perform:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Basic expression
        6. Absolute Difference
        7. Modulo
        8. Square root
        9. Square
        10. Power
        11. Tenth power
        12. yth root of x
        13. Quadratic roots
        14. Factorial
        15. Exponential
        16. Percentage
        17. Trigonometric Functions
        18. Matrix Operations
        19. Area
        20. Show History
        21. Clear History
        22. Exit
    
        ''')
            result = 0
        
        else :     #if operation demanded by user is unavailable
            print("Operation currently unavailable! Sorry for the inconvenience")
            operation = input('''Enter new operation:
    (Or enter "Menu" if you want to see men)
    ''')
            result = 0
    
        if type(result) == str :    #adding result to file only when it is of string type and avoiding 0
            History = open("calc_his.txt", mode="a")
            
            History.write(result)
            History.write('''
            ''')
            History.close()
            
            
    
    
        operation = input('''Enter new operation:
    (Or enter "Menu" if you want to see menu)
    ''')    #taking operation again for performing next calculation
        operation = operation.lower()   #lowering case of each alphabet to avoid case sensitivity
    except :    #if entered input is of type other than required 
        print("Please enter inputs in valid format.")