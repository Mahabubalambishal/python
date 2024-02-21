#read file create kori
file=open("object oriented programming.py","r")
print(file.read())
file.close()
#readline file create kori
'''file=open("object oriented programming.py","r")
print(file.readline())'''

#readlines file create kori
'''file=open("object oriented programming.py","r")
print(file.readlines())'''

#readable file create kori
'''file=open("object oriented programming.py","r")
print(file.readable())'''

#write file create kori(faka file a kono kichu likhi)
'''file=open("write file.py","w")
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")'''

#write file create kori(likha file kichu notun kore kichu likhi)
'''file=open("write file.py","a")
file.write("My department name is Computer.")'''

#read write uvoy file create kori
'''file=open("write file.py","r+")
print(file.read())
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")
file.seek(0,0)
print(file.read())
file.close()'''

#write read uvoy file create kori
'''file=open("write file.py","w+")
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")
print(file.read())
#file.seek(0,0)
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")
file.close()'''

#write read uvoy file create kori(append ar maddhome)
'''file=open("write file.py","a+")
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")
print(file.read())
#file.seek(0,0)
file.write("My name is Mahabub Alam Bishal.I am student in Dinajpur Polytechnic Institute.")
file.close()'''

#seek method use kore sentence ar word gulo alada kore pori(jekono ta ullekh kori)
'''file=open("write file.py","r")
file.seek(6,0)
print(file.read())'''

#seek method use kore sentence ar word gulo alada kore pori(jekono ta ullekh kori)
'''file=open("write file.py","r")
file.seek(0,0)
print(file.read(6))'''

#create kora file update kori (seek method ar maddhome,aijoono read write file function use kori)
'''file=open("write file.py","r+")
print(file.read())
file.seek(9,0)
file.write(" Rangpur")
file.seek(0,0)
print(file.read())
file.close()'''

#file a directory ar abosthan create kori(current directory/relative path)
'''file=open("write file.py","r")
print(file.read())
file.close()'''

'''file=open("","r")
print(file.read())
file.close()'''


















