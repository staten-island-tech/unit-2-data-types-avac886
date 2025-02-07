""" #Integers and Floats
x = 3
y = float(3)
print(x,y)
 """

'''''
#Tip Calculator
bill = input("Enter bill amount:")
tip = input("Enter tip amount:")

bill = float(bill)
tip = int(tip)

total = bill + tip
print(f"The bill is ${bill}. The tip is ${tip}. The total is ${total}")
'''''

""" #Lists
values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" #What if we just want one single, specific value?
values = [1,2.23,5,7,2,30,15,4]
print(values[0])
print(values[7]) """

'''''
#Strings
"test"
["t","e","s","t"]
'''''

'''''
#String Methods
x = "this is a thing"
y= x.split()
z = y[1]
print(y)
print(z)
'''''

'''''
#Challenge 1
sentence = input("Enter a sentence:")
def WordCount():
    x = sentence.split()
    print(x)
    print(len(x))
WordCount()
'''''

""" #Mad Libs Project
Name = input("Write a male name:")
Number1 = input("Write a number:")
Noun1 = input("Write a noun:")
Celebrity_Name1 = input("Write a celebrity name:")
Verb1 = input("Write a verb:")
Celebrity_Pronouns = input("Write the celebtrity's pronouns:")
Verb2 = input("Write a verb:")
Adjective1 = input("Write adjectives:")
Dumb_Word = input("Write a dumb word:")
Action = input("Write an action:")
Adjective2 = input("Write an adjective:")
Feelings = input("Write feelings:")
Onomatopiea = input("Write an onomatopiea:") """

'''''
def new_func(Name, Number1, Noun1, Celebrity_Name1, Verb1, Celebrity_Pronouns, Verb2, Adjective1, Dumb_Word, Action, Adjective2, Feelings, Onomatopiea):
    print(f"""{Name} is a smart lawyer who married into a wealthy
family. How rich was the family you ask? Well the family's 
wealth was top {Number1} in {Noun1}! With just one phone call
{Celebrity_Name1} would come {Verb1} to them as fast as
{Celebrity_Pronouns} legs can get them. Now with such a wealthy
family and job, {Name} must be loving his life right now right?
Quite the contrary actually! Because great wealth comes great
responsibilities! Everday, {Name} has to {Verb2} to every call
he gets from his family in law to help soothe out problems. He
has no freedom! Poor, poor {Name} doesn't even get treated 
nicely too. Most of all, {Name} doesn't even get a single share
of the wealth the family has. And so, with a sad married life, 
{Adjective1} in laws, and a bunch of {Dumb_Word}, {Name} 
decided to {Action}. This was the {Adjective2} decision of his
life! He's {Feelings}! But suddenly a car came crashing into
him and {Onomatopiea}, he's awake. Turns out it was a all a
dream and he's still stuck with the wealthy family. Such a sad
life but never fear, {Name} grew closer to the family and the 
family began to love him as if he was their own. How sweet. 
The End.""")
'''''

""" new_func(Name, Number1, Noun1, Celebrity_Name1, Verb1, Celebrity_Pronouns, Verb2, Adjective1, Dumb_Word, Action, Adjective2, Feelings, Onomatopiea)
 """

""" #Booleans and Control Flow
day_of_week = input("What day is it?")
if day_of_week == "Friday":
    print("Correct") 
else:
    print("Incorrect") """

""" #F Strings
x = "test"
print(f"hello {x}")

temp = 60
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Challenge 1
number = input("Write a number")

#Challenge 2
bill = input("How much was the bill?")
def tip():
    service = input("How was the service? (Write bad, okay, good, or great)")
    if service == "bad":
        total = bill * 0.0 

#Challenge 3

#Challenge 4


""" def login(password):
    #if statement evaluates to true do next line
    if password == "secret":
        print("logged in")
    else:
        print("incorrect password")
 """

def temp(x):
    if x >= 80: 
        print("too hot")
    elif x > 60:
        print("nice")
    else:
        print("too cold")

x = int(input("what da the temp"))