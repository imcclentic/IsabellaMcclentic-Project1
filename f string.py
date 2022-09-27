name = input("what is your name")
greeting = f"hello, {name}, nice to meet you"
print(greeting)

# % = ModulO
# constant is a varible that cannot be changed, python doesn't have real constants, typically they are done in all CAPS
# Large numbers: use underscores in numbers to act as 'commas' in very large numbers (ex 10000000 vs 10_000_000)
# a comment (#) is something you write in a code that is meant for other programmers, and is ignored by the computer
# they explain the reasoning or to explain what something is trying to do or why you did something a certain way
# Comments can also happen at the end of a line, after a readable string but not in the middle

# We store things in variables for later use (including numbers and strings)
# String | name = 'fwofhnf'
# integers | age = 123
# floating point numbers | gpa = 3.5
# subtracting/adding | num = 4.2 .... num +/- 3 = result (7.2 or 1.2)

# Linear collection is a list - a data storage system where items are stored with a one by one order.
# Can hold any data type, but keep it consistent (all numbers or strings, ect) and they start from 0
# Creating a list | student _list = ["string", "string", "string" ect] or student_list2 = list (string" ect)
# to access a single item in the list | ..._name = ...[2] and it will select the value in tht position
# to change a list | ..._name[1] = name will put that name in the first position
# keep list names plural since it has several items and MAKE THE NAMES MAKE SENSE
# to add an item to the list later | NAME.append ('ADDED VALUE')
# or to put it in a specific position | NAME.insert(1, 'VALUE')
# removing items from a list | NAME.remove ('ITEM YOU WANT TO REMOVE') | it only removed the first occurrence in the list
# to remove an item that when you know its position | NAME.pop (POSITION)
# List index | THE POSITION OF AN ITEM IS GUNNA BE ONE LESS THEN YOU THIS BECAUSE THE LIST STARTS A 0 (WHEN FORWARD)
# to open a TEXT file | my_file (FILE.TXT, r/w/a) r = reading, w = writing - override entire file, a = appending, edit at end
# NEVER OPEN A .py FILE!!!
# all_lines = my_file.readlines() to make everything into strings