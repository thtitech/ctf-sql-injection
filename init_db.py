import sqlite3
import hashlib
import os

db = "/srv/ctf/ctf.db"

if os.path.exists(db):
    os.remove(db)

con = sqlite3.connect(db)

c = con.cursor()
# create tables
c.execute("create table users (user_id text PRIMARY KEY, password text, description text)")
c.execute("create table rooms (room_id integer PRIMARY KEY, room_name text, description text)")

# insert room data
data = [("雑談部屋", "みんなで雑談しましょう"), ("一般部屋", "一般的な部屋"), ("暇な人募集", "暇な人集まれ〜"), ("スプラリグマ募集@2", "リグマしましょう！")]

for i, t in enumerate(data):
    sql = "insert into rooms values({0}, '{1}', '{2}')".format(i, t[0], t[1])
    c.execute(sql)

# insert user data
data = [("testuser1", "test", "テスト用"), ("testuser2", "test", "テスト用"), ("admin", "admin", "廃止された管理者"), ("tonosaki", "tonosaki", "システム管理者"), ("kanazawa", "kanazawa", "お試しユーザー"), ("totoki", "totoki", "お試しユーザー"), ("hayashi", "hayashi", "お試しユーザー")]

for d in data:
    passwd = str(hashlib.md5(d[1].encode()).hexdigest())
    sql = "insert into users values('{0}', '{1}', '{2}')".format(d[0], passwd, d[2])
    c.execute(sql)

con.commit()
    
con.close()

