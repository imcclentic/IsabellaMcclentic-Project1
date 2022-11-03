#the remove function gets rid of the first occurenance in the list
#while <ITEM> in <LIST NAME>
    #<LIST NAME>.remove(<ITEM>)

books = ["Python Crash Course", "Game Programming", "Code Complete", "Clean Code", "Python Crash Course",
         "The Pragmatic Programmer", "Python Crash Course"]

while "Python Crash Course" in books:
    books.remove("Python Crash Course")

#for location in range(len(books)):
    #if books[location] == "Python Crash Course":
        #books.pop(location)
    #This doesn't work because the list can change and the location will be messed up

print(books)


