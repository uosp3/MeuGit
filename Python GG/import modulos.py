#import math - o import desta forma importa TODA a biblioteca
from math import sqrt # desta forma importa apenas o sqrt e diretamente para a pasta.
import random #necessário para gerar números aleatórios
import emoji
#https://www.webfx.com/tools/emoji-cheat-sheet/ site para emojis

num=random.randint(1,20)
#raiz=math.sqrt(num) - assim so funciona se tiver importado a biblioteca toda
raiz=sqrt(num) #assim so funciona se tiver importado apenas o sqrt.
print("A raiz quadrada de {} é {:.2f}".format(num,raiz))
print(emoji.emojize('Olá mundo :fox:'))
print(emoji.emojize("Ola, Mundo :sunglasses:"))