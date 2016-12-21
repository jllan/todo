class FlaskConfig(object):
    '''
    # default
    engine = create_engine('mysql://scott:tiger@localhost/foo')

    # mysql-python
    engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

    # MySQL-connector-python
    engine = create_engine('mysql+mysqlconnector://scott:tiger@localhost/foo')

    # OurSQL
    engine = create_engine('mysql+oursql://scott:tiger@localhost/foo')
    '''
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:cbj@localhost/todo'     # 注意这里是URI，不是URL
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'jlan'