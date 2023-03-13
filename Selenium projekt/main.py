# from datetime import date
#
# today = date.today()
#
# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)
#
# # Textual month, day and year
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)
#
# # mm/dd/y
# d3 = today.strftime("%m/%d/%y")
# print("d3 =", d3)
#
# # Month abbreviation, day and year
# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)

import json
# x = {"A": 1, "B":11,"C":111,"D":2,"E":22,"F":222,"G":3,"H":33,"I":333,"J":4,"K":44,"L":444,"M":5,"N":55,"O":555,"P":6,'\
#     '"Q":66, "R":666,"S":7,"T":77,"W":777,"U":8,"V":88,"x":9,"Y":99,"Z":999}
# slowo = input("podaj słowo : ")
# d_slowo = slowo.upper()
# li = list(d_slowo)
# result = ''
# for i in li:
#     result += str(x[i])
# print(result)


# li = int(input("podaj iczbe :"))
# m=4
# n=1
#
# for i in range(1, li+1):
#     print( m* " " +"^"*n)
#     m=m-1
#     n=n+2

from datetime import datetime

local = datetime.now()
print(local.strftime("%d/%m/%Y, %H:%M:%S"))
# 02/12/2020, 23:56:01



