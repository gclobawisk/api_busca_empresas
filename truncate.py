from models.database import Database
from env_config import *
import os

def truncate_reset_auto_increment(tabela):
    conexao = db
    conexao.execute_main_query('DELETE FROM {}'.format(tabela))
    conexao.execute_main_query(' ALTER TABLE {} AUTO_INCREMENT = 1'.format(tabela))


db = Database()

# APAGAR TODOS OS REGISTROS DA TABELA E RESETAR O ÍNDICE DO ID AUTO INCREMENT
retorno_zerar_tabela = truncate_reset_auto_increment("atividades_secundarias")
print('retorno_zerar_tabela atividades_secundarias: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("atividade_principal")
print('retorno_zerar_tabela atividade_principal: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("empresas")
print('retorno_zerar_tabela empresa: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("socios")
print('retorno_zerar_tabela socios: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("contatos")
print('retorno_zerar_tabela contatos: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("enderecos")
print('retorno_zerar_tabela enderecos: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("anexos_solicitacoes_gerenciar_empresa")
print('retorno_zerar_tabela anexos_solicitacoes_gerenciar_empresa: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("mensagens")
print('retorno_zerar_tabela mensagens: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("respostas_mensagens")
print('retorno_zerar_tabela respostas_mensagens: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("solicitacoes_gerenciar_empresa")
print('retorno_zerar_tabela solicitacoes_gerenciar_empresa: {}'.format(retorno_zerar_tabela))

retorno_zerar_tabela = truncate_reset_auto_increment("usuarios_empresas")
print('retorno_zerar_tabela usuarios_empresas: {}'.format(retorno_zerar_tabela))








