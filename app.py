from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *
import pymysql


# 什么意思？
pymysql.install_as_MySQLdb()

app = Flask(__name__)

class Config(object):
    """参数配置"""
    user = 'root'
    password = 'hmqww123'
    database = 'db_vis'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@127.0.0.1:3306/%s' % (user, password, database)
    # 设置sqlalchemy自动更跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False



# 读取配置
app.config.from_object(Config)
# 解决跨域问题
CORS(app, supports_credentials=True)
# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Neighborhood(db.Model):
    __tablename__ = 'neighbourhoods'  # 表名
    neighbourhood_id = db.Column(db.Integer, primary_key=True)
    neighbourhood = db.Column(db.String(255))

    def __init__(self, neighbourhood_id, neighbourhood):
        self.neighbourhood_id = neighbourhood_id
        self.neighbourhood = neighbourhood


db.create_all()



@app.route('/')
def show_all():
    return render_template('vis.html')




if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000,debug=True)

