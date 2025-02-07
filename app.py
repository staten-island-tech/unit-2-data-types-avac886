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

#Challenge 1
sentence = input("Enter a sentence:")
def WordCount():
    x = sentence.split()
    print(x)
    print(len(x))
WordCount()

#Challenge 2
