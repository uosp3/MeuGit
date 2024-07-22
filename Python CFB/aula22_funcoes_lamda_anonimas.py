soma=lambda a,b:a+b
mult=lambda a,b,c:(a+b)*c
print(soma(2,5))
print(mult(2,5,3))

#outra opção
print((lambda a,b:a+b)(3,2))

#num função dentro da lambda
r=lambda x,func:x+func(x)
res=r(2, lambda x:x*x)
print(res)
res=r(2, lambda x:x+3)
print(res)