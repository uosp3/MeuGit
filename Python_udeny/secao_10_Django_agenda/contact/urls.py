from django.urls import path

from contact import views

app_name = 'contact'  # para que os 'name' não conflitem se forem iguais
# no caso o 'name' da url se refere ao 'index' que está no template 'contact'
urlpatterns = [  # urls daqui devem ser referenciadas em 'urls.py' do 'project'
    path('<int:contact_id>/', views.contact, name='contact'),  # name da url
    path('', views.index, name='index'),  # name da url
]
