#checking several conditions | if-elif-else | As soon as one condition is true the rest are skipped
#Most restrictive condition should be first

answer = input("What do you think of 4chan?")
if len(answer) >200:
    print("Wow that was alot")
elif len(answer) >125:
    print("Why did you put so much thought into it")
elif len(answer) >50:
    print("That's valid")
elif len(answer) >1:
    print("I feel that...")
else:
    print("That's fair, have a good day")