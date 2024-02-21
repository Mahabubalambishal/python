#unpack tuple make kori
name=('mahabub','alam','bishal')
(a,b,c)=name
print(c)

#tuple ar vitorkar sokal man dekhar jonno
name=('mahabub','alam','bishal')
(*b,)=name
print(b)

#tuple ar vitor jekono akti ba duiti man dekhar jonno
name=('mahabub','alam','bishal','saikat','shahadat')
(a,d,*c)=name
print(c)


#akti item ar jonno unpack tuple
name=('Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim')
(a,b,c,d,e,f,g,h)=name
print(e)

#sokol item ar jonno unpack tuple
name=('Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim')
(*c,)=name
print(c)

#ak ar odhik item ke dekhar jonno unpack tuple
name=('Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim')
(a,b,*c)=name
print(c)