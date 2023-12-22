import os
import mysql.connector
from mysql.connector import errorcode
from env_config import *

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.environ.get('SERVIDOR'),
            user=os.environ.get('USUARIO'),
            password=os.environ.get('SENHA'),
            database=os.environ.get('BANCO')
        )

    def execute_main_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        cursor.close()

    def execSql(self, sql, dados):
        try:
            # Criar um cursor para executar comandos SQL
            cursor = self.connection.cursor()
            cursor.execute(sql, dados)

            # Confirmar as alterações no banco de dados
            self.connection.commit()
            #print("Dados salvos com sucesso!")


        except mysql.connector.Error as erro:
            print(f"Ocorreu um erro ao salvar os dados: {erro}")

        finally:
            # Fechar o cursor e a conexão com o banco de dados
            cursor.close()
            self.connection.close()
