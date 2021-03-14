#1
# liczby = [1,2,3,4,5,6,7,8,9,10]
# zbior1 = [1-x for x in liczby]
# print(zbior1)
#
# zbior2 = [4**y for y in range(8)]
# print(zbior2)
#
# zbior3 = [z for z in zbior2 if z % 2 == 0]
# print(zbior3)
#2
# import random
# losowe1 = []
# for x in range(9):
#     losowe1.append(random.randint(1, 30))
# print(losowe1)
# parzyste = [x for x in losowe1 if x % 2 == 0]
# print(parzyste)
#3
# produkty= {
# 'papier': 'sztuki',
# 'papierosy': 'sztuki',
# 'owoce': 'kg',
# 'sklejka': 'metry'}
# sztuki = [keys for keys, values in produkty.items() if values == 'sztuki']
# print(produkty)
# print(sztuki)


#4
# def prostokatny(x, y, z):
#     p = x + y + z
#     a_sym = p / 180
#     one = x * a_sym
#     two = y * a_sym
#     three = z * a_sym
#     if one and two or one and three or two and three == 90:
#         return "Trójkąt jest prostokątny"
#     elif one and two and three == 180:
#         return "Trójkąt jest prostokątny"
#     else:
#         return "Trójkąt nie jest prostokątny"
#
# print(prostokatny(2,3,4))
#5
# def trapez(a, b, h):
#     pole = ((a+b)*h)/2
#     print("Pole trapezu: ")
#     return pole
# print(trapez(2,5,7))
#6
# def ciag(a1=1, b=4, ile=10):
#     for i in range(ile):
#         a1 *= b
#     return a1
# print(ciag())
#7
# def ciag2(a1=1, b=4, ile=10):
#     a1 = (a1*b)**ile
#     return a1
# print(ciag2())
#8
# zakupy = {"papier": 12, "papierosy": 3, "harnaś": 7,"test ciazowy":9 }
# def lista(a):
#     b = 0
#     c = 0
#     for x in a.values():
#         b = b + x
#         c += 1
#     print('Cena to', b, "zł.\nWszyskich produktów jest: ")
#     return c
# print(lista(zakupy))
#9
from ciagi import arytmetyczne
from ciagi import geometryczne
