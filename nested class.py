#nested class toiri kori (class ar vitor class toiri kori)
#single nested class toiri kori
'''class muksadul:
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def address(self):
        print(self.father_name)
        print(self.mother_name)
        print("sonapukur")

    class son_mahabub:    #nested class toiri korlam (class ar vitor class toiri korlam)
        def __init__(self,father_name,mother_name):
            self.father_name = father_name
            self.mother_name = mother_name

        def address(self):
            print(self.father_name)
            print(self.mother_name)
            print("dinajpur")
muksadul1=muksadul("syedali","moslema")
son_mahabub1=muksadul1.son_mahabub("muksadul","mahafuja")       #class ar vitor class received korlam
muksadul1.address()
son_mahabub1.address()'''


#class ar vitor double nested class toiri kori (nested class ar vitor abar  notun nested class toiri kori)
'''class muksadul:
    def __init__(self,father_name,mother_name):
        self.father_name=father_name
        self.mother_name=mother_name
    def address(self):
        print(self.father_name)
        print(self.mother_name)
        print("sonapukur")

    class son_mahabub:    #nested class toiri korlam (class ar vitor class toiri korlam)
        def __init__(self,father_name,mother_name):
            self.father_name = father_name
            self.mother_name = mother_name

        def address(self):
            print(self.father_name)
            print(self.mother_name)
            print("dinajpur")
        class mahabub_daughter_hridita:  #nested class ar vitor abar nested class toiri korlam
            def __init__(self,father_name,mother_name):
                self.father_name = father_name
                self.mother_name = mother_name

            def address(self):
                print(self.father_name)
                print(self.mother_name)
                print("america")
muksadul1=muksadul("syedali","moslema")
son_mahabub1=muksadul1.son_mahabub("muksadul","mahafuja")      #class ar vitor class received korlam
mahabub_daughter_hridita1=muksadul1.son_mahabub.mahabub_daughter_hridita("mahabub","mahabuba")    #nested class ar vitor abar nested class received korlam

muksadul1.address()
son_mahabub1.address()
mahabub_daughter_hridita1.address()'''


