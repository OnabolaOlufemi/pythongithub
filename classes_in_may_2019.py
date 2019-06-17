# print("20/2*3 is ")
# print(20/2*3)                                                                                                                     

a = 20 + 30
print(a)
a = 20 + 30
# print("In 30 years Ada will be", a)
# This is an error 
# print("In 30 years Ada will be".format(a)) 
# This is correct 
# print('In 30 years Ada will be {}'.format(a))  


# MONDAY May 20th Class
# greeting = "Hello"
# name = "Brian"
# print(greeting,name,".")
# print(greeting+name+".")
# print(greeting + name +".")
# sentence_1 = greeting + name +"."
# print(sentence_1)
# sentence_2 = greeting + " " + name + "."
# print(sentence_2)

# relationship = "friends"
# original_price = 30000
# name = "Femi"
# discount = 0.15
# report = ("Hello " + name + "," + " because we are " + relationship + "," + " I will drop the price from " + str(original_price) + " to " + str(original_price*discount) + " at a discount of " + str(discount*100) + "%")
# print(report)

# Wednesday 22nd May, 2019
# PYTHON OPERATORS
# Perimeter of Square
# length = 9
# # perimeter_of_square = 4* length
# # print(perimeter_of_square)
# # print("The perimeter of the square is :",perimeter_of_square)
# breadth = 7
# # perimeter1_of_rectangle = length + breadth + length + breadth
# # print(perimeter1_of_rectangle)
# # perimeter2_of_rectangle = 2*length + 2*breadth
# # print(perimeter2_of_rectangle)
# perimeter3_of_rectangle = 2 *(length + breadth)
# print(perimeter3_of_rectangle)
# print("The perimeter of the rectangle is :",perimeter3_of_rectangle)

# value = 105
# if value % 2 is 0 :
#     print(value, ": is an even number,")
# else:
#     print(value, ": is not an even number,")

# STILL ON PYTHON OPERATORS: TO GET IMPUT FROM THE USER

# first_name = input("Hello what is your name :")
# print("Hi your name is ", first_name)

# length = input("Please enter the length of square : ")
# area_of_square = length**2
# print("The area_of_square is : ", area_of_square)


# length = input("Please enter the length of square : ")
# length = int(length)
# area_of_square = length**2
# print("The area of the square is : ", area_of_square)

# MORE ON GETTING IMPUT FROM THE USER: PYTHAGORAS THEOREM
# With a given right-angled triangle;
# opposite = input("Please enter the value of the opposite : ")
# adjacent = input("Please enter the value of the adjacent : ")
# opposite = int(opposite)
# adjacent = int(adjacent)
# sum_of_squares = opposite**2 + adjacent**2
# hypotenuse = sum_of_squares**0.5
# print("The hypotenuse of the triangle is : ", hypotenuse)

# opposite = int(input("Please enter the value of the opposite : "))
# adjacent = int(input("Please enter the value of the adjacent : "))
# sum_of_squares = opposite**2 + adjacent**2
# hypotenuse = sum_of_squares**0.5
# print("The hypotenuse of the triangle is : ", hypotenuse)

# opposite = int(input("Please enter the value of the opposite : "))
# adjacent = int(input("Please enter the value of the adjacent : "))
# hypotenuse = (opposite**2 + adjacent**2)**0.5
# print("The hypotenuse of the triangle is : ", hypotenuse) 
# 
# ASSIGNMENT AS AT MAY 27TH 2019 
# TO WRITE A PROGRAM WHICH TELLS IF A NUMBER IS DIVISIBLE BY 15 OR NOT
# value = 105
# if value % 15 is 0 :
#     print(value, ": is divisible by 15,")
# else:
#     print(value, ": is not divisible by 15,")   
#
                                                                                                                                                                                                                                                                                                                                                                                                                                 



# SATURDAY ASSIGNMENT A 
# import datetime 

# name = input("what is your name ")
# current_age = int(input("how old are you now : "))
# current_date = datetime.datetime.now()
# current_year = current_date.year
# target_age = 100
# target_year = target_age - current_age + current_year s
# print(f"Hello {name} you are currently {current_age} and will turn 100 in {target_year}.\nBye..!!")

# name = input("what is your name ")
# current_age = int(input("how old are you now : "))
# n_times = int(input("enter the number of times : "))
# current_year = 2019
# target_age = 100
# target_year = target_age - current_age + current_year
# print(f"Hello {name} you are currently {current_age} and will turn 100 in {target_year}.\nBye..!!")
# text = (f"Hello {name} you are currently {current_age} and will turn 100 in {target_year}.\nBye..!!")
# text_multiple_prints = text * n_times
# print(text_multiple_prints)

# SATURDAY ASSIGNMENT C
# real_name = input("write your name : ")
# repeated_name = (real_name * 1000)
# print(repeated_name)


# TAKE AWAY ASSINGMENT FROM MAY 2019

num_1 = int(input("please write any num_1 : "))
num_2 = int(input("please write any num_2 : "))
den_1 = int(input("please write any den_1 : "))
den_2 = int(input("please write any den_2 : "))
value_1 = strnum_1*den_2 + num_2*den_1
value_2 = den_1 * den_2
answer = value_1/value_2
print(answer)




