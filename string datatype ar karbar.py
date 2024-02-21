#1.string datatype toiri kori
'''mahabub="I am a future programmer in Bangladesh"
print(mahabub)

#2.string ar protekti upadan ke alada alada string a porinito kori  (substring toiri kori)
mahabub="I am a future programmer in Bangladesh"
#bishal=mahabub.split()
print(mahabub.split())

mahabub="programmer in Bangladesh"
print(mahabub.split())

#3.string a kototi upadan acce ta bair kori
mahabub="programmer in Bangladesh"
print(len(mahabub))

mahabub="I am a future programmer in Bangladesh"
print(len(mahabub))

#4.string ar kono upadan ke dekhar jonno index number dhore call korte hoy
bishal="programmer"
print(bishal[5])

#5.string a babohito upadan gulo ke akotirito kori
name="bis" + "hal"
print(name)

#6.string ar moddhe kono akti upadan ke kujhar jonno
bishal="england"
print(bishal.find("gla"))

#7.string a kono upadan ke bodlate replace method babohar kori
bishal="my name is mahabub"
alam=bishal.replace("mahabub","hridita")
print(alam)
print(bishal)

#8.kono string a babohito upadan acce naki ta ullekh kori
bishal="mahabub"
print(bishal.startswith("m"))

bishal="mahabub"
print(bishal.endswith("h"))

#9.string ar vitor kono upadaner songha dekhar jonno
bishal="mahabub is a student"
print(bishal.count("a"))

#10.string ke uppercase,lowercase  oo capitalize a rupantor kori
bishal="mahabub"
print(bishal.upper())

bishal="MAHABUB"
print(bishal.lower())

bishal="mahabub"
print(bishal.capitalize())

#11.string a space komanor jonno
bishal="  alam  "
print(bishal)

bishal="  alam  "
print(bishal.strip())

bishal=" alam  "
print(bishal.lstrip())

bishal="  alam "
print(bishal.rstrip())'''

bishal="mahabub alam bishal"
print(bishal.split())

bishal="mahabub alam bishal"
print(bishal.replace("mahabub","asmaul"))

bishal="mahabub alam bishal"
print(len(bishal))


bishal="mahabub alam bishal"
print(bishal.find("bub"))

bishal="mahabub alam bishal"
print(bishal[4])

bishal="mahabub alam alam bishal"
print(bishal.count("alam"))


