import sqlite3
from flask import *
import hashlib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", query="", data=[])

@app.route("/search", methods=["POST"])
def search():
    q = request.form["query"]
    con = sqlite3.connect("/srv/ctf/ctf.db")
    c = con.cursor()
    if q == "*":
        sql = "select * from rooms"
    else:
        sql = "select * from rooms where room_name='" + q + "'"
    c.execute(sql)
    data = c.fetchall()
    con.close()
    return render_template("index.html", data=data, query=q)

@app.route("/login", methods=["POST"])
def login():
    user_id = request.form["user_id"]
    password = request.form["password"]
    password = str(hashlib.md5(password.encode()).hexdigest())
    sql = "select * from users where user_id='{0}' and password='{1}'".format(user_id, password)
    con = sqlite3.connect("/srv/ctf/ctf.db")
    c = con.cursor()
    c.execute(sql)
    data = c.fetchall()
    con.close()
    if len(data) == 0:
        return render_template("index.html", data=[], query="", msg="ログイン失敗")
    user_id = data[0][0]
    desc = data[0][2]
    if len(data) == 1 and user_id == "tonosaki":
        msg = "フラッグは「ともにその先の答えを」です"
    else:
        msg = "他のユーザーでログインしてみてください"
    return render_template("user.html", msg=msg, user_id=user_id, description=desc)

@app.errorhandler(500)
def handle_not_found(error):
    return render_template("index.html", data=[], query="", msg="エラーが起きました"), 500

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080)

