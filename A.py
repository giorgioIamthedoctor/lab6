'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
inp = open("input.txt","r")
wr = open("output.txt","w")
s = list(inp.readlines())
ns = list(map(int,s[1].split(" ")))
for i in range(int(s[0])):
  if ns.count(ns[i]) == 2:
    wr.write(str(ns[i]))
    wr.close()
    inp.close()
    break
  if ns.count(ns[int(s[0])-1-i]) == 2:
    wr.write(str(ns[int(s[0])-1-i]))
    wr.close()
    inp.close()
    break
