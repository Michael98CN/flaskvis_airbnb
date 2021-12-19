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

class Listing(db.Model):
    __tablename__ = 'listing_details'  # 表名
    id = db.Column(db.Integer,primary_key=True )
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    neighborhood_overview = db.Column(db.Text)
    host_name = db.Column(db.String(255))
    host_since = db.Column(db.String(255))
    host_about = db.Column(db.Text)
    host_is_superhost = db.Column(db.String(255))
    host_identity_verified = db.Column(db.String(255))
    neighbourhood_cleansed = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    property_type = db.Column(db.String(255))
    room_type = db.Column(db.String(255))
    accommodates = db.Column(db.Integer)
    bathrooms_text = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    beds = db.Column(db.String(255))
    amenities = db.Column(db.Text)
    price = db.Column(db.Float)
    has_availability = db.Column(db.String(255))
    availability_30 = db.Column(db.Integer)
    availability_60 = db.Column(db.Integer)
    availability_90 = db.Column(db.Integer)
    availability_365 = db.Column(db.Integer)
    number_of_reviews = db.Column(db.Integer)
    number_of_reviews_ltm = db.Column(db.Integer)
    number_of_reviews_l30d = db.Column(db.Integer)
    review_scores_rating = db.Column(db.Float)
    review_scores_accuracy = db.Column(db.Float)
    review_scores_cleanliness = db.Column(db.Float)
    review_scores_checkin = db.Column(db.Float)
    review_scores_communication = db.Column(db.Float)
    review_scores_location = db.Column(db.Float)
    review_scores_value = db.Column(db.Float)
    instant_bookable = db.Column(db.String(255))
    reviews_per_month = db.Column(db.Float)

class Calendar(db.Model):
    __tablename__ = 'calendar'  # 表名
    id = db.Column(db.Integer,primary_key=True )
    listing_id = db.Column(db.Integer)
    date = db.Column(db.Float)
    available = db.Column(db.Float)
    price = db.Column(db.Float)
    adjusted_price = db.Column(db.Float)
    minimum_nights = db.Column(db.Integer)
    maximum_nights = db.Column(db.Integer)

db.create_all()



@app.route('/')
def show_all():
    return render_template('vis.html')




if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5000,debug=True)

