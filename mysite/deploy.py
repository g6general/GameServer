development = {
	'url': 'http://127.0.0.1:8000/',
	'db_name': 'accounts',
	'host': 'localhost',
	'user': 'django_user',
	'password': 'django_passwd',
	'core_path': './core/build/'
}

production = {
	'url': 'http://gameserver.pythonanywhere.com/',
	'db_name': 'gameserver$accounts',
	'host': 'gameserver.mysql.pythonanywhere-services.com',
	'user': 'gameserver',
	'password': 'game_root',
	'core_path': '/home/gameserver/Server/core/build/'
}

# development if local
# production if internet
deploy = production
