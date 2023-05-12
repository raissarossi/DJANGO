from django.shortcuts import render
from rest_framework.response import responses
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import viewsets
from .models import *
from .serializer import *
import decimal

def obterIDByToken(token):
    pass

# class ClienteList(ListCreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer
#     #GET 
    # def list(self, request, *args, **kwargs):
    #     #LISTAR TODOS OS CLIENTES


    #     # QUEM FOI O AUTOR DO REQUEST???

    #     token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    #     print(token)
    #     dados = AccessToken(token)
    #     usuario = dados['user_id']
    #     print(usuario)

    #     #QUEM FEZ A REQUISIÇÃO FOI O ID 1


    #     return super().create(request, *args, **kwargs)
    # def get_queryset(self):
    #     queryset = Cliente.objects.all()
    #     resultado = queryset.filter(user=1)

    #     return super().get_queryset()

    # def create(self, request, *args, **kwargs):
    #     conta = Conta.objects.filter(cliente=1)
    #     for i in conta:
    #         if i.numero == request.data['numero']:
    #             if i.saldo > request.data['valor_transferencia']:
    #                 mov = Movimentacao()
    #                 mov.conta = i.id
    #                 mov.valor = request.data['valor_transferencia']
    #                 mov.save()

                    
    #                 gustavo = Conta.objects.get(numero=request.data['numero'])
    #                 gustavo.saldo += decimal(request.data['valor_transferencia'])
    #                 gustavo.save()

    #                 if gustavo is not None:
    #                     mov2 = Movimentacao()
    #                     mov2.conta = gustavo.id
    #                     mov2.save()
                    


                

    #     return super().create(request, *args, **kwargs)


# class ClienteDetail(RetrieveUpdateDestroyAPIView):

class ClienteListarDetalhar(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer



# class ClientePFList(ListCreateAPIView):
#     queryset = ClientePF.objects.all()
#     serializer_class = ClientePFSerializer
# class ClientePFDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ClientePF.objects.all()
#     serializer_class = ClientePFSerializer



# class ClientePJList(ListCreateAPIView):
#     queryset = ClientePJ.objects.all()
#     serializer_class = ClientePJSerializer
# class ClientePJDetail(RetrieveUpdateDestroyAPIView):
#     queryset = ClientePJ.objects.all()
#     serializer_class = ClientePJSerializer

    

# class EnderecoList(ListCreateAPIView):
#     queryset = Endereco.objects.all()
#     serializer_class = EnderecoSerializer
# class EnderecoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Endereco.objects.all()
#     serializer_class = EnderecoSerializer



# class ContatoList(ListCreateAPIView):
#     queryset = Contato.objects.all()
#     serializer_class = ContatoSerializer
# class ContatoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Contato.objects.all()
#     serializer_class = ContatoSerializer



class ContaList(ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
class ContaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer



class MovimentacaoList(ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
class MovimentacaoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer



class InvestimentoList(ListCreateAPIView):
    queryset = Investimento.objects.all()
    serializer_class = MovimentacaoSerializer
class InvestimentoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Investimento.objects.all()
    serializer_class = InvestimentoSerializer



class EmprestimoList(ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
class EmprestimoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer



class ParcelasList(ListCreateAPIView):
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer
class ParcelasDetail(RetrieveUpdateDestroyAPIView):
    queryset = Parcelas.objects.all()
    serializer_class = ParcelasSerializer
