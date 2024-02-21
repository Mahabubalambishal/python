#1.set datatype toiri kori
name={"mahabub","alam","bishal","mahfuj","alam","mahim"}
print(name)

name={"mahabub","alam","bishal","mahfuj","alam","mahim"}
print(type(name))

name=("mahabub","alam","bishal","mahfuj","alam","mahim")
name1=set(name)
print(name1)

name=set("bangladesh")
for names in name:
    print(names,type(names))

a={1,2,3,4,5}
b={2,4,6,8,5}
c=a&b
print(c)

a={1,2,3,4,5}
b={2,4,6,8,5}
c=a^b
print(c)

a={1,2,3,4,5}
b={2,4,6,8,5}
c=a|b
print(c)

a={1,2,3,4,5}
b={2,4,6,8,5}
c=a-b
print(c)

a={1,2,3,4,5}
b={2,4,6,8,5}
c=b-a
print(c)
