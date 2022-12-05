import sqlite3 as sql

con = sql.connect ('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "car" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "MARCA" TEXT,
    "MODELO" TEXT,
    "PRECO" TEXT,
    "ANO" TEXT,
    "LOCALIZACAO" TEXT,
    "IMAGEM" TEXT,
    "DESCRICAO" TEXT
    )'''

cur.execute(sql)
con.commit()
con.close()