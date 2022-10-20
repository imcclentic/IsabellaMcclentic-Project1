rec_file = open("sillyRec.txt", 'r')
rec_lines = rec_file.readlines()
line_number = 1
for line in rec_lines:
    if line_number % 2 ==1:
        print(line)
    line_number = line_number +1
print(line_number)


