#
from re import A
from models import Car, Usuario
import psycopg2.extras
from consultas import *

class CarroDao:
    def __init__(self, db):
        self.__db = db
    
    def salvar(self, carro):
        cursor = self.__db.cursor()
        if(carro.id):
            cursor.execute(SQL_ATUALIZA_CARRO, (carro.marca, carro.modelo, carro.cor, carro.combustivel, carro.ano, carro.id))
        else:
            cursor.execute(SQL_CRIA_CARRO, (carro.marca, carro.modelo, carro.cor, carro.combustivel, carro.ano))
            carro.id = cursor.fetchone()[0]
        self.__db.commit()
        cursor.close()
        return carro
    
    def listar(self):
        cursor = self.__db.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cursor.execute(SQL_BUSCA_CARROS)
        carros = traduz_carros(cursor.fetchall())
        cursor.close()
        return carros

    def busca_por_id(self, id):
        cursor = self.__db.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cursor.execute(SQL_CARRO_POR_ID, (id,))
        tupla = cursor.fetchone()
        cursor.close()
        return Car(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], id=tupla[0])
    
    def deletar(self, id):
        cursor = self.__db.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cursor.execute(SQL_DELETA_CARRO, (id,))
        self.__db.commit()
        cursor.close()

class UsuarioDao:
    def __init__(self, db):
        self.__db = db
    
    def buscar_por_id(self, id):
        cursor = self.__db.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return 
    
    def autenticar(self, id, senha):
        cursor = self.__db.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cursor.execute(SQL_AUTENTICAR_USUARIO, (id, senha))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario
    
    def salvar(self, usuario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CRIA_USUARIO, (usuario.id, usuario.nome, usuario.senha))
        self.__db.commit()
        cursor.close()
        return usuario
    
def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])

def traduz_carros(carros):
    def criar_carro_com_tupla(tupla):
        return Car(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], id=tupla[0])
    return list(map(criar_carro_com_tupla, carros))