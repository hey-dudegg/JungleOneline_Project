from flask import Flask

import re

from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.jungle_week0

app = Flask(__name__)

# 회원가입
@app.route('/user/feature/signup', methods=['post'])
def singup():
  Name = request.form['name']
  Id = request.form['id']
  Pw = request.form['password']
  Nickname = request.form['nickname']
  Myself = request.form['myself']
  Img = request.files['file']
  
  doc ={
    "Name":Name,
    "Id":Id,
    "Pw":Pw,
    "Nickname":Nickname,
    "Myself":Myself,
    "Comment":" ",
    "Img":" ",
    "Gkeyword": [{'성실함':0},{'친화적':0},{'꼼꼼함':0},{'끈기있는':0}],
    "Bkeyword": [{'불성실함':0},{'비판적':0},{'비협조적':0},{'의지가 약한':0}],
    "Writed": " "
  }
  db.user.insert_one(doc)
  return render_template('index.html')
# 교육생 목록 
@app.route('/user/feature/list', methods=['get'])
def list():
  users_names = list(db.users.find({},{"Name":1,"Gkeyword":1}))
# 검색
# @app.route('/user/feature/search', methods=['post'])
# def search():
#   user_name = request.form['name']
#   regex_pattern = re.compile(f".*{user_name}.*")
#   searched_names = list(db.users.find({"Name":{"$regex": regex_pattern}},{"Name":1,"Gkeyword":1}))
# # 카테고리 정렬
# @app.route('/user/feature/listsort', methods=['post'])
# def listsort():
#   sorted_user = list(db.users.find({}).sort[('name',-1),('gkeyword',-1)])

@app.route("/")
def home():
  return render_template('index.html')

@app.route('/ismember', methods=['POST'])
def post_ismember():
  # 클라이언트로부터 데이터를 받기
  id_receive = request.form['id_give']
  pw_receive = request.form['pw_give']
  
  id = db.hanjul.find_one({"id": id_receive})
  pw = db.hanjul.find_one({"pw": pw_receive})
  if id == '':
    if pw == pw_receive:
      return jsonify({"result": "success"})
    else: 
      return jsonify({"result": "pw_fail"})
  else:
    return jsonify({"result": "id_fail"})

@app.route("/user/login")
def logInPage():
  return render_template('logIn.html')

@app.route("/user/signup")
def signUpPage():
  return render_template('signUp.html')

@app.route("/main/list")
def mainPage():
  return render_template('mainPage')

# ! Mac 환경에선 port 번호 5001, 배포 시에는 5000으로 수정
if __name__ == "__main__":
  app.run('0.0.0.0', port=5001, debug=True)
