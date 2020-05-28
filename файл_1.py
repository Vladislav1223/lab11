spisok = []
spisok1=[]
print('Исходный файл')
f=open('f.txt', 'r')
print(f.read())
with open('f.txt', 'r') as filehandle:# откроем файл и считаем его содержимое в список
    for i in filehandle:
        count = i[:-1]# удалим заключительный символ перехода строки
        spisok.append(count)# добавим элемент в конец списка
for i in reversed(spisok):
    spisok1.append(i) #Перевернем наши элементы списка в обратном порядке
#Откроем другой файл и запишем туда элементы нашего списка
with open('g.txt', 'w') as filehandle:  
    for i in spisok1:
        filehandle.write('%s\n' % i)
print('Перезаписанные данные в другой файл')
g=open('g.txt', 'r')
print(g.read())



