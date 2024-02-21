#list make kori
'''name1=["mahabub","alam","bishal"]
print(name1)
print(name1[2])         #index number dekhar jonno number dhore call korte hoy
print(len(name1))       #kototi upadan acce ta dekhar jonno len function babohar kora hoy'''

#input function make kori
'''name1=input("name defined")
print("my name is",name1)'''
'''name1=input("name1")
name2=input("name2")
print("name1+name2",name1+ name2)'''

#condition statement use kori
'''country=["ban","ind","sri","pak"]      #input variable niye condition puron kori
saarc_member=input("country name")
if saarc_member in country:
    print(saarc_member,"member of saarc")
else:
    print(saarc_member,"is not member of country")'''

'''name=["mahabub","alam","bishal"]      #ak variable ar man onno variable acce naki ta condition kore dekhi
name1="saikat"
if name1 in name:
    print(name1,"acce")
else:
    print(name1,"nai")'''

'''a=7          #ak variable man ar shathe onno variable tulona kori
b=10
if a<b:
    print("true")
else:
    print("false")'''

'''marks=input("please enter the input")
marks=int(marks)
if marks>=80:
    grade="a+"
elif marks>=70:
    grade="a"
elif marks>=60:
    grade="a-"
elif marks>=50:
    grade="b"
elif marks>=40:
    grade="c"
else:
    grade="f"
print("your grade is",grade)'''

'''a=30
b=50
c=45
if a>b:
    boro=a
else:
    boro=b
if c>boro:
    boro=c
print("maximum",boro)'''

'''year=input("shal")
year=int(year)
if year%4==0:
    print(year,"lip year shal")
elif year%400==0:
    print(year,"llip year shal")
elif year%100==0:
    print(year,"not lip year")
else:
    print(year,"not lip year")'''

#turtle module make kori
'''import turtle
turtle.forward(100)
turtle.exitonclick()'''

'''import turtle
turtle.shape("turtle")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.exitonclick()'''

#loop ar babohar dekhi
'''for name in range(10):
    print("i want o be a great programmer")'''

'''for name in range(10):
    print(name)'''
'''number=0
for i in range(1,51):
    number=number+1
    print(number)'''

'''number=0
for mahabub in range(50):
    number=number+1
    print(number)'''

'''for name in range(1,101,4):
    print(name)'''

'''country=["bangladesh","india","pakistan","nepal","sri-lanka","bhutan","afghanistan","maldip"]
for name in country:
    print(name,"is a south asian country")'''

'''for number in range(11):
    print(number)
number=list(range(11))
print(number)'''

'''a=[10,20,30,40]
result=0
for add in a:

    result=result+add
    print(result)'''

'''result=0
for i in range(1,51):
    result=result+i
    print(result)'''

'''number=0
while number<50:
    number=number+1
    print(number)'''
'''a=[6,1,3,0,9,3,2,5]
big=a[0]
for n in a:
    if n>big:
        big=n
        print(n)'''
'''list1=[2345,2367,2656,7890,3456,8901,1235,7865,4532]
list2=list1[0]
for i in list1:
    if i>list2:
        list2=i
        print(list2)'''

'''n=input("enter your number")
n=int(n)
m=1
while m<=10:
    print(n,"x",m,"=",n*m)
    m=m+1'''

#break ar continue statement use kori
'''a=1
while a<=10:

    if a == 6:
        break
    print(a)
    a=a+1

a=1
while a<=10:
    if a == 6:
        continue
    print(a)
    a=a+1'''

#function toiri kori
'''def student(a,b):
    c=a+b
    print(c)
    d=a-b
    print(d)
student(12,23)'''

#string niye kaj kori
'''a="bangladesh"
print(len(a))
print(a[0])'''

'''a="bangladesh"
for b in a:
    print(b)
a=["bangladesh","pakistan","india","sri-lanka"]
a[0]="china"
print(a)'''

#data type list ar sokol babohar
#akti list make kori
'''name=["mahabub","alam","bishal","mahim","mitu","saikat","shuvo","alif"]
print(name)

#list ar modddhe kono upadan add kori
name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name.append("hamim")       #list ar sobsheshe add hobe
print(name)

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name.insert(6,"hamim")     #index anujayi add kora jay
print(name)'''

#list ar kono item badh dewar jonno
'''name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name.remove("alam")
print(name)

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name.pop(2)
print(name)

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name.clear()

#list ar kono upadan change korar jonno
name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
name[2]="hridita"
print(name)

#list a kon upadan kototi acce ta dekhar jonno
name=[1,2,2,3,4,5,6]
name.count(2)
name=[12,5445,456,789,3457,3456]
name.sort()
print(name)

name=[12,5445,456,789,3457,3456]
name=[1,2,2,3,4,5,6]
name.reverse()
print(name)

name=[12,5445,456,789,3457,3456]
name2=[1,2,2,3,4,5,6]
name.extend(name2)
print(name)

name=[12,5445,456,789,3457,3456]
name2=[1,2,2,3,4,5,6]
print(name+name2)

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
str="-".join(name)
print(str)

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
print(name[0])

name=["mahabub","alam","bishal","mahim","saikat","shuvo","alif"]
print(type(name))

#tuple datatype ar babohar ullekh kori
name=("mahabub","alam","bishal","saikat","mahim","shahadat")
print(type(name))

name=("mahabub","alam","bishal","saikat","mahim","shahadat")
print(name[0])

name=("mahabub","alam","bishal","saikat","mahim","shahadat")
name1,name2,name3,name4,name5,name6=name
print(name2)

name=(1,2,3,5,[6,6,8],5.6,("apple","orange"))
for i in name:
    print(i,type(i))'''

#set datatype ar babohar ullekh kori
'''a={1,4,5,7,9,6,4,3}
print(type(a))

a={1,4,5,7,9,6,4,3}
print(a)

a=[1,3,6,8,9,4]
b=set(a)
print(b)

a=(1,4,5,7,8,9,6,4)
b=set(a)
print(b)

a="bangladesh"
b=set(a)
print(b)

a={1,4,5,7,9,6,4,3}
b=4 in a
print(b)

a={1,4,5,7,9,6,4,3}
b=10 in a
print(b)

a={1,2,3,4,5}
b={2,4,5,7,8,9}
c=a&b
print(c)

a={1,2,3,4,5}
b={2,4,5,7,8,9}
c=a^b
print(c)

a={1,2,3,4,5}
b={2,4,5,7,8,9}
c=a|b
print(c)

a={1,2,3,4,5}
b={2,4,5,7,8,9}
c=a-b
print(c)

a={1,2,3,4,5}
b={2,4,5,7,8,9}
c=b-a
print(c)'''

#dictionary datatype ar babohar ulloekh kori
#dictionary datatype key ooo value uvoye babohito hoy
'''name1={"mahabub":101,"bishal":102,"alam":103}
print(name1)

name1={"mahabub":101,"bishal":102,"alam":103}
print(type(name1))

name1={"mahabub":101,"bishal":102,"alam":103}
print(name1["bishal"])

name1={"mahabub":101,"bishal":102,"alam":103}'''

result={"mahabub":{"bangla":80,"english":90},"alam":{"bangla":70,"english":100},"bishal":{"bangla":66,"english":78}}
print(result["alam"])

result={"mahabub":{"bangla":80,"english":90},"alam":{"bangla":70,"english":100},"bishal":{"bangla":66,"english":78}}
print(result.keys())

result={"mahabub":{"bangla":80,"english":90},"alam":{"bangla":70,"english":100},"bishal":{"bangla":66,"english":78}}
print(result["mahabub"])











