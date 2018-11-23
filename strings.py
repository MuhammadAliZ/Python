message = "Hello,World"

print(message)
print(len(message)) #Length of the string
print(message[0]) #Index
print(message[10]) #Index
print(message[-1]) #Index
print(message[0:5]) #range where the first index is inclusive where the second index is not
print(message[:5]) #slicing
print(message[6:11])
print(message[6:])

print("-----------STRINGS METHODS------")

print(message.lower()) #To lower case characters
print(message.upper()) #To uppercase characters
print(message.count("hello")) #To count number of characters in a specifc part of the message
print(message.count("Hello"))
print(message.count("l"))
print(message.find("world")) #finding the index of a specific part of the message
print(message.find("ello"))
print(message.find(","))
print(message.find("l"))
print(message.find("universe")) #if not found, it output -1

#message.replece('World', 'Universe') #Returns a string with the new value. Doesn't replace in place
message2 = message.replace('World', 'Universe')
print(message)
print(message2)

#Concatenation
greeting = 'Hello'
name = 'Michael'
message3 = greeting + ', ' + name + '. Welcome!'
print(message3)

#formatted string using dot format method and place holders

message4 = '{}, {}. Welcome!'.format(greeting, name)
print(message4)

#String fromatting using f string without placeholder
#message5 = f'{greeting}, {name.upper()}. Welcome!'
#print(message5)

print('----------------------------------------')

#dir #help
#print(dir(name))
#print(help(str))
#print(help(str.lower))
