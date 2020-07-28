#если введенное число больше 7, то вывести “Привет”
def addNumber(value):

    if (value < 7):
        print('Число меньше 7')

    elif (value == 7):
        print ('число равно 7')

    else:
        print('Привет')

#если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"
def addName(name):
    if (name == 'Вячеслав'):
        print('Привет, Вячеслав')

    else:
        print('Нет такого имени')

#на входе есть числовой массив, необходимо вывести элементы массива кратные 3
def addCount():
    array = [0,0,0,0,0]
    print("Введите 5 чисел")
    for i in range(5):
        array[i]=int(input())
    print('Числа кратные 3')
    for i in range(5):
        if (array[i] % 3 == 0 and array[i] != 0 ):
            print(array[i])

# Вызывается функция по заданию 1
print ("Введите число")
number = int(input())
addNumber(number)

# Вызывается функция по заданию 2
print ("Введите имя")
name_1 = input()
addName(name_1)

# Вызывается функция по заданию 3
addCount()

# Скобочная последовательность, дополнительное задание
stri= '[((())()(())]]'
par = 0
col = 0
cha = 0

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

for i in stri:
    if ( '{' in stri):
        cha += 1
        count_1 += 1
    elif ( '}' in stri):
        cha -= 1
        count_2 += 1

    if ('[' in stri):
        col += 1
        count_3 += 1
    elif ( ']'in stri):
        col -= 1
        count_4 += 1

    if ( '('in stri):
        par += 1
        count_5 += 1
    elif (')' in stri):
        par -= 1
        count_6 += 1

if (cha < 0 or col < 0 or par < 0):
    print('Задана не правильная последовательность [((())()(())]] <br \/>')
elif (cha != 0 or col != 0 or par != 0):
    print('Задана не правильная последовательность [((())()(())]] <br \/>')
else:
    print('правильная ');
if (count_3 != count_4 and count_3 > count_4):
    print('необходимо добавить [ ')
else:
    print('необходимо добавить ]')

if (count_1 != count_2 and count_1 > count_2):
    print('необходимо добавить  } ')
elif (count_1 == count_2 and count_1 < count_2):
    print('необходимо добавить { ')
else:
    print('таких символов вообще нет в данной последоватеельности {} ')
if (count_5 != count_6 and count_5 > count_6):
    print('необходимо добавить ) ')
elif (count_5 == count_6 and count_5 < count_6):
    print('таких символов вообще нет в данной последоватеельности () ')
else:
    print('необходимо добавить ( ')

