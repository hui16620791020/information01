from flask import Flask,session
from info import create_app
from flask_script import Manager





app = create_app("development")
# 7.创建manager管理类
manager = Manager(app)


@app.route("/")
def index():
    # 没有调整之前：　数据存在flask后端服务器　　只是讲session_id使用cookie传给客户端
    session["name"] = "James"
    return "hello word"


if __name__ == '__main__':
    manager.run()