# https://www.knowprogram.com/python/star-pattern-python-for-loop/

def ractangle(n):
    for i in range(0,n):
        for j in range(0, n):
            print('*', end=' ')
        print()
# ractangle(4)

def ractangle1(n):
    for i in range(n):
        # printing stars
        print("* " * n)
# ractangle(5)

def triangle(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('* ', end='')
        print()
# triangle(5)

def reverse_triangle(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print('* ', end='')
        print()
# reverse_triangle(5)

def mirror_triangle(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print(' ',end=' ')
        for j in range(i+1):
            print('* ',end='')
        print()
# mirror_triangle(5)

def short_mirror_triangle(n):
   for i in range(1, n+1):
      # printing stars
      print(" " * (n-i) + "*" * i)
# short_mirror_triangle(5)

def piramid(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print(' ',end='')
        for j in range(i+1):
            print(' *',end='')
        print()
# piramid(5)

def short_piramid(n):
   for i in range(n):
      # printing stars
      print(" " * (n-i-1) + "*" * (2*i+1))
# short_piramid(5)

def reverse_piramid(n):
    for i in range(n, 0, -1):
        for j in range(n-i, 0 ,-1):
            print(' ',end='')
        for j in range(i, 0, -1):
            print(' *',end='')
        print()
# reverse_piramid(5)

def reverse_mirror_triangle(n):
    for i in range(n, 0, -1):
        for j in range(n-i, 0 ,-1):
            print(' ',end=' ')
        for j in range(i, 0, -1):
            print(' *',end='')
        print()
# reverse_mirror_triangle(5)

def pattern_(n):
   # print upper triangle
   for i in range(n):
      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print("\r")
      
   # print lower triangle
   for i in range(n):
      for j in range(n-i-1):
         # printing stars
         print("* ",end="")
      print("\r")

def short_pattern_(n):
   for i in range(n):
      print('* ' * (i + 1))
   for i in range(n):
      print('* ' * (n - i - 1))

def pattern(n):
   # print upper triangle
   for i in range(n):
      for j in range(n-i-1):
         # printing spaces
         print(" ", end=" ")

      for j in range(i+1):
         # printing stars
         print("* ",end="")
      print()

   # print lower triangle
   for i in range(n-1):
      for j in range(i+1):
         # printing spaces
         print(" ",end=" ")

      for j in range(n-i-1):
         # printing stars
         print("* ",end="")
      print()
    
def dimaond(n):
   # print upper pyramid
   for i in range(n):
      for j in range(n-i-1):
         print(" ", end="")
      for j in range(2*i+1):
         # printing stars
         print("*", end="")
      print()

   # print downward pyramid
   for i in range(n-1):
      for j in range(i+1):
         print(" ", end="")
      for j in range(2*(n-i-1)-1):
         # printing stars
         print("*", end="")
      print()