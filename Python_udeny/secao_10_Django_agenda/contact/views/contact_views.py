from django.core.paginator import Paginator  # type: ignore
from django.db.models import Q  # type: ignore
from django.shortcuts import get_object_or_404, redirect, render  # type:ignore

from contact.models import Contact  # type: ignore


def index(request):  # barra invertida quebra a linha.
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',  # o que será renderizado
        context,
    )


def search(request):  # barra invertida quebra a linha.
    search_value = request.GET.get('q', '').strip()  # strip limpa espaços

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')  # fatiamento, mostra de 10 em 10 começa em 10

    paginator = Paginator(contacts, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'search - ',
        'search_value': search_value,
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
