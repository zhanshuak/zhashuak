n1 = int (input ("введите нижний диапазон: "))
n2 = int (input ("введите верхний диапазон:"))
k = int (input ("Введите количество элементов:"))
sp = []
for i in range (k):

    sp.append (random.randrange(n1, n2))

print ("Вывод списка: ")

print (sp)

sp.sort ()

print ("Элементы отсортированы по возрастанию: ")

print (sp)

sp.sort (reverse = True)

print ("Элементы отсортированы по убыванию: ")

print (sp)
    
    
