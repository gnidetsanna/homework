
'''

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self, restaurant_name, cuisine_type):
        print(restaurant_name,cuisine_type)

    def open_restaurant(self):
        print('Restourant', self.restaurant_name, 'is open')


my_restourant = Restaurant('Cake','Ukrainian')

print(my_restourant.restaurant_name)

my_restourant.open_restaurant()






def print_human(**an):
    for key in an:
        print(key , '=', an[key])

print(print_human(name = 'asas',surname = 'sdfsf'))


custom_get: ({
    'a':'value1',
    'b':'value2'
})



def custom_dic (dictionary, key):
    try:
        return (dictionary[key])
    except KeyError:
        raise ZeroDivisionError

import os

#def read_file(File.txt):
#    File.txt = open(File.txt, 'r')
#    line = str()
#    for line in File.txt:
#        print(line, end='')

#if __name__ == '__main__':
#    read_file(os.path.join('File.txt','/Users/macuser/PycharmProjects/homework/File.txt'))


import math

def add(a, b):
    return a + b

def div(a, b):
    return a/b

obj = {
    '+':add,
    '-':div
}

def user_input():
    a = float(input('>>>:'))
    oper = input(' '.join([oper for oper in obj.keys()]))
    b = float(input('>>>'))
    return {
        'first':a,
        'oper': oper,
        'second': b
    }

def write_text_to_file (File.txt,text):
    File.txt = open(File.txt, 'w')
    File.txt.write(text)
    File.txt.close()


def main():
    try:
       user_data = user_input()
       result_number = obj[user_data['oper']](user_data['first'],user_data['second'])
       result_str = '{first} {oper} {second}={result}'.format(first=user_data['first'],oper=user_data['oper'],second=user_data['second'],result=result_number)
    except ZeroDivisionError as e:
        result_str = e
    filename = os.path.join('/Users/macuser/PycharmProjects/homework/File.txt')
    write_text_to_file(File.txt=File.txt, text=result_str)
    print(result_str)



import os

def count_char_into_file(file, char):
    with open(file) as f:
        text = f.read()
        count = 0
        for elem in f.read():
            if elem == char:
                count = count + 1
    return count

print(count_char_into_file('/Users/macuser/PycharmProjects/homework/File.txt', 'A'))




def list_set(list_1,list_2):
  #  new_list = []
 #   for i in list_1:
  #      if i in list_2:
   #         new_list.append(i)
    #        return new_list

    return [i for i in list_1 if i in list_2]


print(list_set([1,2,3],[1,2,4,5]))



class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self, restaurant_name, cuisine_type):
        print(restaurant_name,cuisine_type)

    def open_restaurant(self):
        print('Restourant', self.restaurant_name, 'is open')


my_restourant = Restaurant('Cake','Ukrainian')

print(my_restourant.restaurant_name)

my_restourant.open_restaurant()



class Person():

    def __init__(self,name,age,food=[]):
        #if age < 18:
         #   raise ValueError
        self.name = name

        self.age = age

        self.food = food


    def age_check(self):
        if self.age >= 18:
            return True
        else:
            return False

    def vegetarian_check(self):
        if 'meat' in self.food:
            return False
        else:
            return True



t = Person('John',17,['cola'])
#print(t.age_check())

Masha = Person('Masha',10,['sprite','meat','apple'])
Kolya = Person('Kolya',19,['fanta','meat'])
Seryi = Person('Seryi',18)

list_human = [t,Masha,Kolya,Seryi]

new_list = []

for elem in list_human:
    if elem.age_check():
        new_list.append(elem)
    else:
        False
print(new_list)


print(Masha.vegetarian_check())

veg_list = []
for elem in list_human:
    if elem.vegetarian_check() == False:
        veg_list.append(elem)

print(veg_list)




def join_srt(string):
     import re
     return ' '.join(re.findall('[A-Z][^A-Z]*', string))

print(join_srt('MyWorldIsGood'))



import random

class Human():
     def __init__(self,name='', age=10, znak_zodiaca =''):
          self.name = name
          self.age = age
          self.znak_zodiaca = znak_zodiaca

     def __str__(self):
          return '{} {} {}'.format(self.name, self.age, self.znak_zodiaca)

     def __eq__(self, other):
          return self.name == other.name and self.age == other.age

     def __add__(self,other):
          if self.age >= 18 and other.age >= 18:
               new_name = self.name + ' ' + other.name
               new_age = 0.1
               znak_zodiaca_list = [
                    'стрелец',
                    'овен',
                    'рак',
                    'близнецы',
                    'весы'
               ]
               new_znak = random.choice(znak_zodiaca_list)
               return Human(name=new_name, age=new_age, znak_zodiaca= new_znak)
          else:
               raise ValueError('Errorrr!')




def main():
     alex = Human(name='Alex',age=32,znak_zodiaca = 'strelets')
     olya = Human(name='Olya', age=25, znak_zodiaca='oven')
     olya1 = Human(name='Olya', age=25, znak_zodiaca='bliznetsu')
     new_human = alex+olya1
     print(new_human)
     print(olya == olya1)

main()



class Book:
     def __init__(self,title='', price=0,list_of_comment=[],text=''):
          self.title = title
          self.price = price
          self.list_of_comment = list_of_comment
          self.text = text

     def __str__(self):
          return '{} {} len of comments -{}\n'.format(self.title, self.price, len(self.list_of_comment))


def main():
     book1 = Book(title='title1', price=100, text=" BlaBlaBla")
     book2 = Book(title='title2', price=450, text="BLKFLKDL")
     book_list = [book1,book2]
     for number,book in enumerate(book_list):
          print(number+1, '\t', Book.title)
     print(book1,book2)


if __name__ == '__main__':
    main()


import os

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    if n in range(2,11):
          if len(arr) in range(-100,101):
               k = sorted(set(arr))
               print(k[-2])


python_students = []
for _ in range(2 < int(input()) < 5):
        name = input()
        score = float(input())
        k = [name,score]
        python_students.append(k)
print(python_students)

from __future__ import print_function
score_list = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
print(new_list)
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")




class Animal:
    def __init__(self):
        self.can_fly = False
        self.can_run = False

    def print_abilities(self):
        print(self.__class__.__name__)
        print('Can flyL', self.can_fly)
        print('Can run:', self.can_run)
        print()

class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True

class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Pegasus(Horse,Bird):
    pass

def main():
    bird = Bird()




if __name__ == '__main__':
    main()


import datetime
class Product:
    def __init__(self, price, is_sale):
        self.price = price
        self.is_sale = is_sale
        self.is_publish = datetime.datetime.now


class Laptop(Product):

    def __init__(self, brand, color, model,**kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.color = color
        self.model = model



laptop_1 = Laptop(price = 3000, is_sale = False, brand = 'Lenovo', model='g50',color='white')


print(laptop_1.is_sale)




arr = []
for i in range(int(input())):
    s = input().split()
    for i in range(1, len(s)):
        s[i] = int(s[i])

    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1], s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print (arr.index(s[1]))
    elif s[0] == "count":
        print (arr.count(s[1]))
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print(arr)



def print_full_name(a, b):

    if len(first_name)<10 and len(last_name)<10:
        print ("Hello ", first_name,' ', last_name,"! You just delved into python.",sep='')


if __name__ == '__main__':
    first_name = input().strip()
    last_name = input().strip()
    print_full_name(first_name, last_name)



import os

def file_read (File):
    file = open(File,'r')
    for line in file:
        print(line)
    file.close()

file_read('/Users/macuser/PycharmProjects/homework/File.txt')

import os


text = 'Bitch'
def file_write (File,text):
    file = open(File,'w')
    file.write(text)
    file.close()

if __name__ == '__main__':
    file_write('/Users/macuser/PycharmProjects/homework/File.txt',text)
'''
import datetime


def calc_result(res):
    list_of_oper = []
    list_of_oper.append(res)
    time = datetime.datetime.now()
    print(list_of_oper,'\n',time)

calc_result('2+1=5')