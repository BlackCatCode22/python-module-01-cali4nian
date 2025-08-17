# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# ##### PROGRAM #####
# print('Enter Hours: ')
# hours = float(input())
# print('Enter Rate: ')
# rate = float(input())
# if hours > 40:
#     overtimeHours = hours - 40
#     overtimeRate = (rate/2) + rate
#     basePay = 40 * rate
#     overTimePay = overtimeHours * overtimeRate
#     print('Pay :' + str(basePay + overTimePay))
# else:
#     print('Pay: ' + str(hours * rate))


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

# print('Enter Hours: ')
# hours = None
# try:
#     hours = float(input())
# except:
#     print('Error, please enter numeric input')
#     exit()
#
# print('Enter Rate: ')
# rate = None
# try:
#     rate = float(input())
# except:
#     print('Error, please enter numeric input')
#     exit()
#
# if hours > 40:
#     overtimeHours = hours - 40
#     overtimeRate = (rate/2) + rate
#     basePay = 40 * rate
#     overTimePay = overtimeHours * overtimeRate
#     print('Pay :' + str(basePay + overTimePay))
# else:
#     print('Pay: ' + str(hours * rate))



# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# print('Enter grade from 0.0 to 1.0: ')
# grade = None
#
# try:
#     grade = float(input())
# except:
#     print('Bad score')
#     exit()
#
# if grade >= 0.9:
#     print('A')
# elif grade >= 0.8:
#     print('B')
# elif grade >= 0.7:
#     print('C')
# elif grade >= 0.6:
#     print('D')
# else:
#     print('F')



# Run the program repeatedly as shown above to test the various different values for input.