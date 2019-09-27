
"""class Restaurant():

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

#def read_file(File):
#    File = open(File, 'r')
#    line = str()
#    for line in File:
#        print(line, end='')

#if __name__ == '__main__':
#    read_file(os.path.join('File','/Users/macuser/PycharmProjects/homework/File'))


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

def write_text_to_file (File,text):
    File = open(File, 'w')
    File.write(text)
    File.close()


def main():
    try:
       user_data = user_input()
       result_number = obj[user_data['oper']](user_data['first'],user_data['second'])
       result_str = '{first} {oper} {second}={result}'.format(first=user_data['first'],oper=user_data['oper'],second=user_data['second'],result=result_number)
    except ZeroDivisionError as e:
        result_str = e
    filename = os.path.join('/Users/macuser/PycharmProjects/homework/File')
    write_text_to_file(File=File, text=result_str)
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

print(count_char_into_file('/Users/macuser/PycharmProjects/homework/File', '.'))

"""



import os

def file_finder  (File,text):
    File = open(File, 'w')
    File.write(text)
    File.close()
