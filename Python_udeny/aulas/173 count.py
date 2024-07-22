#https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/34734412#questions
from itertools import count

c1=count()
c2=count(10, 3)# 10 indica o ínicio da contagem e 3 é o passo

print(next(c1))
print(next(c1))
print(next(c1))

for i in c1:
    if i > 100:
        break
    print(i)
