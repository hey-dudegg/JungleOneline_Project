from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
from bson import ObjectId
from werkzeug.utils import secure_filename
import os

from jinja2 import Template

from pymongo import MongoClient

from routes import getInfo_bp, logIn_bp, main_bp

import re, json, os, uuid

app = Flask(__name__)

# * DB 연결
client = MongoClient('localhost', 27017)
db = client.jungle_week0

# * Blueprint 설정
app.register_blueprint(getInfo_bp)
app.register_blueprint(logIn_bp)
app.register_blueprint(main_bp)

# ! Router
@app.route("/")
def home():
  return render_template('index.html')  

@app.route("/user/<user_name>/comment")
def userPage(user_name):
  student = db.user.find({"Name": user_name})

  if student:
    return render_template('userPage.html', student=student)
  else :
    return "교육생 정보를 찾을 수 없습니다.", 404

@app.route("/user/signup")
def signUpPage():
  return render_template('signUp.html')

@app.route("/user/writing")
def writePage():
  return render_template('writing.html')  

# ! API

# ? 회원가입
@app.route('/user/feature/signup', methods=['post'])
def singup():
  try:
    Id = request.form['id']
    Pw = request.form['pw']
    PwConf = request.form['pwConf']
    Name = request.form['name']
    Nickname = request.form['nickname']
    Myself = request.form['myself']
    Img = request.files['img']
  except:
    return jsonify({"result": "fail"})

  if Img and allowed_file(Img.filename):
    filename = str(uuid.uuid4()) + Name
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename )
    Img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  
  doc ={
    "Id":Id,
    "Pw":Pw,
    "Name":Name,
    "Nickname":Nickname,
    "Myself":Myself,
    "Comment":[],
    "Img":{'filename': filename, 'path': file_path},
    "Gkeyword": [{'성실함':0},{'친화적':0},{'꼼꼼함':0},{'끈기있는':0},
                 {'수용적인':0},{'현명한':0},{'상상력 풍부한':0},{'책임감 있는':0},
                 {'계획적인':0},{'전문적인':0}],
    "Bkeyword": [{'불성실함':0},{'비판적':0},{'비협조적':0},
                 {'의지가 약한':0},{'이기적인':0},{'민감한':0},{'화가 많은':0},
                 {'고집쎈':0},{'수동적':0}],
    "Writed": " "
  }
  db.user.insert_one(doc)
  
  return jsonify({"result": "success"}) 

# ? 사진 업로드
# * 디렉토리 설정
UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# * 파일 확장자 정의
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# * 파일 확장자 확인 함수
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# * 사진 불러오기
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ! Mac 환경에선 port 번호 5001, 배포 시에는 5000으로 수정
if __name__ == "__main__":
  app.run('0.0.0.0', port=5001, debug=True)
