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
            form.save()
            return redirect('index')
    else:
        form = CursoForm() 
        dados = {
            'form': form,
        }
    return render(request, 'academico/cadastrar_curso.html', dados)
