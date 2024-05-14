# --- Python Tutorial - Python Full Course for Beginners - https://www.youtube.com/watch?v=_uQrJ0TkZlc ---

# 00:01:52 - DOWNLOAD LATEST FROM python.org, I'M NOT DOWNLOADING THE Pycharm ide, TO RUN CREATE A .py FILE AND DO    python3 <path-to-.py-file>


# 00:06:13 - PRINTING STRINGS WITH print, EXPRESSIONS MULTIPLYING STRINGS
#
# print("Mosh Hamedani")
# print('o----')
# print(' ||||')
# print('*' * 10)


# 00:13:06 - VARIABLES, STRINGS, INTEGERS, FLOATS, BOOLEANS, CASE SENSITIVITY, Python UNDERSCORE NAMING CONVENTION
#
# price = 10
# price = 20
# rating = 4.9
#
# name = 'John Smith'
# age = 40
# new_patient = True


# 00:18:24 - EXERCISE, input, CONCATENATION
#
# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)


# 00:22:50 - USING int AND float, TYPE CONVERSIONS, GETTING TYPE OF WITH type METHOD
#
# birth_year = input('Birth year: ')
# age = 2024 - int(birth_year)
# print(age)
# print(type(birth_year))
# print(type(age))


# 00:28:06 - EXERCISE 
#
# weight_lbs = input('Weight (lbs): ')
# weight_kg = float(weight_lbs) * .45
# print(weight_kg)


# 00:29:35 - NESTED STRINGS, STRING INDICES, INDEX DEFAULTS, SQUARE BRACKET SYNTAX, MULTILINE STRINGS WITH TRIPLE QUOTES
#
# course = 'Python for "Beginners"'
# print(course)
# print(course[0])
# print(course[-1])
# print(course[-10])
# print(course[1:4])
# print(course[:4])
# print(course[:])
# print(course[1:-1])
#
# letter = '''
# Dear Guy
#
# Just saying hi
#
# Yours truly,
# Other Guy
# '''
# print(letter)


# 00:37:40 - UNFORMATTED VS FORMATTED STRINGS
#
# first = 'John'
# last = 'Smith'
# message_unformatted_string = first + ' [' + last + '] is a coder'
# print(message_unformatted_string)
# message_formatted_string = f'{first} [{last}] is a coder'
# print(message_formatted_string)


# 00:40:55 - USING STRING METHODS len, upper, lower, find, replace, in
#
# course = 'Python for "Beginners"'
# print(len(course))
# print(course.lower())
# print(course.upper())
# print(course.find('o'))
# print(course.replace('"Beginners"', '(not really) "Beginners"'))
# print(course.replace('P', 'J'))
# print('python' in course)
# print('Python' in course)


# 00:48:38 - ARITHMETIC OPERATORS, OPERATOR PRECEDENCE (PARENTHESIS, EXPONENTIATION, MULTIPLICATION OR DIVISION, ADDITION OR SUBTRACTION), AUGMENTED ASSIGNMENT OPERATOR
#
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)
# x = 10
# x = x + 3
# x += 3
# print(x)


# 00:54:21 - EXERCISE
#
# x = (2 + 3) * 10 - 3
# print(x) #should equal 47


# 00:55:10 - math functions AND SOMETIMES importing THE math (object) module (https://docs.python.org/3/library/math.html)
#
# x = -2.9
# print(round(x))
# print(abs(x))
# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))


# 00:58:24 - CONDITIONAL STATEMENTS, INDENTS
#
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")


# 01:05:02 - EXERCISE
#
# price = 1000000
# good_credit = False
#
# if good_credit:
#     downpayment = price * .1
# else:
#     downpayment = price * .2
#
# print(f"Downpayment is {downpayment}")


# 01:06:38 - LOGICAL OPERATORS
#
# has_high_income = True
# has_high_credit = False
# has_criminal_record = False
#
# if (has_high_income and has_high_credit) and not has_criminal_record:
#     print("Very eligible for loan")
#
# if (has_high_income or has_high_credit) and not has_criminal_record:
#     print("Eligible for loan")


# 01:11:31 - COMPARISON OPERATORS
#
# temperature = 25
#
# if temperature > 30:
#     print("It's a hot day")
# else:
#     if temperature == 30:
#         print("It's actually right on the cusp of being a hot day")
#     elif temperature != 25:
#         print("It's not 25 degrees but it's still hot")
#     else:
#         print("It's not a hot day, it's only 25 degrees")


# 01:14:04 - EXERCISE
#
# name = 'Jak'
#
# if len(name) < 3:
#     print("Name must be at least 3 chars")
# elif len(name) > 50:
#     print("Name must be no more than 50 chars")
# else:
#     print(f"Name is good, it's {name}")


# 01:16:25 - EXERCISE
#
# weight = int(input('Weight: '))
# unit = (input('(L)bs or (K)g: ')).lower()
#
# if unit == 'l':
#     converted_weight = weight * .45
#     new_unit = 'kilograms'
# else:
#      converted_weight = weight * 2.22222
#      new_unit = 'pounds'
#
# print(f'You are {converted_weight} {new_unit}')


# 01:20:50 - WHILE LOOPS, BREAKS AND ELSES ON WHILE LOOPS
#
# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")


# 01:24:15 - GUESSING GAME
#
# secret_number = 9
# guesses = 0
#
# while guesses < 3:
#     guess = int(input('What do you guess? '))
#     guesses +=1
#     if guess == secret_number:
#         print(f'You guessed it! Yes the secret number is {secret_number}')
#         break
#     elif guesses < 3:
#         print('Try again')    
# else:
#     print(f'Oh no, you didn\'t guess it! It was {secret_number}')


# 01:31:00 - CAR GAME
#
# entry = input('>')
# if entry != 'quit':
#     if entry == 'help':
#         response = '''start - to start the car
# stop - to stop the car
# quit - to exit'''
#     elif entry == 'start':
#         response = 'Car started...Ready to go!'
#     elif entry == 'stop':
#         response = 'Car stopped.'
#     else:
#         response = 'I don\'t understand that...'
#     print(response)
#
#
# entry = ''
# has_started = False
#
# while True:
#     entry = input('> ').lower()
#     if entry == 'start':
#         if not has_started:
#             has_started = True
#             print('Car started')
#         else:
#             print('Car has already started')
#     elif entry == 'stop':
#         if not has_started:
#             print('Car has already stopped')
#         else:
#             print('Car stopped.')
#     elif entry == 'help':
#         print('''start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif entry == 'quit':
#         break
#     else:
#         print('Sorry I don\'t understand')


# 01:41:55 - FOR LOOPS, ITEM DEFAULTS IN STRINGS, LISTS, RANGE FUNCTION/STEPS (WHICH MUST BE INTEGERS), 
#
# prices = [10,20,30]
# price = 0
# for i in prices:
#     price += i
# print(f'Total price is {price}')


# 01:47:54 -  #NESTED FOR LOOPS
#
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# 01:51:32 - EXERCISE
#
# numbersF = [5,2,5,2,2]
# for i in numbers:
#     print('x' * i)
#
# line = ''
# numbersF = [5,2,5,2,2]
# numbersL = [1,1,1,1,4]
# for i in numbersL:
#     for j in range(i):
#         line += 'x'
#     print(line)
#     line = ''


# 01:56:00 - LISTS (SAME AS arrays IN JAVASCRIPT)
#
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
#
# print(names[2])
# print(names[-1])
# print(names[1:3])
# print(names[:2])
# print(names[2:])
# print(names[-2:])
# print(names[-2:][0])
# print(names[-2:][0][1])
#
# names[0] = 'Jon'
# print(names[0])


# 01:59:38 - EXERCISE
#
# nums = [34,67,23,897,854,35]
# largest_cached = nums[0]
#
# for num in nums:
#     if num > largest_cached:
#         largest_cached = num
# print(largest_cached)


# 02:01:54 - 2D LISTS
#
# matrix = [
#     [4,5,6],
#     [1,2,3],
#     [7,8,9]
# ]
#
# print(matrix[2][1])
#
# matrix[2][1] = 20
# print(matrix[2][1])
#
# for row in matrix:
#     for i in row:
#         print(i)


# 02:06:09 - LIST METHODS, append, insert, remove, clear, pop, index, in, count, sort, reverse, copy
#
# matrix.append([10,11,12])
# print(matrix)
# print(matrix[3][2])
#
# matrix.insert(2,[6.25,6.5,6.75])
# print(matrix)
#
# matrix.remove(matrix[3])
# print(matrix)
#
# matrix.sort()
# print(matrix)
#
# matrix.reverse()
# print(matrix)
#
# matrix2 = matrix.copy()
#
# matrix.clear()
# print(matrix)
# print(matrix2)



# 02:06:09 - EXERCISE
#
# nums = [2,2,4,6,3,4,6,1]
# nums2 = []
#
# for num in nums:
#     if num not in nums2:
#         nums2.append(num)
#
# print(nums2)


# 02:13:35 - TUPLES (BASICALLY IMMUTABLE LISTS)
#
# numbers = (1,2,3)
# print(numbers[0])


# 02:15:42 - UNPACKING TUPLES OR LISTS (SAME AS destructuring assignment IN JAVASCRIPT)
#
# coordinates = (1,2,3)
#
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# print(x,y,z)
# x = 0
# y = 0
# z = 0
# x,y,z = coordinates
# print(x,y,z)


# 02:18:33 - DICTIONARIES (SAME AS objects IN JAVASCRIPT) AND None (I believe same as undefined and/or null in JavaScript)
#
# customer = { #If keys are strings they must be in quotes...
#     'name': 'John Smith',
#     'age': 30,
#     'is_verified': True,
#     3: 3, #...but you can actually have int keys...
#     2.4: 2.4, #...and float keys
# }
#
# print(customer)
# print(customer.get('name'))
# print(customer.get('height')) #Returns None
# print(customer.get('height', 6.0)) #But can add a default if get returns None
#
# customer['name'] = 'Jack Smith'
# print(customer)
#
# customer['birthday'] = '2000, 04-02nd'
# print(customer)


# 02:23:30 - EXERCISE
#
# numbersDict = {
#     1: 'One',
#     2: 'Two',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five',
#     6: 'Six',
#     7: 'Seven',
#     8: 'Eight',
#     9: 'Nine'
# }
# spelledDict = ''
# entry = input('Enter your digits: ')
#
# for digit in entry:
#     spelledDict += f'{numbersDict.get(int(digit), '!')} '
#
# print(spelledDict)


# 02:26:32 - EXERCISE
#
# emoji_dict = {
#     ':)': '🙂',
#     ':(': '🙁'
# }
#
# message = input('Input message: ')
# individual_words = message.split(' ')
# udpated_message = ''
#
# for word in individual_words:
#     udpated_message += f'{emoji_dict.get(word, word)} '
#
# print(udpated_message)


# 02:30:42 - FUNCTIONS, ARGUMENTS VS PARAMETERS, POSITIONAL ARGUMENTS, KEYWORD ARGUMENTS, return STATEMENT, BY DEFAULT ALL FUNCTIONS return None
#
# def greet_user(first_name, middle_initial, last_name):
#     print(f'Hi {first_name} {middle_initial} {last_name} (from function)')
#     print(f'Hope you\'re doing well, {first_name} (from same function)')
#
# # greet_user('John', 'Smith')
# # greet_user('Mary', 'Jane')
#
# greet_user('John', last_name = 'Smith', middle_initial = 'E')


# 02:49:25 - EXERCISE
#
# def convert_emoji(str):
#     new_str = ''
#     emoji_dict = {
#         ':)': '🙂',
#         ':(': '🙁'
#     }
#     tokens = str.split(' ')
#     for token in tokens:
#         new_str += f'{emoji_dict.get(token, token)} '
#     return new_str

# message = input('Input a message: ')
# print(convert_emoji(message))


# 02:53:54 - EXCEPTIONS, ValueError, ZeroDivisionError, try-except BLOCKS
#
# try: 
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(risk)
# except ZeroDivisionError:
#     print('Can\'t divide by zero')
# except ValueError:
#     print('Invalid value')


# 02:59:27 - COMMENTS
#
#Use Command+forward slash or simply # to comment out a line


# 03:01:58 - classes, points, types, Pascal NAMING CONVENTION, AN object IS AN INSTANCES OF A class, A class DEFINES THE BLUEPRINT OR TEMPLATE OF CREATING objects (OR class INSTANCES), classes HAVE methods AND attributes
#
# class Point:
#     def move():
#         print('move')
#     def draw():
#         print('draw')
#
# point1 = Point.draw()
#
# point1 = Point() #Same as instantiating a function expression in JavaScript with "New"
# point1.x = 10
# point1.y = 20
# print(point1.x)
#
# point2 = Point()
# point2.x = 1
# print(point2.x)


# 03:07:58 - CONSTRUCTORS (THEY ARE functions THAT GET CALLED AT THE TIME OF CREATING AN object)
#
# class Point:
#     def __init__(self, x, y): #This is the constructor
#         self.x = x
#         self.y = y
    
#     def move():
#         print('move')
#
#     def draw():
#         print('draw')
#
# point3 = Point(7,8)
# point3.y = 9
# print(point3.x, point3.y)


# 03:11:25 - EXERCISE
#
# class Person:
#     def __init__(self, name): #This is the constructor method...
#         self.name = name #...and this is me adding an attribute called name to the constructor
#
#     def talk(self):
#         print(f'Hi my name is {self.name}')
#
# tim = Person('Tim')
# tim.talk()
#
# bob = Person('Bob')
# bob.talk()


# 03:14:54 - INHERITANCE, EMPTY classes, pass STATEMENT
#
# class Mammal:
#     def __init__(self, name):
#         self.name = name
#     def walk(self):
#         print('walk')
#
# class Mouse(Mammal): #Mouse class inherits everything from Mammal class but doesn't have any further methods or attributes itself so "pass" must be placed in that class
#     pass
#
# class Dog(Mammal):
#     def bark(self):
#         print('I\'m barking')
#
# class Cat(Mammal):
#     def meow(self):
#         print(f'I\'m meowing and my name is {self.name}')
#
# cat1 = Cat('Felix')
# cat1.meow()


# 03:19:48 - modules IN Python SIMILAR TO JAVASCRIPT, from IN module imports
#
#import <name of file without .py extension>
#from <name of module> import <name of method or variable>


# 03:24:06 - EXERCISE
# from utils_Mosh_Youtube_Python_Full_Course import find_max
# numbers_list = [4,6,7,4,3,2]
# maximum_num = find_max(numbers_list)
# print(maximum_num)


# 03:30:26 - Packages (SIMPLY DIRECTORIES/FOLDERS CONTAINING modules, THE WAY TO CREATE packages IS TO MAKE A FOLDER AND INCLUDE AN EMPTY __init__.py FILE. YOU CAN import THE ENTIRE package, JUST A module from THE package OR JUST A method from THE module from THE package USING DOT SYNTAX)


# 03:36:36 - GENERATING RANDOM VALUES, modules BUILD INTO Python's standard library FOUND AT https://docs.python.org/3/py-modindex.html
#
#import random
#
# for i in range(3):
#     print(random.random())
# for i in range(3):
#     print(random.randint(0,130))
#
# people = ['John', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(people)
# print(leader)


# 03:41:36 - EXERCISE
#
# import random
# class Dice:
#     def roll():
#         return random.randint(1,6), random.randint(1,6) #No need to wrap this in parentheses because Python will automatically interpret this as a tuple
#
# roll1 = Dice.roll()
# print(roll1)


# 03:44:53 - FILES AND DIRECTORIES, Path module, exists and glob methods
#
# from pathlib import Path #Similar to importing 'fs' in JavaScript plus has features of 
# from time import sleep
#
# path1 = Path('ecommerce')
# path2 = Path('email')
#
# print(path2.exists()) #path2.exists returns False
#
# path2.mkdir()#...until path2.mkdir is called...
# print(path2.exists()) #...now it returns True...
#
# sleep(2) #...pause the script for 2 seconds...
#
# path2.rmdir() #...but when path2.rmdir os called...
#
# print(path2.exists())#...now it returns False
#
# path3 = Path()
#
# for file in path3.glob('*.py'):
#     print(file)
#
# for file in path3.glob('*'):
#     print(file)


# 03:51:02 - Pypi and Pip #Pypi is an open source package repository like npm
#
# pip3 install openpyxl


# 03:56:13 - EXCEL, import <name of package> as <alias you choose>
#
# import openpyxl as xl
# from xl.chart import BarChart, Reference
#
# wb = xl.load_workbook('transactions.xlsx')
# sheet_1 = wb['Sheet1']
#
# # cell_a_1 = sheet_1['a1'] #As an example you can get column then row with square bracket syntax...
# # print(cell_a_1.value)
# # cell_a_2 = sheet_1.cell(1, 2) #...or get get row then column with cell method...
# # print(cell_a_2.value)
# # cell_b_1 = sheet_1['a2'] #...again, get column then row with square bracket syntax...
# # print(cell_b_1.value)
# # cell_b_2 = sheet_1.cell(2, 2)  #...or get get row then column with cell method...
# # print(cell_b_2.value)
#
# max_number_of_rows = sheet_1.max_row
#
# for row in range(2, max_number_of_rows + 1): #Loop through all rows except the first which is a header...
#     cell = sheet_1.cell(row, 3) #...and make cell equal to the cell of the row in question at the 3rd column...
#     #cell = sheet_1[f'c{row}'] #...or you could equally use square bracket syntax for this...
#     corrected_price = cell.value * .9 #...and correct the cell by reducing it 10% of its value
#     corrected_price_cell = sheet_1.cell(row, 4)
#     corrected_price_cell.value = corrected_price
#
# values = Reference(sheet_1, min_row=2, max_row=sheet_1.max_row, min_col=4, max_col=4) #This is rows 2 to 4
#
# chart = BarChart()
# chart.add_data(values)
# sheet_1.add_chart(chart, 'e2')
#
# wb.save('transactions2.xlsx')


# 04:08:42 - EXERCISE (EXTEND THE ABOVE TO A FUNCTION)
#
# import openpyxl as xl
# from xl.chart import BarChart, Reference
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet_1 = wb['Sheet1']
#
#     for row in range(2, max_number_of_rows + 1): #Loop through all rows except the first which is a header...
#         cell = sheet_1.cell(row, 3) #...and make cell equal to the cell of the row in question at the 3rd column...
#         #cell = sheet_1[f'c{row}'] #...or you could equally use square bracket syntax for this...
#         corrected_price = cell.value * .9 #...and correct the cell by reducing it 10% of its value
#         corrected_price_cell = sheet_1.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#         values = Reference(sheet_1, min_row=2, max_row=sheet_1.max_row, min_col=4, max_col=4) #This is rows 2 to 4
#
#         chart = BarChart()
#         chart.add_data(values)
#         sheet_1.add_chart(chart, 'e2')
#
#         wb.save(filename)


# 04:11:07 - MACHINE LEARNING, MACHINE LEARNING LIBRARIES, Numpy, Pandas and DataFrames, MatPlotLib, Scikit-Learn, LOADING A CSV FILE in Jupyter, CLEANING/PREPARING DATA, SPLITTING DATASETS, LEARNING AND PREDICTING, decision tree algorithm, persisting models, VISUALIZING A decision tree, <...THIS WAS CONDUCTED FROM WITHIN CHROME RUNNING Jupyter because Terminal WON'T DISPLAY ALL THE DATA WE NEED TO SEE>

# *** Note, I installed the Jupyter notebooks extension from Microsoft (which also came with Jupyter Cell Tags, Jupyter Keymap, Jupyter Notebook Renderers and Jupyter Side Show) instead of    https://jupyter.org    then    Anaconda per    https://www.youtube.com/watch?v=h1sAzPojKMg    using the link    https://www.anaconda.com/download/success    to download the 64-Bit (M1) Graphical Installer (697.4M)    thereby skipping registration entirely, when Anaconda Navigator prompted for an upgrade I declined and closed it altogether, then simply ran    jupyter notebook    from Terminal to start    http://localhost:8888/tree    in Chrome. Note, the course is outdated, I had to directly    import joblib    rather than    from sklearn.externals import joblib    . Also, instead of using the    "Graphviz (dot) language support for Visual Studio Code" by Stephanvs    extension I got the    "Graphviz Interactive Preview" by tintinweb    per    https://stackoverflow.com/a/78011002    and click "DOT" in the top right to activate the visualization
