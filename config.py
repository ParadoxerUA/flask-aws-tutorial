class ProductionConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:adminadmin@flasktest.cp2vtctxjxkv.eu-central-1.rds.amazonaws.com:3306/flasktest'
    SQLALCHEMY_POOL_RECYCLE = 3600
    WTF_CSRF_ENABLED = True
    SECRET_KEY = '87af05b67bf4aca75e2119175d1fa18c'
