#Write a program to identify the 3 words that occur most alongwith their frequency
#@author : Akshay

def freq(str):
    str = str.split()
    str2 = []

    for i in str:

        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


str = 'flower fruits flower vegetables vegetables flower vegetables fruits fruits'
freq(str)