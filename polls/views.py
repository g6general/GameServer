from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader
from .models import getAllAccounts, createAccount, deleteAccount
from .models import editAccount, statistics, analytics, getAccountById
from django.middleware.csrf import get_token

#INDEX_URL = 'http://127.0.0.1:8000/'
INDEX_URL = 'http://gameserver.pythonanywhere.com/'

DEFAULT_DATE = 'today'
DEFAULT_LEVEL = 0
DEFAULT_COINS = 10
DEFAULT_CRYSTALS = 3
DEFAULT_ENERGY = 1
DEFAULT_INVENTORY = 0
DEFAULT_CONSUMABLES = 0
DEFAULT_SKILL = 0
DEFAULT_PAYED = 0
DEFAULT_PAYING = False
DEFAULT_BANNED = False

def index(request):
	template = loader.get_template('polls/index.html')
	accounts = getAllAccounts()
	context = {
		'accounts': accounts
	}
	return HttpResponse(template.render(context, request))

def addAccount(request):
	if request.method == 'POST':
		data = [
			request.POST['nick'],
			request.POST['date'],
			request.POST['language'],
			True if request.POST['facebook'] == 'true' else False,
			True if request.POST['apple'] == 'true' else False,
			True if request.POST['google'] == 'true' else False,
			request.POST['time-in-game'],
			request.POST['number-of-sessions'],
			request.POST['session-time'],
			DEFAULT_LEVEL,
			DEFAULT_COINS,
			DEFAULT_CRYSTALS,
			DEFAULT_ENERGY,
			DEFAULT_INVENTORY,
			DEFAULT_CONSUMABLES,
			DEFAULT_SKILL,
			DEFAULT_PAYED,
			DEFAULT_PAYING,
			DEFAULT_BANNED
		]
		newId = createAccount(data)

		response = None

		if request.POST['from-whom'] == 'browser':
			response = HttpResponseRedirect(INDEX_URL)
		elif request.POST['from-whom'] == 'game':
			response = newId
		return response

	return HttpResponseRedirect(INDEX_URL)

def saveAccount(request):
	if request.method == 'POST':
		accountId = int(request.POST['id'])
		data = [
			request.POST['level'],
			request.POST['coins'],
			request.POST['crystals'],
			request.POST['energy'],
			request.POST['inventory'],
			request.POST['consumables'],
			request.POST['skill'],
			request.POST['payed'],
			True if request.POST['paying'] == 'True' else False,
			True if request.POST['banned'] == 'True' else False
		]
		editAccount(accountId, data)
	return HttpResponseRedirect(INDEX_URL)

def removeAccount(request, id):
	deleteAccount(id)
	return HttpResponseRedirect(INDEX_URL)

def getAccountInfo(request, id):
	account = getAccountById(id)

	response = JsonResponse({
		'level': account.level,
		'coins': account.coins,
		'crystals': account.crystals,
		'energy': account.energy,
		'inventory': account.inventory,
		'consumables': account.consumables,
		'skill': account.skill,
		'payed': account.payed,
		'paying': 'True' if account.paying else 'False',
		'banned': 'True' if account.banned else 'False'
	})

	return response

def showStatistics(request):
	count, banned, paying, active, money = statistics()

	response = JsonResponse({
		'count': count,
		'banned': banned,
		'paying': paying,
		'active': active,
		'money': money
	})

	return response

def showAnalytics(request, id):
	active, coefficient, metrics = analytics(id)

	response = JsonResponse({
		'active': active,
		'coefficient': coefficient,
		'metrics': metrics
	})

	return response

def getToken(request):
	response = JsonResponse({
		'csrf_token': get_token(request)
	})

	return response
