from django.shortcuts import get_object_or_404, render  # type: ignore
from django.http import Http404

from contact.models import Contact  # type: ignore


def index(request):  # barra invertida quebra a linha.
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20]  # fatiamento, mostra de 10 em 10 começa em 10

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',  # o que será renderizado
        context,
    )


def contact(request, contact_id):  # barra invertida quebra a linha.
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',  # o que será renderizado
        context,
    )
