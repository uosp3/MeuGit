from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),
    path('investidores/', include('investidores.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Configuração de URL para o projeto principal.

A lista `urlpatterns` encaminha URLs para visualizações. Para mais informações, consulte:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
Exemplos:
Função visualizações
1. Adicione uma importação: from my_app import views
2. Adicione uma URL para urlpatterns: path('', views.home, name='home')
Visualizações baseadas em classe
1. Adicione uma importação: from other_app.views import Home
2. Adicione uma URL para urlpatterns: path('', Home.as_view(), name='home')
Incluindo outro URLconf
1. Importe a função include(): from django.urls import include, path
2. Adicione uma URL para urlpatterns: path('blog/', include('blog.urls'))
"""
