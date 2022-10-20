#Sometimes if you want to do something several times | use the 'range' function | List up from 0 to but not including cutoff
#EX) numbers = range(10) where numbers is [0,1,2,3,4,5,6,7,8,9]
#number lists created using range used to run a loop of fixed numbers,
#Can skip numbers | range(START #, END # (NOT INCLUDED IN LIST), INCREMENTS):

for xloc in range(50, 1000, 80):
    print(f"I want to raw a line at xposition: {xloc}")

#you can also count down using the same method as skipping numbers

for countdown in range(10, 1, -1):
    print(countdown)

#tuples are a kind of immutable list/read-only list. it does not change
#like strings, once it is made you can't change it But you can mutate it (uppercase it, lowercase it, ect)

student=("john", 3.2, 92)

#Slices copies part of a sequence (String,list,tuple) into a new one
#Use sequence[X:Y] to make a copy of a part of the sequence

weekdays=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
work_days=weekdays[1:6]
print(work_days)

#You can omit a value in [X:Y] | [:Y] , [X:], [:] | The omitted value will start/end with omitted value
#Len - lets us know now many things are in a sequence
    #len(sequence) is the function we use
    #Spaces count as characters when using num_chars

weekdays=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
how_many=len(weekdays)
print(how_many)
desc="How many days are in a week"
num_chars=len(desc)
print(num_chars)