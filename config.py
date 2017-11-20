class Config:
    # 数据库session自动commit
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #session,cookie,Token 加密key
    SECRET_KEY = 'BYS.bys#nbBYs'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    #数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://sa:1ohNE7Hwj=yW@192.168.1.195:3306/demo' #mysql://用户：密码@连接地址：端口/数据库


class TestingConfig(Config):
    #数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://sa:1ohNE7Hwj=yW@192.168.1.195:3306/demo' #mysql://用户：密码@连接地址：端口/数据库


class ProductionConfig(Config):
    #数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://sa:1ohNE7Hwj=yW@192.168.1.195:3306/demo' #mysql://用户：密码@连接地址：端口/数据库

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,
    'default': DevelopmentConfig
}