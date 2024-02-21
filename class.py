#object ar shathe class toiri korlam
'''class name1:
    pass
mahabub=name1(   )
alam=name1(    )
mahabub.age=20              #object ar maddhome class define korchi
mahabub.school="sunflower"
alam.age=18
alam.school="kinter garden"
print(alam.school)
print(mahabub.school)'''


#class variable  ar shathe class toiri korlam (variable ar upadanti prottekti object ar common upadan hisabe babohito hoy)

'''class name1:
    father_name="muksadul haq"    #variable ar maddhome class define korchi
mahabub=name1(   )
alam=name1(    )
mahabub.age=20
mahabub.school="sunflower"
alam.age=18
alam.school="kinter garden"
print(alam.father_name)
print(mahabub.father_name)'''

#__init__() ba constractor ar maddhome class toiri kori (constractor ba __init__() ar kaj holo value ba attribute ar man parametera received kora)
'''class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.hobby="programming"       #object ar maddhome class define korchi
alam.hobby="playing game"
print(mahabub.father_name)
print(mahabub.age)
print(mahabub.school)
print(mahabub.hobby)
print(alam.father_name)
print(alam.age)
print(alam.school)
print(alam.hobby)'''

#notun method toirir maddhome class toiri kori (sokol class ke akottre dekhar jonno mathod use kori)
'''class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
alam.all()
mahabub.all()'''


#class ar kono upadan ke change ba modify kori (ai jonno class ke object ar name dhore change korte hobe)

'''class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.all()
mahabub.age=25               #class ke object ar name dhore change korlam
mahabub.all()'''


#delete object properties
'''class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
#mahabub.all()
#mahabub.age=25      #class ke object ar name dhore change korlam
del alam.age     #object properties delete korlam
alam.all()'''

#delete object (jekono object ke delete kori)

'''class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
del mahabub                    #object ke delete korlam
mahabub.all()
alam.all()
#mahabub.age=25               #class ke object ar name dhore change korlam
#mahabub.all()'''

#__doc__ method ar maddhome kon object ooo class define kora hoyeche ta dekhi (object oo class ar surute string ke dekhar jonno)

'''class name:
    this object and class defined       #__doc__method use kore korlam
       only father name,age and school
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
#del mahabub                    #object ke delete korlam
#mahabub.all()
#alam.all()
#mahabub.age=25               #class ke object ar name dhore change korlam
#mahabub.all()
print(name.__doc__)'''

#build in __dict__ method use kore object ar property gulo dictionary akare sajai (dictionary datatype ar moto use kori)

class name:
    father_name="muksadul"      #variable ar maddhome class define korchi
    mother_name="mahafuja"
    def __init__(self,age,school):    #__init__() ba constractor ar maddhome class define korchi
        self.age=age
        self.school=school
    def all(self):                    #method ar maddhome sokol class ke akkottore define korchi
        #print(self.age,self.school,self.father_name,self.mother_name)
        print(self.school)
        print(self.father_name)
        print(self.mother_name)
        print(self.age)

mahabub=name(20,"sunflower")
alam=name(18,"kinter garden")
mahabub.all()
print(mahabub.__dict__)