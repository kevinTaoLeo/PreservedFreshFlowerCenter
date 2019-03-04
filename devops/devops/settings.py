"""Django settings for devops project.Generated by 'django-admin startproject' using Django 2.1.7.For more information on this file, seehttps://docs.djangoproject.com/en/2.1/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/2.1/ref/settings/"""import osimport pymysqlimport sys# Build paths inside the project like this: os.path.join(BASE_DIR, ...)BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))sys.path.insert(0,os.path.join(BASE_DIR,"apps"))   ##加载apps# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = 'udepn%h$&o7p51!*pd1d@a!=m+lq#o9(1&0w@sg0-z0&^d%h*_'# SECURITY WARNING: don't run with debug turned on in production!DEBUG = TrueALLOWED_HOSTS = ['192.168.147.129',]# Application definitionINSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    'rest_framework',    'idcs.apps.IdcsConfig',    'users.apps.UsersConfig',    'cabinet.apps.CabinetConfig',    'rest_framework_swagger',]MIDDLEWARE = [    'django.middleware.security.SecurityMiddleware',    'django.contrib.sessions.middleware.SessionMiddleware',    'django.middleware.common.CommonMiddleware',    #'django.middleware.csrf.CsrfViewMiddleware',    'django.contrib.auth.middleware.AuthenticationMiddleware',    'django.contrib.messages.middleware.MessageMiddleware',    'django.middleware.clickjacking.XFrameOptionsMiddleware',]ROOT_URLCONF = 'devops.urls'TEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [],        'APP_DIRS': True,        'OPTIONS': {            'context_processors': [                'django.template.context_processors.debug',                'django.template.context_processors.request',                'django.contrib.auth.context_processors.auth',                'django.contrib.messages.context_processors.messages',            ],        },    },]WSGI_APPLICATION = 'devops.wsgi.application'# Database# https://docs.djangoproject.com/en/2.1/ref/settings/#databases# DATABASES = {#     'default': {#         'ENGINE': 'django.db.backends.sqlite3',#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),#     }# }DATABASES = {    'default': {        'ENGINE': 'django.db.backends.mysql',        'NAME': "devops",        'USER': 'root',        'PASSWORD': "123456",        'HOST': "192.168.147.129",        'OPTIONS': { 'init_command': 'SET storage_engine=INNODB;', }    }}# Password validation# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [    {        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',    },    {        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',    },]# Internationalization# https://docs.djangoproject.com/en/2.1/topics/i18n/LANGUAGE_CODE = 'en-us'TIME_ZONE = 'UTC'USE_I18N = TrueUSE_L10N = TrueUSE_TZ = True# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/2.1/howto/static-files/STATIC_URL = '/static/'