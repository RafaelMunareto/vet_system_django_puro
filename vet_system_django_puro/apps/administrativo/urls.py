from django.urls import path
from .views import *

urlpatterns = [
    
    path('administrativo', estatica.listar, name='administrativo'),
   
    path('parceiros', parceiros.listar, name='parceiros'),
    path('parceiros/<int:id>', parceiros.detalhes, name='parceiros.detalhes'),
    path('parceiros/contatos/<int:id>', parceiros.contatos, name='parceiros.contatos'),
    path('parceiros/endereco/<int:id>', parceiros.endereco, name='parceiros.endereco'),
    path('parceiros/adicionar', parceiros.adicionar, name='parceiros.adicionar'),
    path('parceiros/editar/<int:id>', parceiros.editar, name='parceiros.editar'),
    path('parceiros/delete/<int:id>', parceiros.delete, name='parceiros.delete'),
    path('parceiros/store', parceiros.store, name='parceiros.store'),
    path('parceiros/put/<int:id>', parceiros.put, name='parceiros.put'),
    path('parceiros_export', parceiros.export, name='parceiros.export'),
    
    path('fornecedores', fornecedores.listar, name='fornecedores'),
    path('fornecedores/<int:id>', fornecedores.detalhes, name='fornecedores.detalhes'),
    path('fornecedores/contatos/<int:id>', fornecedores.contatos, name='fornecedores.contatos'),
    path('fornecedores/endereco/<int:id>', fornecedores.endereco, name='fornecedores.endereco'),
    path('fornecedores/bancario/<int:id>', fornecedores.bancario, name='fornecedores.bancario'),
    path('fornecedores/adicionar', fornecedores.adicionar, name='fornecedores.adicionar'),
    path('fornecedores/editar/<int:id>', fornecedores.editar, name='fornecedores.editar'),
    path('fornecedores/delete/<int:id>', fornecedores.delete, name='fornecedores.delete'),
    path('fornecedores/store', fornecedores.store, name='fornecedores.store'),
    path('fornecedores/put/<int:id>', fornecedores.put, name='fornecedores.put'),
    path('fornecedores_export', fornecedores.export, name='fornecedores.export'),
   
    path('produtos', produtos.listar, name='produtos'),    
    path('produtos/<int:id>', produtos.detalhes, name='produtos.detalhes'),
    path('produtos/associados/<int:id>', produtos.associados, name='produtos.associados'),
    path('produtos/adicionar_novo', produtos.adicionar_novo, name='produtos.adicionar_novo'),
    path('produtos/adicionar/<int:id>', produtos.adicionar, name='produtos.adicionar'),
    path('produtos/editar/<int:id>', produtos.editar, name='produtos.editar'),
    path('produtos/delete/<int:id>', produtos.delete, name='produtos.delete'),
    path('produtos/store', produtos.store, name='produtos.store'),
    path('produtos/put/<int:id>', produtos.put, name='produtos.put'),
    path('produtos_export', produtos.export, name='produtos.export'),
    
    path('estoque', estoque.listar, name='estoque'),    
    path('estoque/editar/<int:id>', estoque.editar, name='estoque.editar'),
    path('estoque/delete/<int:id>', estoque.delete, name='estoque.delete'),
    path('estoque/store', estoque.store, name='estoque.store'),
    path('estoque/put/<int:id>', estoque.put, name='estoque.put'),
    path('estoque_export', estoque.export, name='estoque.export'),

    path('servicos', servicos.listar, name='servicos'),    
    path('servicos/adicionar', servicos.adicionar, name='servicos.adicionar'),
    path('servicos/editar/<int:id>', servicos.editar, name='servicos.editar'),
    path('servicos/delete/<int:id>', servicos.delete, name='servicos.delete'),
    path('servicos/store', servicos.store, name='servicos.store'),
    path('servicos/put/<int:id>', servicos.put, name='servicos.put'),
    path('servicos_export', servicos.export, name='servicos.export'),

    path('pagamentos/<int:periodo>', pagamentos.listar, name='pagamentos'),    
    
    path('pagamentos_fornecedor/<int:id>/<slug:data>', pagamentos_fornecedor.listar, name='pagamentos_fornecedor'),    
    path('pagamentos_fornecedor/editar/<int:id>', pagamentos_fornecedor.editar, name='pagamentos_fornecedor.editar'),
    path('pagamentos_fornecedor_export', pagamentos_fornecedor.export, name='pagamentos_fornecedor.export'),
    path('pagamentos_fornecedor/put/<int:id>', pagamentos_fornecedor.put, name='pagamentos_fornecedor.put'),

    path('custos_fixos', custos_fixos.listar, name='custos_fixos'),    
    path('custos_fixos/adicionar', custos_fixos.adicionar, name='custos_fixos.adicionar'),
    path('custos_fixos/editar/<int:id>', custos_fixos.editar, name='custos_fixos.editar'),
    path('custos_fixos/delete/<int:id>', custos_fixos.delete, name='custos_fixos.delete'),
    path('custos_fixos/store', custos_fixos.store, name='custos_fixos.store'),
    path('custos_fixos/put/<int:id>', custos_fixos.put, name='custos_fixos.put'),
    path('custos_fixos_export', custos_fixos.export, name='custos_fixos.export'),

   
]
