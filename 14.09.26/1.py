# s = ['aa', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
# s = 'aaaaassssaaaa'
# print(len(s))
# print(s.count('aa'))

# s = [1,2,3,4,5,6,7]
# print(max(s))
# print(min(s))
# print(sum(s))


# s = [0,3,8,5,7,3,7,3,2,5,6,8,45]

# s.sort()
# print(s)
# s.append(8)
# print(s)
# s.remove(7)
# print(s)
# s.reverse()
# print(s)

# s = 'aaaaaa fffff aaaaa'
# print(max(s, key=len))


# s = 'aaaaaaafffffff'
# s = s.replace('f','D', -2)
# print(s)


# from math import *
# a = 5.3
# print(int(a))
# print(round(a))
# print(ceil(a))


# s = input('введите слово')
# mas = []
# for i in s:
#     mas.append(i)
# print(mas)
# print(mas.reverse())
# if mas.reverse() == mas:
#     print(s)


# s = input('введите слово')
# if s[::-1] == s:
#     print(s)

# s = ['1', '2', '3', '4']
# print(s[::-1])




s = [11,21,13,2,12,2,3,1,2]
# print(s.count(1))
k = 0
for i in s:
    i = str(i)
    for j in i:
        print(j)
        if j == '1':
            k += 1
print(k)




