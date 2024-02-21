#list type data ninnoy
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
print(li)
#ata kon type data ta ninnoy
li=[Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
print(type(li))
#list data mutable(poriborton hoy)
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li[2]='Hablu'
print(li)
'''jekono type data ke list a rupantor kora jay
jemon:integer,float,chracter,complex,boolian etc'''
#list item access
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
print(li[3])
#list item changes
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li[2]='mahafuj'
print(li)
'''list a kono item add korar jonno
append oo insert mathod use kora hoy'''
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li.append('sagor')
print(li)
#insert method use kore
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li.insert(1,'Alam')
print(li)
#list a kono item remove korar jonno
#remove method use kore kono item ke badh dewa
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li.remove('Mahim')
print(li)
#pop method use kore kono item ke badh dewa
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li.pop(1)
print(li)
#clear method use kore kono item ke badh dewa
li=['Mahabub','Bishal','Saikat','Shahadat','Mahim','shuvo','Alif','Hamim']
li.clear()
print(li)