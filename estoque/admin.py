# Importando módulo de administração do Django
from django.contrib import admin

# Importando o modelo Produto do arquivo models.py
from .models import Produto

# Register your models here.
# Esta linha registra o modelo Produto no site de administração do Django
admin.site.register(Produto)
