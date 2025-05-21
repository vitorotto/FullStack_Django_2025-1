from django.shortcuts import render
from .models import Aluno, Curso
from .forms import CursoForm, AlunoForm
from django.shortcuts import redirect

# Create your views here.


def index(request):
    return render(request, 'academico/index.html')


def alunos(request):
    alunos = Aluno.objects.all()
    dados = {
        'alunos': alunos,
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
            curso = form.cleaned_data['nome']
            print(curso)
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
