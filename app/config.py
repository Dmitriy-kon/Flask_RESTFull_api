class Config:
    # App configuration
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}

    # DB configurate
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data/movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
