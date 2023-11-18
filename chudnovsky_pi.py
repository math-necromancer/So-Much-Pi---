#The Math Necromancer

#Implementation of the Chudnovsky
#ALgorithm for Computing π

#It's, like, the most cursed thing ever,
#and it takes years to derive, so it's best
#not to ask questions

#Source: https://en.wikipedia.org/wiki/Chudnovsky_algorithm

import decimal
import math
import SetPrecision

#Optimize the Algorithm via 'Binary Splitting'
def optimize(j, k):
     #The Chudnovsky algorithm is pretty cursed.
     if k == j + 1:
          P_jk = -(6 * j - 5) * (2 * j - 1) * (6 * j - 1)
          Q_jk = 10939058860032000 * j ** 3
          R_jk = P_jk * (545140134 * j + 13591409)
     elif j == 1 and k <= 1:
          #optimize(1, x x ∈ (-∞, 1]) sets up an infinite
          #recursion, so manually change the
          #parameters
          return optimize(1, 2)
     else:
          m = (j + k) // 2
          P_jm, Q_jm, R_jm = optimize(j, m)
          P_mk, Q_mk, R_mk = optimize(m, k)

          P_jk = P_jm * P_mk
          Q_jk = Q_jm * Q_mk
          R_jk = Q_mk * R_jm + P_jk * R_mk
     return P_jk, Q_jk, R_jk

def chudnovsky_pi(x):
     #Adding even more to the wierdness of this formula
     _C = 426880 * decimal.Decimal(10005).sqrt()
     P_x, Q_x, R_x = optimize(1, x)
     return (_C * Q_x) / (13591409 * Q_x + R_x)

_pi_iter = int(input("Yo Broseidon, Enter the number of Iterations\nfor this epic Formula!\n!Warning: It's pretty rad, but it is really slow!\n"))
precision = int(input("Yo yo yo, Broseph! You should enter the number of\ndecimal places to display!\n"))
_pi = SetPrecision.set_precision(chudnovsky_pi(_pi_iter), precision)
print("Yo bro, you won't believe this, The answer is...\n")
print(str(_pi) + "! Isn't that so Brotastic?\n")
print("Oh yeah Broseph, for reference, here the first 16 digits of pi!\n")
print("3.1415926535897931\n")