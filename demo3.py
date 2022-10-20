#courses_file = open("requiredCS.txt", 'r')

#lines_from_file = courses_file.readlines()
#for line in lines_from_file:
    #loud_line = line.upper()
    #loud_line = loud_line.strip()
    #print(loud_line)
   # list = line.split(' : ')
   # print(list[0])
   # print(list[1])

#print("Those are the classes you have to take for a CS major")


# KEYWORDS FOR <new variable> and IN <list variable>
# Code block: used to determine which code belongs to a 'chunk' | determines what code is part of 'for' loop
# Code blocks are determined by indentations, all code indented to the same level are part of the same block
# strip take out any invisible characters (in this case it gets rid of the line spaces in between each item)

#demo = 'this that this those'
#words = demo.split(' ')
#print(words)
#print(words[1])

names_file = open("names.txt", 'r')
all_names = names_file.readlines()
for names_line in all_names:
    names_line = names_line.strip()
    names_line = names_line.split('-')
    print(f"{names_line[0]} is {names_line[1]} years old")