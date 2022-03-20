#-*-coding:utf-8 -*-

import generate

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__) # __name__代表目前執行的模組
CORS(app)

@app.route("/") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def home():
    return 'hello!'


@app.route('/predict', methods=["POST"])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    prefix = insertValues['keyin']
    total_length = insertValues['row']
    result = generate.main(prefix,total_length)
    return jsonify(result)


@app.route("/test") # 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
def getValue():
    result = generate.main('美好',6)
    print(result)
    return jsonify(result)


if __name__=="__main__": # 如果以主程式執行
    app.run(host='0.0.0.0', port=80, debug=True) # 立刻啟動伺服器