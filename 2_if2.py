"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str_1,str_2):
    if  isinstance(str_1,str)==False or  isinstance(str_2,str)==False: 
      return '0'
    elif str_1!=str_2:
      if len(str_1)>len(str_2):
        return '2'
      elif str_2=='learn':
        return '3'
    else:
      return '1'
      


if __name__ == "__main__":
    print(main('привет',"тест"))
    print(main(4,"learn"))
    print(main('learn','learn'))
    print(main('python',"learn_pytnon"))
    print(main('45','learn'))
