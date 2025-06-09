from django.shortcuts import render
from .models import Aluno, Curso
from .forms import CursoForm, AlunoForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError


# Create your views here.


def index(request):
    return render(request, 'academico/index.html')


def alunos(request):
    query = request.GET.get('busca', '')
    if query:
        alunos = Aluno.objects.filter(ativo=True, nome__icontains=query)
    else:
        alunos = Aluno.objects.filter(ativo=True)
    dados = {
        'alunos': alunos,
        'ativos': True,
        'query': query,
    }
    return render(request, 'academico/lista_alunos.html', dados)


def alunos_inativos(request):
    query = request.GET.get('busca', '')
    if query:
        alunos = Aluno.objects.filter(ativo=False, nome__icontains=query)
    else:
        alunos = Aluno.objects.filter(ativo=False)

    dados = {
        'alunos': alunos,
        'ativos': False,
        'query': query
    }
    return render(request, 'academico/lista_alunos.html', dados)


def cursos(request):
    cursos = Curso.objects.all()
    dados = {
        'cursos': cursos,
    }
    return render(request, 'academico/lista_cursos.html', dados)


def cadastrar_aluno(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm()
        dados = {
            'form': form,
        }
    return render(request, 'academico/cadastrar_aluno.html', dados)


def cadastrar_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # is_valid() Vai validar os dados, o Tokken CSRF, e criar um
            # dicionário com os dados chamado cleaned_data
            # Aqui estamos pegando o nome do curso
            nome = form.cleaned_data['nome'].title()
            form.instance.nome = nome
            print(nome)
            form.save()
            return redirect('cursos')  # Redireciona para a lista de cursos
    else:
        form = CursoForm()
        dados = {
            'form': form,
        }
    return render(request, 'academico/cadastrar_curso.html', dados)


def editar_aluno(request, id):
    # aluno vai receber os dados do aluno selecionado.
    try:
        aluno = Aluno.objects.get(id=id)
    except:
        return redirect('alunos')

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    # form vai receber um formulário com os dados do aluno selecionado.
    form = AlunoForm(instance=aluno)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'aluno': aluno,
    }

    return render(request, 'academico/editar_aluno.html', dados)


def editar_curso(request, id):
    # cursos vai receber os dados do cursos selecionado.
    try:
        curso = Curso.objects.get(id=id)
    except:
        return redirect('cursos')

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')

    # form vai receber um formulário com os dados do cursos selecionado.
    form = CursoForm(instance=curso)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'curso': curso,
    }

    return render(request, 'academico/editar_curso.html', dados)


def excluir_curso(request, id):
    try:
        curso = Curso.objects.get(id=id)
        curso.delete()
    except:
        return redirect('cursos')

    curso = Curso.objects.all()
    dados = {
        'cursos': curso,
    }
    return render(request, 'academico/lista_cursos.html', dados)


def excluir_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
        aluno.ativo = False
        aluno.save()
        messages.success(request, "Aluno excluído com sucesso.")
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")

    return redirect('alunos')


def ativar_aluno(request, id):
    try:
        aluno = Aluno.objects.get(id=id)
    except Aluno.DoesNotExist:
        messages.error(request, "Aluno não encontrado.")
        return redirect('alunos_inativos')

    if aluno.ativo == False:
        aluno.ativo = True
        aluno.save()
        messages.success(request, "Aluno reativado com sucesso.")

    else:
        messages.info(request, "O aluno já está ativo.")

    return redirect('alunos_inativos')


ORDENACAO_ALUNOS_LOOKUP = {
    'curso': 'curso__nome',
    'nome': 'nome',
    'genero': 'genero',
    'escolaridade': 'escolaridade',
    'estado_civil': 'estado_civil',
    'data_nascimento': 'data_nascimento'
}


def ordenar_alunos(request, campo):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(campo)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=True)

    if busca:
        alunos = alunos.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {
        'alunos': alunos,
        'ativos': True,
        'query': busca,
    }
    return render(request, 'academico/lista_alunos.html', dados)


def ordenar_alunos_inativos(request, campo):
    campo_ordenacao = ORDENACAO_ALUNOS_LOOKUP.get(campo)
    busca = request.GET.get('busca', '')
    alunos = Aluno.objects.filter(ativo=False)

    if busca:
        alunos = Aluno.objects.filter(nome__icontains=busca)

    alunos = alunos.order_by(campo_ordenacao)
    dados = {
        'alunos': alunos,
        'ativos': False,
        'query': busca,
    }
    return render(request, 'academico/lista_alunos.html', dados)
