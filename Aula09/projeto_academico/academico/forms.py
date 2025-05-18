from django import forms
from .models import Curso, Aluno

# Formulário para Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso #Aqui vamos dizer que o formulário vai usar o modelo Curso
        fields = ['nome'] #Aqui vamos dizer quais campos do modelo Curso queremos usar no formulário

#Formulário para Aluno
class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Aluno #Aqui vamos dizer qual modelo esse formulário vai usar
        fields = ['nome', 'data_nascimento', 'cpf', 'genero', 'estado_civil', 'escolaridade', 'curso']
        #Aqui vamos dizer quais campos do modelo aluno queremos usar no formulário
