user = 'maria'
password = 'pass'
host = 'db'
database = 'beverage'

COCKROACH = {
    'engine': 'cockroachdb',
    'username': 'root',
    'password': '',
    'host': host,
    'port': 26257,
    'db_name': database,
}

ELASTICSEARCH = {
    'engine': 'elasticsearch',
    'host': '', # set at runtime
    'port': 9200,
    'user': 'elastic',
    'password': 'changeme'
}

MYSQL = {
    'engine': 'mariadb+pymysql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

POSTGRESQL = {
    'engine': 'postgresql',
    'username': user,
    'password': password,
    'host': host,
    'db_name': database,
}

SQLSERVER = {
    'engine': 'mssql+pymssql',
    'username': 'sa',
    'password': 'z!x<?oB1ab',
    'host': host,
    'db_name': 'master',
}

SQLALCHEMY = {
  'autocommit': False,
  'autoflush': False,
  'sessionmaker': [False, False],
  'debug': False,
}
