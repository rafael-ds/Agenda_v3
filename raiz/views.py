from django import forms
from django.shortcuts import get_object_or_404, render, redirect # redirect usado para redirecionamento de pagina
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


@login_required(redirect_field_name='index')
def sair(request):
    logout(request)
    return redirect('index')


# Página Deashbord 
@login_required(redirect_field_name='index')
def home(request):

    contatos = Contato.objects.filter(usuario=request.user)

    contesto = {

        'contatos': contatos,
        
    }   

    return render(request, 'home.html', contesto)


# Views de postagem de novo contato
@login_required(redirect_field_name='index')
def novoContato(request):
    if request.method != 'POST':
        return render(request, 'novoContato.html')

    nome = request.POST.get('nome')
    tel = request.POST.get('telefone')
    email = request.POST.get('email')
    categoria = Categoria(request.POST.get('cardes'))
    midias = request.POST.get('fotoContato')

    usuario = request.user

    contato = Contato.objects.create(nome=nome, telefone=tel, email=email, categoria=categoria, usuario=usuario, midias=midias, )
        
    if contato:
        messages.success(request, 'Contato inserido com sucesso.')
        return redirect('novoContato')

# Views mostra um unico contato
#contato_id --> argumento que indicado na na urls
@login_required(redirect_field_name='index')
def contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    contesto = {
        'contato': contato
    }

    return render(request, 'contato.html', contesto)


@login_required(redirect_field_name='index')
def busca(request):
    termo = request.GET.get('termo') # nome do campo de pesquisa

    contatos = Contato.objects.order_by('id').filter(
        # Obs: sem o __icontains nao ouve retorno
        usuario=request.user,
        nome__icontains=termo, 

    )

    return render(request, 'busca.html', {'contatos': contatos})


@login_required(redirect_field_name='index')
def delete(request, id):
    del_contato = Contato.objects.get(id=id)
    del_contato.delete()

    messages.success(request, 'Contato excluido com sucesso.')
    return redirect('home')


# Nao funcionando
"""@login_required(redirect_field_name='index')
def editar(request, id):
    post = get_object_or_404(Contato, id=id)

    form = Contato(instance=post)

    if(request.method == 'POST'):
        form = Contato(request.POST, instance=post)

        if(form.is_valid()):
            post = form.save(commite=False)

            post.nome = form.cleaned_data['nome']
            post.telefone = form.cleaned_data['telefone']
            post.email = form.cleaned_data['email']
            post.caategoria = form.cleaned_data['caategoria']

            post.save()

            return redirect('home')
        else:
            return render(request, 'editar.html', {'form': form, 'post':post})

    elif(request.method == 'GET'):
        return render(request, 'editar.html', {'form': form, 'post': post})"""