from django.db import models
from core.wrapper import *

ACTIVE_GAMER_LIMIT = 100

class Account(models.Model):
	number = models.IntegerField()
	nickname = models.CharField(max_length=30)
	date = models.CharField(max_length=30)
	language = models.CharField(max_length=30)
	facebook = models.BooleanField()
	apple = models.BooleanField()
	google = models.BooleanField()
	timeInGame = models.IntegerField()
	numberOfSessions = models.IntegerField()
	sessionTime = models.IntegerField()
	level = models.IntegerField()
	coins = models.IntegerField()
	crystals = models.IntegerField()
	energy = models.IntegerField()
	inventory = models.IntegerField()
	consumables = models.IntegerField()
	skill = models.IntegerField()
	payed = models.IntegerField()
	paying = models.BooleanField()
	banned = models.BooleanField()

def getAllAccounts():
	return Account.objects.all()

def getAccountById(id):
	return Account.objects.filter(number=str(id)).first()

def deleteAccount(id):
	obj = getAccountById(id)
	obj.delete()

def generateId():
	if Account.objects.all().count():
		return 1+Account.objects.order_by('-number').first().number
	else:
		return 0

def createAccount(data = []):
	newAccount = None
	newId = generateId()

	if data:
		newAccount = Account(
			number = newId, nickname = data[0], date = data[1], language = data[2], facebook = data[3],
			apple = data[4], google = data[5], timeInGame = data[6], numberOfSessions = data[7],
			sessionTime = data[8], level = data[9], coins = data[10], crystals = data[11],
			energy = data[12], inventory = data[13], consumables = data[14], skill = data[15],
			payed = data[16], paying = data[17], banned = data[18]
			)
	else:
		newAccount = Account(
			number = newId, nickname = 'default', date = 'today', language = 'ru', facebook = True,
			apple = True, google = True, timeInGame = 0, numberOfSessions = 0, sessionTime = 0,
			level = 0, coins = 0, crystals = 0, energy = 0, inventory = 0, consumables = 0,
			skill = 0, payed = 0, paying = False, banned = False
			)

	newAccount.save()
	return newId
	
def editAccount(id, data):
	account = getAccountById(id)
	account.level = data[0]
	account.coins = data[1]
	account.crystals = data[2]
	account.energy = data[3]
	account.inventory = data[4]
	account.consumables = data[5]
	account.skill = data[6]
	account.payed = data[7]
	account.paying = data[8]
	account.banned = data[9]
	account.save()

def isGamerActive(account):
	return isGamerActiveWrapper(account)

def statistics():
	accounts = Account.objects.all()
	return statisticsWrapper(accounts)

def analytics(id):
	account = getAccountById(id)
	return analyticsWrapper(account)

def fillDataCheat():
	createAccount(['JIuMoH4eG', 'Sat Dec 08 2018', False, True, False, False, '237', '11', '23',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['SmoKKeR', 'Sat Dec 08 2018', False, False, True, True, '582', '37', '45',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Foxy_[P]i]r]a]t]e]', 'Sat Dec 08 2018', False, True, True, True, '112', '561', '13',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['ẌūℒΐǤắ₦', 'Sat Dec 08 2018', True, False, False, True, '427', '78', '27',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Lиsичка', 'Sat Dec 08 2018', True, False, False, False, '926', '128', '34',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['☆Zigzag☆', 'Sat Dec 08 2018', True, True, False, False, '467', '29', '48',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['N.E.O.N', 'Sat Dec 08 2018', False, True, True, True, '512', '118', '11',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['▀▄▀▄ FINISH ▀▄▀▄', 'Sat Dec 08 2018', False, False, True, False, '954', '489', '25',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['ﮚ.†.λ.Ⱡ.₭.∑.Ʀ', 'Sat Dec 08 2018', True, True, True, False, '126', '312', '17',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Good_Joker', 'Sat Dec 08 2018', False, True, False, False, '356', '410', '10',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['pr!zrak?!', 'Sat Dec 08 2018', True, False, True, True, '243', '79', '28',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Mirrox', 'Sat Dec 08 2018', False, True, False, False, '754', '287', '50',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['_LegenDa_', 'Sat Dec 08 2018', True, False, True, True, '275', '56', '21',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Ceme4ka', 'Sat Dec 08 2018', True, True, True, True, '835', '98', '14',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
	createAccount(['Летучий Олень', 'Sat Dec 08 2018', True, False, False, False, '285', '331', '42',
		0, 10, 3, 1, 0, 4, 0, 2, False, False])
