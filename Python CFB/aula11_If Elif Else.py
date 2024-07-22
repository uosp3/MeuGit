a=10
b=5
res=0
op="+"

if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b
else:
    print("Operador invalido")

print("Operacao ",str(a)+op+str(b), " = ", res)

#AND
#       V V >>>> V
#       V F >>>> F
#       F V >>>> F
#       F F >>>> F

#OR
#       V V >>>> V
#       V F >>>> V
#       F V >>>> V
#       F F >>>> F
