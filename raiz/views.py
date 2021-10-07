from django.shortcuts import render, redirect, resolve_url # redirect usado para redirecionamento de pagina
from django.contrib import messages, auth # auth usado para chegem de usuario

# Chama um decoration que posibilitar o acesso so ao usuario logado
from django.contrib.auth.decorators import login_required

# Verificando a suplicidade de usuarios e email
from django.contrib.auth.models import User

from django.contrib.auth import logout

from .models import Contato, Categoria


def index(request):
    if request.method != 'POST':
        return render(request, 'index.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    dados = auth.authenticate(request, username=usuario, password=senha)

    if not dados:
        messages.error(request, 'Usuário ou senha incorretos.')
        return render(request, 'index.html')

    else:
        auth.login(request, dados)
        return redirect('home')


# Página de cadastro
def cadastro(request):
    # Retorna o formulario vazio se nada foi postado
    if request.method != 'POST':
        messages.info(request, 'NADA POSTADO')
        return render(request, 'cadastro.html')

    # Dados do novo usuario
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    confirmaSenha = request.POST.get('confirmaSenha')

    # Checagem se os campos estão preenchidos
    if not usuario or not senha or not confirmaSenha:   
        messages.warning(request, 'Todos os Campos são Obrigatórios')
        return render(request, 'cadastro.html')

    # Checagem se a senha é maior que 6 
    if len(senha) < 6:
        messages.warning(request, 'Senha necessita ter mais de seis caracteres')
        return render(request, 'cadastro.html')

    # Checagem de confirmação de senha
    if senha != confirmaSenha:
        messages.warning(request, 'Senhas não conferem')
        return render(request, 'cadastro.html')

    # Verificando se o usuário ja existe
    if User.objects.filter(username=usuario).exists():
        messages.warning(request, 'Nome de usuário já existe')
        return render(request, 'cadastro.html')
        
    messages.success(request, 'Usuário cadastrado com sucesso. Faça o login para acessar sua conta.')

    user = User.objects.create_user(username=usuario, password=senha)

    user.save()
    return redirect('index')


def sair(request):
    logout(request)
    return redirect('index')


# Página Deashbord 
@login_required(redirect_field_name='index')
def home(request):

    contatos = Contato.objects.filter(usuario=request.user)

    contesto = {
        'contatos': contatos
    }   

    return render(request, 'home.html', contesto)



@login_required(redirect_field_name='index')
def novoContato(request):
    if request.method != 'POST':
        return render(request, 'novoContato.html')

    nome = request.POST.get('nome')
    tel = request.POST.get('telefone')
    email = request.POST.get('email')
    categoria = Categoria(request.POST.get('cardes'))

    usuario = request.user

    contato = Contato.objects.create(nome=nome, telefone=tel, email=email, categoria=categoria, usuario=usuario )
        
    if contato:
        messages.success(request, 'Contato inserido com sucesso.')
        return redirect('novoContato')

    """if request.method != 'POST':
        form = FormContato()
        return render(request, 'novoContato.html', {'formulario': form})

    form = FormContato(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulario.')
        form = FormContato(request.POST)
        return render(request, 'novoContato.html', {'formulario': form})
    
    form.save()
    messages.success(request, 'Contatos salvo com sucesso.')
    return redirect('novoContato')"""