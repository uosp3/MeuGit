
from django.urls import path  # type: ignore

from contact import views

app_name = 'contact'  # para que os 'name' não conflitem se forem iguais
# no caso o 'name' da url se refere ao 'index' que está no template 'contact'
urlpatterns = [  # urls daqui devem ser referenciadas em 'urls.py' do 'project'
    path('', views.index, name='index'),  # name da url
    path('search/', views.search, name='search'),  # name da url

    # contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),  # name da url
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # user
    path('user/create/', views.register, name='register'),  # name da url
    path('user/login/', views.login_view, name='login'),  # name da url
    path('user/logout/', views.logout_view, name='logout'),  # name da url
    path('user/update/', views.user_update, name='user_update'),  # name da url
]
