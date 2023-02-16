"With this method you can create a list in Python"

x = list()

while True:
    inp = input("Please give an Element in your list: ")
    if inp == "done" : break
    y = float(inp) #Here you can change the Value of your list to a string, float or a integer
    x.append(y)

print(x)

