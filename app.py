import requests
import time
import re
from models.database import Database
from sendEmail.send import EmailSender
import json

def insertAtividadePrincipal(codigo_atividade_principal, id_empresa, cnpj):
    qryInsertAtividadePrincipal = f''' INSERT INTO atividade_principal
                                        (
                                            cnpj, fk_cnae_id, fk_empresa_id
                                        )
                                        VALUES
                                        (
                                            %s, %s, %s
                                        )
                                        '''

    try:
        # Executar o comando SQL para inserir os dados na tabela socios

        conexao = Database()
        codigo_tratado = codigo_atividade_principal.replace(".", "")
        codigo_tratado = codigo_tratado.replace("-", "")
        #print('Código Tratado: ', codigo_tratado)

        sql_get_id_cnae = f"SELECT id from cnaes where codigo = '{codigo_tratado}'"
        result_get_id_cnae = conexao.execute_main_query(sql_get_id_cnae)

        if len(result_get_id_cnae) > 0:
            cnae_id = result_get_id_cnae[0][0]
            #print ("encontrou o codigo cnae e o id é",cnae_id)
        else:
            #print ("nao encontrouuu:")
            cnae_id = 1358

        fk_empresa_id = id_empresa
        fk_cnae_id = cnae_id
        dados_atividade_principal = (cnpj, fk_cnae_id, fk_empresa_id)

        conexao.execSql(qryInsertAtividadePrincipal, dados_atividade_principal)

    except Exception as e:
        print("ERROR:", e)


def insertAtividadesSecundarias(codigo_atividade_secundaria, id_empresa, cnpj):
    qryInsertAtividadesSecundarias = f''' INSERT INTO atividades_secundarias
                                            (
                                                cnpj, fk_cnae_id, fk_empresa_id
                                            )
                                            VALUES
                                            (
                                                %s, %s, %s
                                            )
                                            '''

    try:
        # Executar o comando SQL para inserir os dados na tabela socios

        conexao = Database()
        codigo_tratado = codigo_atividade_secundaria.replace(".", "")
        codigo_tratado = codigo_tratado.replace("-", "")

        #print (f"código tratado atividade secundária: '{codigo_tratado}'")

        sql_get_id_cnae_atividade_secundaria = f"SELECT id from cnaes where codigo = {codigo_tratado}"
        result_get_id_cnae_atividade_secundaria = conexao.execute_main_query(sql_get_id_cnae_atividade_secundaria)

        if len(result_get_id_cnae_atividade_secundaria) > 0:
            cnae_id_atividade_secundaria = result_get_id_cnae_atividade_secundaria[0][0]
            #print(f"encontrou e o id é {cnae_id_atividade_secundaria}")
        else:
            cnae_id_atividade_secundaria = 1358

        fk_empresa_id = id_empresa
        fk_cnae_id = cnae_id_atividade_secundaria
        dados_atividades_secundarias = (cnpj, fk_cnae_id, fk_empresa_id)

        conexao.execSql(qryInsertAtividadesSecundarias, dados_atividades_secundarias)

    except Exception as e:
        print("ERROR:", e)


def insertSocios(nome_completo_socio, id_empresa, cnpj, tipo, qualificacao_socio):
    qryInsertSocios = f'''
                        INSERT INTO socios
                        (
                            nome_completo, id_empresa, cnpj_empresa, 
                            tipo, qualificacao_socio
                        )
                        VALUES
                        (
                            %s, %s, %s, %s,
                            %s
                        )
                        '''

    try:
        # Executar o comando SQL para inserir os dados na tabela socios
        conexao = Database()

        dados_socios = (nome_completo_socio, id_empresa, cnpj,
                        tipo, qualificacao_socio)

        conexao.execSql(qryInsertSocios, dados_socios)

    except Exception as e:
        print("ERROR:", e)


def insertContatos(email, telefone, id_empresa):
    qryInsertContatos = f'''
                            INSERT INTO contatos
                            (
                                email, telefone, fk_empresa_id
                            )
                            VALUES
                            (
                                %s, %s, %s
                            )
                            '''

    try:
        # Executar o comando SQL para inserir os dados na tabela socios
        conexao = Database()

        dados_contatos = ()
        dados_contatos = (email, telefone, id_empresa)

        conexao.execSql(qryInsertContatos, dados_contatos)

    except Exception as e:
        print("ERROR:", e)


def insertEnderecos(logradouro, numero, complemento, municipio, bairro, uf, cep, id_empresa):
    qryInsertEnderecos = f'''
                            INSERT INTO enderecos
                            (
                                logradouro, numero, complemento, municipio, bairro, uf, cep, fk_empresa_id
                            )
                            VALUES
                            (
                                %s, %s, %s, %s, %s, %s, %s, %s
                            )
                            '''

    try:
        # Executar o comando SQL para inserir os dados na tabela socios
        conexao = Database()

        dados_enderecos = ()
        dados_enderecos = (logradouro, numero, complemento, municipio, bairro, uf, cep, id_empresa)

        conexao.execSql(qryInsertEnderecos, dados_enderecos)

    except Exception as e:
        print("ERROR:", e)


def app(quantidade_consultas):
    conexao = Database()
    contador = 1
    arq = open("listacnpj.txt")
    linhas = arq.readlines()

    for linha in linhas:
        cnpj = linha.strip("\n")
        print(f"Consultando CNPJ: {cnpj}")
        try:
            #cnpj = '24936511000188' GABRIEL R.
            #cnpj = '27865757000102' GLOBO
            # Executar o comando SQL para inserir os dados na tabela
            conexao = Database()
            sql = f"SELECT razao_social from empresas where cnpj = {cnpj}"
            result = conexao.execute_main_query(sql)

            if len(result) > 0:
                print(f"CNPJ encontrado na Base de Dados:\n\t{result}\n")
                #time.sleep(2)
            else:
                # obtendo número máximo de CNPJ
                if contador >= quantidade_consultas:
                    break
                else:

                    data = obter_dados_empresa(cnpj)
                    razao_social = data['nome']
                    abertura = data['abertura']
                    situacao = data['situacao']
                    tipo = data['tipo']
                    porte = data['porte']
                    natureza_juridica = data['natureza_juridica']
                    logradouro = data['logradouro']

                    numero = data['numero']
                    municipio = data['municipio']
                    bairro = data['bairro']
                    uf = data['uf']
                    cep = data['cep']

                    telefone = data['telefone']
                    data_situacao = data['data_situacao']
                    motivo_situacao = data['motivo_situacao']
                    cnpj_com_mascara = data['cnpj']

                    ultima_atualizacao = data['ultima_atualizacao']
                    status = data['status']
                    fantasia = data['fantasia']
                    complemento = data['complemento']
                    email = data['email']
                    efr = data['efr']
                    situacao_especial = data['situacao_especial']
                    data_situacao_especial = data['data_situacao_especial']
                    capital_social = data['capital_social']

                    atividade_principal = data['atividade_principal']
                    atividades_secundarias = data['atividades_secundarias']
                    socios = data['qsa']

                    #print(f"Salvado na Base de Dados:")

                    qryInsert = f'''
                        INSERT INTO empresas
                        (
                            razao_social, fantasia, cnpj, abertura, situacao, tipo, porte, natureza_juridica,
                            ultima_atualizacao, status, efr, motivo_situacao, situacao_especial,
                            capital_social
                        )
                        VALUES 
                        (
                            %s, %s, %s, %s,
                            %s, %s, %s, %s,
                            %s, %s, %s, %s,
                            %s, %s
                        )
                        '''



                    # TRATAMENTO ABERTURA
                    if len(abertura) >= 8:
                        abertura = abertura[6:10] + "-" + abertura[3] + abertura[4] + "-" + abertura[0] + abertura[1]

                    dados = (razao_social, fantasia, cnpj, abertura, situacao, tipo, porte, natureza_juridica,
                             ultima_atualizacao, status, efr, motivo_situacao, situacao_especial,
                             capital_social)

                    try:
                        # Executar o comando SQL para inserir os dados na tabela
                        conexao.execSql(qryInsert, dados)



                    except Exception as e:
                        print("ERROR:", e)

                    conexao = Database()

                    #OBTENDO O ID DA EMPRESA
                    sql_get_id_cnpj = f"SELECT id from empresas where cnpj = {cnpj}"
                    result_get_id_empresa = conexao.execute_main_query(sql_get_id_cnpj)
                    id_empresa = result_get_id_empresa[0][0]


                    insertContatos(email, telefone, id_empresa)
                    insertEnderecos(logradouro, numero, complemento, municipio, bairro, uf, cep, id_empresa)

                    for key,value in data.items():
                        if key == "qsa":
                            if len(key) > 0:
                                #print("")
                                #print("\t\t\t| Socios |")
                                for socio in value:
                                    for key_socio, value_socio in socio.items():
                                        if key_socio == "nome":
                                            nome_completo_socio = value_socio
                                            #print (f"\t{nome_completo_socio}")
                                        if key_socio == "qual":
                                            qualificacao_socio = value_socio
                                            #print(f"\t{qualificacao_socio}")

                                            # Chamada da função Para inserir os Sócios
                                            insertSocios(nome_completo_socio, id_empresa, cnpj, tipo,qualificacao_socio)
                                    #print("")
                        elif key == "atividade_principal":
                            if len(key) > 0:
                                #print("")
                                #print("\t\t\t| Atividade Prinpipal |")

                                for atividade in value:
                                    for key_atividade, value_atividade in atividade.items():
                                        if key_atividade == "code":
                                            codigo_atividade_principal = value_atividade
                                            #print (f"\t{codigo_atividade_principal}")
                                            insertAtividadePrincipal(codigo_atividade_principal, id_empresa, cnpj)

                                        # if key_atividade == "text":
                                        #     descricao_atividade_principal = value_atividade
                                            #print(f"\t{descricao_atividade_principal}")

                                            # Chamando a função para inserir na tabela Atividade Principal
                                            #insertAtividadePrincipal(codigo_atividade_principal, id_empresa, cnpj)

                        elif key == "atividades_secundarias":
                            if len(key) > 0:
                                #print("")
                                #print("\t\t\t| Atividade Prinpipal |")

                                for atividade_secundaria in value:
                                    for key_atividade_secundaria, value_atividade_secundaria in atividade_secundaria.items():
                                        if key_atividade_secundaria == "code":
                                            codigo_atividade_secundaria = value_atividade_secundaria
                                            #print(f"\t{codigo_atividade_secundaria}")
                                            insertAtividadesSecundarias(codigo_atividade_secundaria, id_empresa, cnpj)

                                        # if key_atividade_secundaria == "text":
                                        #     descricao_atividade_secundaria = value_atividade_secundaria
                                        #     #print(f"\t{descricao_atividade_secundaria}")

                                            # Chamando a função para inserir na tabela Atividade Principal
                                            #insertAtividadesSecundarias(codigo_atividade_principal, id_empresa, cnpj)
                        else:
                            #print(f"\t{key}: {value} invalidos")
                            pass



                    print(f"Dados no CNPJ: {cnpj} foram Salvos com Sucesso! #{contador}")
                    contador += 1
                    time.sleep(21)


        except Exception as e:

            print("ERROR:", e)

        #time.sleep(21)


def obter_dados_empresa(cnpj):
    #token sertras
    #token = 'e45446d6415407a3495fac847a0471912570d6cd8af169135bc42f1761a72181'

    try:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            return data

        elif response.status_code == 404:
            print("Empresa não encontrada")
        else:
            print("Erro ao acessar a API da ReceitaWS")
    except:
        print("Erro ao Tentar Consumir a API")


app(quantidade_consultas=1000)



