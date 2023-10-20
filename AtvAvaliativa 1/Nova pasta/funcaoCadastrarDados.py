from mysql import connector
from mysql.connector import cursor
from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def cadastrar(desc, val, cat, dtmov, tipo):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_dados
            (descricao, valor, categoria, dt_movimentacao, tipo)
            VALUES
            ('{desc}', '{val}','{cat}','{dtmov}', '{tipo}')
            """

        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()

