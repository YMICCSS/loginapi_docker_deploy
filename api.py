from flask import Flask,render_template,redirect
from flask import request
import secrets
from db import update_db

app = Flask(__name__)

# 隨機碼函式
def generate_nonce():
    nonce = secrets.token_hex()
    return nonce

@app.route('/',methods=['GET'])
def home():
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def hello_world():

    url = request.form.get("save_url")
    url_list = url.split("?")
    Account = request.form.get("ACCOUNT")
    Password = request.form.get("PASSWORD")
    nonce = generate_nonce()
    Userid = url_list[2].split("=")[1]
    token = url_list[1].split("=")[1]
    if Account == "11" and Password == "11":
        update_db(Account, Password, nonce, Userid, token)
        return redirect(f"https://access.line.me/dialog/bot/accountLink?linkToken={token}&nonce={nonce}")

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5500)