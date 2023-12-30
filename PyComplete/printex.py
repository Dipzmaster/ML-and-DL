# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:06:38 2021

@author: HP
"""

print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('Z\n')

w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')


print(10, 10**10)
print(11, 10**11)
print(12, 10**12)
print(13, 10**13)
print(14, 10**14)
print(15, 10**15)

print('{0} {1}'.format(0, 10**0))
print('{0} {1}'.format(1, 10**1))
print('{0} {1}'.format(2, 10**2))
print('{0} {1}'.format(3, 10**3))
print('{0} {1}'.format(4, 10**4))
print('{0} {1}'.format(5, 10**5))


print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))


x = '''
string that goes on
for three lines!
'''
print(x)
#This is a multi-line

x = '''
A cube has 8 corners:
7------8
/| /|
3------4 |
| | | |
| 5----|-6
|/ |/
1------2
'''
print(x)