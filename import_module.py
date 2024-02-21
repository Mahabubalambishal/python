'''#create_own_module theke kono class ke import kori

#create_own_module theke muksadul class ke import kori
from create_own_module import muksadul
muksadul1=muksadul(40,"sonapukur","bangladeshi")
muksadul1.all()'''


#create_own_module theke double class ke import kori (muksadul,mahabub double class)
'''from create_own_module import muksadul as m
from create_own_module import mahabub as ma
muksadul1=m(40,"sonapukur","bangladeshi")
mahabub1=ma(20,"dinajpur","british","islam")
muksadul1.all()
mahabub1.all()'''


#create_own_module ke sompurno import kori (create_own_module ke sompurno vabe class toiri kori)
'''import create_own_module as m
muksadul1=m.muksadul(40,"sonapukur","bangladeshi")
mahabub1=m.mahabub(20,"dinajpur","british","islam")
muksadul1.all()
mahabub1.all()'''


#module into module (module ar vitor module)
import create_own_module as m
from module_into_module import saikat as s
muksadul1=m.muksadul(40,"sonapukur","bangladeshi")
mahabub1=m.mahabub(20,"dinajpur","british","islam")
saikat1=s(13,"rangpur","american","saudi","cantpublic")
muksadul1.all()
mahabub1.all()
saikat1.all()











