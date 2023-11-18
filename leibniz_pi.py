#The Math Necromancer

#Implementations of the Leibniz Formula
#for Computing π

#Source: Some dead guy from 1716

import decimal
import SetPrecision

def leibniz_pi(x):
     _pi = 1
     for i in range(1, x):
          #This Leibniz Formula is the special case that
          #arctan(1) = 1/4 π
          _pi += ((-1) ** i) / (2 * i + 1)
     _pi *= 4
     return _pi
_pi_iter = int(input("Yo yo yo, Broseph! Enter the number of Iterations\nfor this Epic Formula!\n!Warning: This series converges very slowly, so you'll need lots of terms!\n"))
precision = int(input("Yo, bro, now try inputting the number of\ndecimal places to be displayed!\n"))
_pi = SetPrecision.set_precision(leibniz_pi(_pi_iter), precision)
print("Yo bro, you won't believe this, The answer is...\n")
print(str(_pi) + "! Isn't that so Brotastic?\n")
print("Oh yeah Broseph, for reference, here the first 16 digits of pi!\n")
print("3.1415926535897931\n")