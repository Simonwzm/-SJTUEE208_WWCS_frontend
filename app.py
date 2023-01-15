from flask import Flask, render_template, request, redirect, url_for,jsonify,Blueprint
import json
import os

# import search_engine.searchFile as searchFile
import search_engine_1.searchFile as searchFile

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r"./upload"  # 设置文件上传的目标文件夹
CORS(app,supports_credentials=True)



@app.route('/search', methods=['GET', 'POST'])
def index():
    data = request.get_json(silent=True)
    
    print(data)

    keyword = data["keyword"]
    url = data["url"]
    title = data["title"]
    if "date" not in data.keys():
        date = None
    else:
        date = data["date"]
        date = date.split("-")
    result = searchFile.main(keyword,url,date,title)
    # print(result)
    return jsonify(result)

@app.route('/upload',methods=["POST"]) # 方法要与前端一致
def upload():
    file_obj = request.files['file']  # Flask中获取文件
    if file_obj is None:
        # 表示没有发送文件
        return "未上传文件"
    #保存文件
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")     
    file_obj.save(file_path)
    return file_path






if __name__ == '__main__':
    app.run()