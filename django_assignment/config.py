DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'django_database',
    'USER': 'postgres',
    'PASSWORD': 'p@stgress',
    'HOST': 'localhost',
    'PORT': '5433',
}

SECRET_KEY = 'django-insecure-ed*765rxcymxl#5(s@!5_!e!z&mpdr1vlv&80_vqe*7q^&4%1y'

SOURCE_DB = {
    'dbname': 'hotel_db',
    'user': 'postgres',
    'password': 'p@stgress',
    'host': 'localhost',
    'port': '5433',
}

DEST_DB = {
    'dbname': 'django_database',
    'user': 'postgres',
    'password': 'p@stgress',
    'host': 'localhost',
    'port': '5433',
}
