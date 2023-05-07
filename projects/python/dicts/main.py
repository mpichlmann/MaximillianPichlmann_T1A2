import greet #here we are importing our functions that have been defined over in the greet.py file 
from greet import hello, goodbye #this is a way of importing only specific functions in the greet.py file

greet.hello('matt') #here we are using the greet module, on the hello function

print(greet.PI) #we can even create variables and call them 
print(dir(greet)) #this will print all the functions that are in the greet module 

from terminal_palette import Palette
p = Palette()
print(p.red('some text'))