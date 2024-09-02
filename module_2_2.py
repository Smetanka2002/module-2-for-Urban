#2023/09/29 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first = 101
second = 125
third = 125
if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second or second == third or first == third:
    print(0)