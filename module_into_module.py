from create_own_module import mahabub
class saikat(mahabub):
    def __init__(self, age, address, nationality, religion, school):
        super().__init__(age, address, nationality, religion)
        self.school = school

    def all(self):
        print(self.age)
        print(self.address)
        print(self.nationality)
        print(self.religion)
        print(self.school)