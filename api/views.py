from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.serializers import *
from administracao.models import *
from gerencia.models import *


class ClienteAutenticacaoAPIView(ObtainAuthToken):
    """Autentica um usuário"""
    def post(self, request, *args, **kwargs):
        response = {
            'sucesso': False,
            'mensagem': ''
        }
        authentication = super(ClienteAutenticacaoAPIView, self).post(request, *args, **kwargs)

        # Define o conteudo da resposta em caso de autenticacao com sucesso
        if authentication.status_code == status.HTTP_200_OK:
            token = Token.objects.get(key=authentication.data['token'])
            response.update(token=token.key)
            response.update(sucesso=True)

        return Response(response)


class CargaInicialAPIView(generics.ListAPIView):
    """View para retornar os dados para o carregamento inicial"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer


class AtualizaAlunoAPIView(generics.UpdateAPIView):
    """View para editar os dados do perfil de um cliente"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


# URLs para o exemplo dado no curso de Ionic

class NoticiasAPIView(generics.ListAPIView):
    """Lista todas as notícias"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class CriaNoticiaAPIView(generics.CreateAPIView):
    """Cria uma nova notícia"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class AtualizaNoticiaAPIView(generics.UpdateAPIView):
    """Atualiza uma notícia"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
