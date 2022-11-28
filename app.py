from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from car")
    data=cur.fetchall()
    return render_template("index.html", datas=data)

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from car")
    data=cur.fetchall()
    return render_template("index.html", datas=data)

@app.route("/add_car", methods=["POST", "GET"])
def add_car():
    if request.method == "POST":
        marca=request.form["marca"]
        modelo=request.form["modelo"]
        preco=request.form["preco"]
        ano=request.form["ano"]
        localizacao=request.form["localizacao"]
        descricao=request.form["descricao"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("insert into car(MARCA, MODELO, PRECO, ANO, LOCALIZACAO, DESCRICAO) values (?,?,?,?,?,?)", (marca, modelo, preco, ano, localizacao, descricao))
        con.commit()
        flash("Dados cadastrados", "success")
        return redirect(url_for("index"))
    return render_template("add_car.html")

@app.route("/edit_car/<string:id>", methods=["POST", "GET"])
def edit_car(id):
    if request.method == "POST":
        marca=request.form["marca"]
        modelo=request.form["modelo"]
        preco=request.form["preco"]
        ano=request.form["ano"]
        localizacao=request.form["localizacao"]
        descricao=request.form["descricao"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update car set MARCA=?, MODELO=?, PRECO=?, ANO=?, LOCALIZACAO=?, DESCRICAO=? where ID=?", (marca, modelo, preco, ano, localizacao, descricao, id))
        con.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from car where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_car.html", datas=data)

@app.route("/delete_car/<string:id>", methods=["GET"])
def delete_car(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from car where ID=?", (id,))
    con.commit()
    flash("Dados excluídos", "warning")
    return redirect(url_for("index"))

if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)