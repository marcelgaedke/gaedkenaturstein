
IS_SERVER = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h@038=+$l7kwmfga%eyb+jg0yg+(6*xp_@t97y=xu-clutp)+1'

STATIC_ROOT ='/var/www/ssd1400/htdocs/App1/static'
#STATIC_ROOT = "/home/kidneybean/grabmalehamburg/website/grabmalehamburg_14_1_2019/gaedkenaturstein/htdocs/App1/static"

#MEDIA_ROOT ="/home/kidneybean/Downloads/grabmalehamburg_3_10_18/htdocs/App1/static/"
MEDIA_ROOT = "/home/kidneybean/grabmalehamburg/website/grabmalehamburg_14_1_2019/gaedkenaturstein/htdocs/App1/static"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grabmalehamburg_local',
        'USER': 'user1',
        'PASSWORD': 'pass1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssd1400gn',
        'USER': 'ssd1400gn',
        'PASSWORD': 'DimdifEnd4oj(',
        'HOST': 'localhost',
        'PORT': '',
    }
}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

