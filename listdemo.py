weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friiday', 'Saturday']
weekdays[-2] = 'Friday'
print (weekdays)

courses = ['Comp151', 'Math140', 'Math142']
courses.append('Comp150')
courses.insert(1, 'Comp143')
print(courses)
# courses.remove('Comp150')
courses.pop(4) #or -1 if you're counting backwards
print(courses)