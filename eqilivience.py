#equality ==
# = IS THE ASSIGNMENT NOT EQUALITY
#greater then >
#less then <
#not equal !=
#if and only if (iff)

#Or = either can be true
#And = Both must be true

#example:
#age = int(input ("How old are you"))
#if age >=21:
    #print("Welcome to the bar")
    #print("Come as you are")
#if age <21:
    #print("go home")

us_recession_start_year=[1920, 1923, 1926, 1929, 1937, 1945, 1949, 1953, 1958,
                         1958, 1960, 1969, 1973, 1980, 1981, 1990, 2001, 2008, 2020]
total_election_years = 0
for recession_year in us_recession_start_year:
    if recession_year % 4 == 0:
        total_election_years = total_election_years +1
        print(f"election and recession in {recession_year}")
print(f"There where {total_election_years} that started recession and where election years")

courses = ["comp151", "comp152", "math130", "math120"]
if "comp250" in courses:
    print("yes it is there")
if "com250" not in courses:
    print("no it is not in there")

#Short curcuit logical operators | False -and- anything is false | True -or- anything is true

#if-else | if we want to do one thing if a condition is true and another if it is false

