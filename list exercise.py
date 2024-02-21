'''list=[1,4,6,9,7,10]
number=[y+10 for y in list]
print(number)

list=[1,4,6,9,7,10]
list.sort()
print(list)

list=[1,4,6,9,7,10]
list.sort(reverse=True)
print(list)'''

'''list=[1,4,6,9,7,10]
list2=list.copy()
print(list)
print(list2)

list=[1,4,6,9,7,10]
thislist = ["apple", "banana", "cherry"]
list.extend(thislist)
print(list)

list= [["apple", "banana", "cherry"],["saikat","alam","shifat"],["mahabub","alam","bishal"]]
y=list[2][2]
print(y)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2])
print(thislist[2:5])'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(type(thislist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "coconat" in thislist:
    print("yes")

list=[1,4,6,9,7,10]
thislist = ["apple", "banana", "cherry"]
list.append(thislist)
print(list)