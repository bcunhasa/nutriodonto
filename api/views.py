from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.serializers import *
from administracao.models import *


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
            user = token.user
            cliente = Cliente.objects.get(usuario=user.id)
            
            response.update(token=token.key)
            response.update(mensagem='Usuário autenticado com sucesso.')
            response.update(usuario=user.id)
            response.update(perfil=cliente.id)
            response.update(username=user.username)
            response.update(sucesso=True)

        return Response(response)


class CargaInicialAPIView(generics.ListAPIView):
    """View para retornar os dados para o carregamento inicial"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer
