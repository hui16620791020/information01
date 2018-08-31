# coding=UTF-8
from flask import Flask,session,current_app
from info import create_app,db,models
from flask_script import Manager
import logging
from flask_migrate import Migrate,MigrateCommand
app = create_app("development")
#  7.创建manager管理类
manager = Manager(app)
 #  初始化迁移对象
Migrate(app,db)
 #  将迁移命令添加到管理对象中
manager.add_command("db", MigrateCommand)




if __name__ == '__main__':
    # logging.debug("debug的日志信息")
    # logging.info("info的日志信息")
    # logging.warning("warning的日志信息")
    # logging.error("error的日志信息")
    # logging.critical("critical的日志信息")
    # current_app.logger.debug("使用flask里面封装的方法，记录debug日志")
    manager.run()