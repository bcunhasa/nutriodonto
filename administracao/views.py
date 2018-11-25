from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from .models import *
from .forms import *


class IndexView(View):
    """Página inicial do site"""
    
    def get(self, request):
        return render(self.request, 'administracao/index.html')


class LoginRequired(LoginRequiredMixin):
    """Configurações para o login"""
    login_url = 'administracao/login/'
    redirect_field_name = 'next'


class LoginView(View):
    """Página para a autenticação do usuário"""
    
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(self.request, 'administracao/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(username=username, password=password)
        
        try:
            if username != 'sadoadmin':
                request.user.administrador
            
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect(reverse('administracao:visao_geral'))
            else:
                context = {'form': form}
                return render(self.request, 'administracao/login.html', context)
        except:
            context = {'form': form}
            return render(self.request, 'administracao/login.html', context)


class LogoutView(View):
    """Página para logout do usuário"""
    
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('administracao:index'))


class VisaoGeralView(LoginRequired, View):
    """Página de visão geral do site de administração"""
    
    def get(self, request):
        campanhas = Campanha.objects.count()
        acoes = Acao.objects.count()
        escolas = Escola.objects.count()
        alunos = Aluno.objects.count()
        questionarios = Questionario.objects.count()
        exames = Exame.objects.count()
        
        context = {
            'pagina_visao_geral': True,
            'campanhas': campanhas,
            'acoes': acoes,
            'escolas': escolas,
            'alunos': alunos,
            'questionarios': questionarios,
            'exames': exames,
        }
        return render(self.request, 'administracao/visao_geral.html', context)


class GraficosView(LoginRequired, View):
    """Página que exibe gráficos baseados nos dados já coletados"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        context = {'pagina_graficos': True, 'questionarios': questionarios}
        return render(self.request, 'administracao/graficos.html', context)


class UsuariosView(LoginRequired, View):
    """Página que lista os usuários cadastrados no sistema"""
    
    def get(self, request):
        usuarios = User.objects.order_by('-id')
        context = {'pagina_usuarios': True, 'usuarios': usuarios}
        return render(self.request, 'administracao/usuarios.html', context)


class CampanhasView(LoginRequired, View):
    """Página que lista as campanhas cadastradas no sistema"""
    
    def get(self, request):
        campanhas = Campanha.objects.order_by('-id')
        context = {'pagina_campanhas': True, 'campanhas': campanhas}
        return render(self.request, 'administracao/campanhas.html', context)


class DetalhesCampanhaView(LoginRequired, View):
    """Página com as informações sobre uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(instance=campanha)
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/campanha.html', context)


class CriaCampanhaView(LoginRequired, View):
    """Cadastra as informações de uma nova campanha"""
    
    def get(self, request):
        form = CampanhaForm()
        context = {'pagina_campanhas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:campanhas'))
        context = {'pagina_campanhas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaCampanhaView(LoginRequired, View):
    """Altera as informações de uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(instance=campanha)
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        form = CampanhaForm(request.POST, request.FILES, instance=campanha)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:campanhas'))
        context = {'pagina_campanhas': True, 'campanha': campanha, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveCampanhaView(LoginRequired, View):
    """Remove uma campanha"""
    
    def get(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        context = {'pagina_campanhas': True, 'campanha': campanha}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, campanha_id):
        campanha = Campanha.objects.get(id=campanha_id)
        campanha.delete()
        return HttpResponseRedirect(reverse('administracao:campanhas'))


class AcoesView(LoginRequired, View):
    """Página que lista as ações cadastradas no sistema"""
    
    def get(self, request):
        acoes = Acao.objects.order_by('-id')
        context = {'pagina_acoes': True, 'acoes': acoes}
        return render(self.request, 'administracao/acoes.html', context)


class DetalhesAcaoView(LoginRequired, View):
    """Página com as informações sobre uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(instance=acao)
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/acao.html', context)


class CriaAcaoView(LoginRequired, View):
    """Cadastra as informações de uma nova ação"""
    
    def get(self, request):
        form = AcaoForm()
        context = {'pagina_acoes': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = AcaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:acoes'))
        context = {'pagina_acoes': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaAcaoView(LoginRequired, View):
    """Altera as informações de uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(instance=acao)
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        form = AcaoForm(request.POST, request.FILES, instance=acao)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:acoes'))
        context = {'pagina_acoes': True, 'acao': acao, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveAcaoView(LoginRequired, View):
    """Remove uma ação"""
    
    def get(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        context = {'pagina_acoes': True, 'acao': acao}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, acao_id):
        acao = Acao.objects.get(id=acao_id)
        acao.delete()
        return HttpResponseRedirect(reverse('administracao:acoes'))


class EscolasView(LoginRequired, View):
    """Página que lista as escolas cadastradas no sistema"""
    
    def get(self, request):
        escolas = Escola.objects.order_by('-id')
        context = {'pagina_escolas': True, 'escolas': escolas}
        return render(self.request, 'administracao/escolas.html', context)


class DetalhesEscolaView(LoginRequired, View):
    """Página com as informações sobre uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(instance=escola)
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/escola.html', context)


class CriaEscolaView(LoginRequired, View):
    """Cadastra as informações de uma nova escola"""
    
    def get(self, request):
        form = EscolaForm()
        context = {'pagina_escolas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = EscolaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:escolas'))
        context = {'pagina_escolas': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaEscolaView(LoginRequired, View):
    """Altera as informações de uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(instance=escola)
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        form = EscolaForm(request.POST, request.FILES, instance=escola)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:escolas'))
        context = {'pagina_escolas': True, 'escola': escola, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveEscolaView(LoginRequired, View):
    """Remove uma escola"""
    
    def get(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        context = {'pagina_escolas': True, 'escola': escola}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, escola_id):
        escola = Escola.objects.get(id=escola_id)
        escola.delete()
        return HttpResponseRedirect(reverse('administracao:escolas'))


class AlunosView(LoginRequired, View):
    """Página que lista os alunos cadastrados no sistema"""
    
    def get(self, request):
        alunos = Aluno.objects.order_by('-id')
        context = {'pagina_alunos': True, 'alunos': alunos}
        return render(self.request, 'administracao/alunos.html', context)


class DetalhesAlunoView(LoginRequired, View):
    """Página com as informações sobre um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(instance=aluno)
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/aluno.html', context)


class CriaAlunoView(LoginRequired, View):
    """Cadastra as informações de um novo aluno"""
    
    def get(self, request):
        form = AlunoForm()
        context = {'pagina_alunos': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:alunos'))
        context = {'pagina_alunos': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaAlunoView(LoginRequired, View):
    """Altera as informações de um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(instance=aluno)
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        form = AlunoForm(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:alunos'))
        context = {'pagina_alunos': True, 'aluno': aluno, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveAlunoView(LoginRequired, View):
    """Remove um aluno"""
    
    def get(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        context = {'pagina_alunos': True, 'aluno': aluno}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, aluno_id):
        aluno = Aluno.objects.get(id=aluno_id)
        aluno.delete()
        return HttpResponseRedirect(reverse('administracao:alunos'))


class QuestionariosView(LoginRequired, View):
    """Página que lista os questionários cadastrados no sistema"""
    
    def get(self, request):
        questionarios = Questionario.objects.order_by('-id')
        context = {'pagina_questionarios': True, 'questionarios': questionarios}
        return render(self.request, 'administracao/questionarios.html', context)


class DetalhesQuestionarioView(LoginRequired, View):
    """Página com as informações sobre um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(instance=questionario)
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/questionario.html', context)


class CriaQuestionarioView(LoginRequired, View):
    """Cadastra as informações de um novo questionário"""
    
    def get(self, request):
        form = QuestionarioForm()
        context = {'pagina_questionarios': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = QuestionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:questionarios'))
        context = {'pagina_questionarios': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaQuestionarioView(LoginRequired, View):
    """Altera as informações de um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(instance=questionario)
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        form = QuestionarioForm(request.POST, request.FILES, instance=questionario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:questionarios'))
        context = {'pagina_questionarios': True, 'questionario': questionario, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveQuestionarioView(LoginRequired, View):
    """Remove um questionário"""
    
    def get(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        context = {'pagina_questionarios': True, 'questionario': questionario}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, questionario_id):
        questionario = Questionario.objects.get(id=questionario_id)
        questionario.delete()
        return HttpResponseRedirect(reverse('administracao:questionarios'))


class ExamesView(LoginRequired, View):
    """Página que lista os exames cadastrados no sistema"""
    
    def get(self, request):
        exames = Exame.objects.order_by('-id')
        context = {'pagina_exames': True, 'exames': exames}
        return render(self.request, 'administracao/exames.html', context)


class DetalhesExameView(LoginRequired, View):
    """Página com as informações sobre um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(instance=exame)
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/exame.html', context)


class CriaExameView(LoginRequired, View):
    """Cadastra as informações de um novo exame"""
    
    def get(self, request):
        form = ExameForm()
        context = {'pagina_exames': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = ExameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:exames'))
        context = {'pagina_exames': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaExameView(LoginRequired, View):
    """Altera as informações de um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(instance=exame)
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        form = ExameForm(request.POST, request.FILES, instance=exame)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:exames'))
        context = {'pagina_exames': True, 'exame': exame, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveExameView(LoginRequired, View):
    """Remove um exame"""
    
    def get(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        context = {'pagina_exames': True, 'exame': exame}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, exame_id):
        exame = Exame.objects.get(id=exame_id)
        exame.delete()
        return HttpResponseRedirect(reverse('administracao:exames'))


class DiretoresView(LoginRequired, View):
    """Página que lista as os questionários para os diretores cadastradas no sistema"""
    
    def get(self, request):
        diretores = Diretor.objects.order_by('-id')
        context = {'pagina_diretores': True, 'diretores': diretores}
        return render(self.request, 'administracao/diretores.html', context)


class DetalhesDiretorView(LoginRequired, View):
    """Página com as informações sobre um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(instance=diretor)
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/diretor.html', context)


class CriaDiretorView(LoginRequired, View):
    """Cadastra as informações de um novo questionário para diretores"""
    
    def get(self, request):
        form = DiretorForm()
        context = {'pagina_diretores': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)
    
    def post(self, request):
        form = DiretorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:diretores'))
        context = {'pagina_diretores': True, 'form': form}
        return render(self.request, 'administracao/novo_elemento.html', context)


class EditaDiretorView(LoginRequired, View):
    """Altera as informações de um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(instance=diretor)
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)
    
    def post(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        form = DiretorForm(request.POST, request.FILES, instance=diretor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('administracao:diretores'))
        context = {'pagina_diretores': True, 'diretor': diretor, 'form': form}
        return render(self.request, 'administracao/edita_elemento.html', context)


class RemoveDiretorView(LoginRequired, View):
    """Remove um questionário para diretores"""
    
    def get(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        context = {'pagina_diretores': True, 'diretor': diretor}
        return render(self.request, 'administracao/remove_elemento.html', context)
        
    def post(self, request, diretor_id):
        diretor = Diretor.objects.get(id=diretor_id)
        diretor.delete()
        return HttpResponseRedirect(reverse('administracao:diretores'))
