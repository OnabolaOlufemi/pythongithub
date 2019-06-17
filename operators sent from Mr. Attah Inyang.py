# #PYTHON OPERATORS
# # + ---> ADDITION
# # - ---> SUBTRACTION
# # / ---> DIVISION
# # * ---> MULTIPLICATION
# # % ---> MODULUS
# # ** ---> EXPONENT


# X = 5%3 #modulus RETURNS 2 REMAINDER AFTER DIVISION
# print(X)

# X = 5/3 #NORMAL DIVISION RETURNS A FLOAT WITH DECIMAL VALUES
# print("NORMAL DIVISION :", X)

# X = 5//3 #FLOOR DIVISION RETURNS A INTEGER ROUNDED DOWN
# print("FLOOR DIVISION :", X)

# X = 5 ** 3 #EXPONENT RAISES TO POWER
# print("EXPONENT OPERATION :", X)

# #ASSIGNMENT OPERATORS     
# # = ---> BASIC ASSIGNMENT
# # += ---> ADDITION & ASSIGN
# # -= ---> SUBTRACTION & ASSIGN
# # *= ---> MULTIPLICATION & ASSIGN

# print("\nAT BASIC ASSIGNMENT\n")
# APPLES = 6 # BASIC ASSIGNMENT, ASSIGN VARIABLES
# print("APPLES : ", APPLES)

# print("AT subtract and ASSIGNMENT\n\n".upper())
    
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES -= 1 # SUBTRACTION & ASSIGN VARIABLES
# print("APPLES : ", APPLES)


# print("\n\nAT add and ASSIGNMENT\n\n".upper())

# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES += 1 # ADD & ASSIGN VARIABLES
# print("APPLES : ", APPLES)

# print("\n\nAT multiply and ASSIGNMENT\n\n".upper())

# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# APPLES *= 2 # MULTIPLY  & ASSIGN VARIABLES
# print("APPLES : ", APPLES)
# import datetime

# current_age = int(input("Please enter your current age : "))
# name = input("Please enter your name : ") 

# current_date = datetime.datetime.now()
# current_year = current_date.year

# target_age = 100

# target_year = target_age - current_age + current_year

# print(f"Hello {name} you are currently {current_age} and will turn 100 in {target_year}.\nBye..!!!")



# current_age = int(input("Please enter your current age : "))
# name = input("Please enter your name : ") 
# number_of_prints = int(input("Please enter your number of times to print : "))

# current_year = 2019

# target_age = 100

# target_year = target_age - current_age + current_year
# text = (f"Hello {name} you are currently {current_age} and will turn 100 in {target_year}.\n\n")

# text_multiple_print = text * number_of_prints

# print(text_multiple_print)

# num1 = int(input("please enter the first num : "))
# num2 = int(input("please enter the second num : "))

# print(num1 + num2)


question = input("Please enter the question in  this format (a + b) : ")
broken_down_question = question.split()
num1 = int(broken_down_question[0])
num2 = int(broken_down_question[2])
operator = broken_down_question[1]

# print(question)
# print(broken_down_question)
# print(num1+num2)
if operator == "+":
    print("\nAddition..!!!\n")
    print(num1+num2)
elif operator == "-":
    print("\nSubtraction..!!!\n")
    print(num1-num2)
elif operator == "*":
    print("\nMultiplication..!!!\n")
    print(num1*num2)
elif operator == "/":
    print("\nDivision..!!!\n")
    print(num1/num2)
else:
    print("UNKNOWN OPERATOR...!!!")