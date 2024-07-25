# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy) - fica na memória, não vai para o bd
# Retorna o contato
contact = Contact(**fields)  # passar os nomes dos campos
contact.save()  # salva no bd
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')

'''
shell do django
PS E:\Cursos\MeuGit\Python_udeny\secao_10_Django_agenda> python manage.py shell

In [1]: from contact.models import Contact
dels.Contact

In [3]: variavel = Contact(first_name='Gustavo')

In [4]: variavel
Out[4]: <Contact: Gustavo >

In [5]: variavel.save()

In [7]: variavel.last_name = 'Moreira'

In [8]: variavel.save()

In [9]: variavel.phone = '1231231232'

In [11]: variavel.save()

In [12]: variavel.delete()
Out[12]: (1, {'contact.Contact': 1})

In [13]: variavel.save()

In [15]: variavel = Contact.objects.get(id=4)

In [16]: variavel
Out[16]: <Contact: Gustavo Moreira>

In [17]: variavel.first_name = 'Helena'

In [18]: variavel.save()

In [19]: variavel
Out[19]: <Contact: Helena Moreira>

In [20]: variavel.id
Out[20]: 4

In [21]: variavel.pk
Out[21]: 4

In [22]: variavel = Contact.objects.get(pk=4)

In [23]: variavel
Out[23]: <Contact: Helena Moreira>

In [24]: variavel = Contact.objects.all()

In [25]: variavel
Out[25]: <QuerySet [<Contact: João Miranda>, <Contact: Luiz Miranda>, <Contact: Helena Moreira>]>

In [27]: for contato in variavel: contato.first_name

In [28]: contato
Out[28]: <Contact: Helena Moreira>

In [29]: variavel = Contact.objects.all()

In [30]: for contato in variavel: contato.first_name

In [31]: variavel
Out[31]: <QuerySet [<Contact: João Miranda>, <Contact: Luiz Miranda>, <Contact: Helena Moreira>]>

In [32]: variavel = Contact.objects.filter(id=4)

In [33]: variavel
Out[33]: <QuerySet [<Contact: Helena Moreira>]>

In [34]: for contato in variavel: contato.first_name

In [35]: variavel = Contact.objects.all().filter(id=2)

In [36]: variavel
Out[36]: <QuerySet [<Contact: Luiz Miranda>]>

In [37]: variavel = Contact.objects.all().order_by('id')

In [38]: variavel
Out[38]: <QuerySet [<Contact: João Miranda>, <Contact: Luiz Miranda>, <Contact: Helena Moreira>]>

In [39]: variavel = Contact.objects.create(first_name='Edu', last_name=' 
    ...: Vieira')
'''
