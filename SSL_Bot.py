#This is an Input/Output AI Chatbot based on Manual Rules

import os#FFFF00
os.system('color 5f') # sets the background to blue

#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#start the conversation
print('Bot: Hi, Welcome to SSL Wireless!') #greeting
speak.Speak('Hi Welcome to SSL Wireless!') #!')

#keep going the conversation
print('Bot: Whats your name?') #ask
speak.Speak('Whats your name?')
Name = input() #save answer
print('Bot: Im glad to meet you, ' + Name + '!!') #reply
speak.Speak('Im glad to meet you, ' + Name + '!!')
print('Bot: The number of letters of your name is:')
speak.Speak('The number of letters of your name is:')

#Couting name
count = 0
for i in range(0, len(Name)):
	if( Name[i] != ' '):
		count = count + 1

print(count)
speak.Speak(count)

#keep going the conversation
print('Bot: How old are you?') #ask
speak.Speak('How old are you?')
Reply = input() #save answer
print("User:" + Reply)
print('Bot: Okay, then you will be ' + str(int(Reply) + 1) + ' next year.') #reply
speak.Speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')

#keep going the conversation 
print('Bot: Whats the name of your brother?') #ask
speak.Speak('Whats the name of your brother?')
Reply = input() #save answer
print('Bot: Awesome!, my brothers name is also ' + Reply + '!!') #reply
speak.Speak('Awesome!, my brothers name is also ' + Reply + '!!')

#keep going the conversation
print('Bot: It was nice meeting you, \n Bye') #ask
speak.Speak('It was nice meeting you, \r\n Bye')
Reply = input() #save answer
print('Bot: Okay , See you') #reply
speak.Speak('Okay , See you.')





