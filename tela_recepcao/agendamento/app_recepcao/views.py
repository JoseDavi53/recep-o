from django.shortcuts import render, redirect
from .models import Pessoa  # Importe o modelo que você criou

def index(request):
    return render(request, 'index.html')

def salvar(request):
    if request.method == 'POST':
        # Criando o objeto com os dados do formulário HTML
        nova_pessoa = Pessoa()
        nova_pessoa.primeiro_nome = request.POST.get('primeiro_nome')
        nova_pessoa.sobrenome = request.POST.get('sobrenome')
        nova_pessoa.data_nascimento = request.POST.get('data_nascimento')
        nova_pessoa.tipo_usuario = request.POST.get('tipo_usuario')
        
        # Salva no MySQL
        nova_pessoa.save()
        
        # Redireciona para a página de sucesso
        return render(request, 'sucesso.html')
    
    return render(request, 'index.html')

def sucesso(request):
    return render(request, 'sucesso.html')

def sorteio(request):
    return render(request, 'sorteio.html')