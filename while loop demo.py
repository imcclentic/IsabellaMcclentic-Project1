import gtts
from playsound import playsound

#two kinds of loops:
    #we do something for each element of a collection using the keyword 'for'
    #we do something until to world situation meets some condition using the keyword 'while'
        #real life - shovel snow until its gone
        #ask user for input until they give the right answer
            #Syntax
                # while <condition>
                    #code clock
        ##Be careful of infinate loops
            #update the conditions inside fo the loop or it will loop forever

#number_of_questions = get_number_of_students()
#while number_of_questions >0:
    #print("your question is...")

# a flag variable is a term for a boolean type variable to deterimine if we should do something or not
# set the flag to false till the would changes to be done the loop

#done = False
#while not done:
    #answer = float(input("enter gpa, enter number from 0 to 4"))
    #if 0 <= answer <=4:
        #done = True

# if a program should do something froever then we do a special loop
# forever means until the program ends like in games ect

#while true
    #Do stuff here
    # to end use the keyword 'break'
    # if using in a loop in a loop it will only end the current loop

said_right_thing = False
while not said_right_thing:
    question = input("will you take me with you?")
    good_answers = ["yes", "okay", "yup", "yeah", "fine", "ok"]
    if question.lower() in good_answers:
        said_right_thing = True

# to say text outloud - import a new library and install gtts, playsound, and pyttsx3

celebrate = "hooray, you will take me with you! and forever"
speaker = gtts.gTTS(celebrate)
speaker.save("speaker1.mp3")
playsound("speaker1.mp3")
creepy = "and ever!"
speaker2 = gtts.gTTS(creepy)
speaker.save("creepy.mp3")
for repeat in range(10):
    playsound(creepy.mp3)