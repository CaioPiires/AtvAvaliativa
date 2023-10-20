from conexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def funcaoAtualizar(idDados, desc, val, cat, dtMov, tipo):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_dados
            SET descricao= '{desc}', valor= '{val}',
            categoria='{cat}', dt_movimentacao= '{dtMov}', tipo= '{tipo}' WHERE id_dados= '{idDados}'
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True    
    
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar!" +str(falha))
        return False
    
    finally:
        conexao.close()
        cursor.close()