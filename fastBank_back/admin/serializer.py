from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'nomeSocial', 'data_nascimento', 'created_at', 'updated_at')

class ClientePFSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePF
        fields = ('cliente','cpf','rg')

class ClientePJSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePJ
        fields = ('cliente', 'cnpj', 'inscricaoEstadual', 'inscricaoMunicipal')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('logradouro','numero','bairro','cidade','uf','cep','complemento')

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ('cliente','telefone','email', 'observacao')

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ('cliente','agencia','numero','digito','saldo','limite','updated_at','ativa')

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ('conta','tipo', 'valor','destinatario','data')

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimento
        fields = ('conta', 'valor', 'prazo', 'saldoInvestido', 'local', 'finalizado')

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ('conta','valor','juros','data','aprovado','observacao')

class ParcelasSerializer(models.ModelSerializer):
    class Meta:
        model = Parcelas
        fields = ('emprestimo','vezes','valorParcela','dataPagamento','valorPago')
