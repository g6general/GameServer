import sys
import ctypes
from mysite.deploy import deploy

CORE_LIBRARY = ''

if sys.platform == 'linux' or sys.platform == 'linux2':
	CORE_LIBRARY = 'libcore.so'
elif sys.platform == 'darwin':
	CORE_LIBRARY = 'libcore.dylib'
elif sys.platform == 'win32':
	CORE_LIBRARY = 'core.dll'

core = ctypes.CDLL(deploy['core_path'] + CORE_LIBRARY)

class s_account(ctypes.Structure):
	_fields_ = [
		("number", ctypes.c_int),
		("nickname", ctypes.c_wchar_p),
		("date", ctypes.c_wchar_p),
		("language", ctypes.c_wchar_p),
		("facebook", ctypes.c_bool),
		("apple", ctypes.c_bool),
		("google", ctypes.c_bool),
		("timeInGame", ctypes.c_int),
		("numberOfSessions", ctypes.c_int),
		("sessionTime", ctypes.c_int),
		("level", ctypes.c_int),
		("coins", ctypes.c_int),
		("crystals", ctypes.c_int),
		("energy", ctypes.c_int),
		("inventory", ctypes.c_int),
		("consumables", ctypes.c_int),
		("skill", ctypes.c_int),
		("payed", ctypes.c_int),
		("paying", ctypes.c_bool),
		("banned", ctypes.c_bool)
	]

class s_statistics(ctypes.Structure):
	_fields_ = [
		("count", ctypes.c_int),
		("banned", ctypes.c_int),
		("paying", ctypes.c_int),
		("active", ctypes.c_int),
		("money", ctypes.c_int)
	]

class s_analytics(ctypes.Structure):
	_fields_ = [
		("active", ctypes.c_bool),
		("coefficient", ctypes.c_double),
		("metrics", ctypes.c_double)
	]

def isGamerActiveWrapper(account):
	convertAccount = s_account(
		account.number, account.nickname, account.date, account.language, account.facebook,
		account.apple, account.google, account.timeInGame, account.numberOfSessions,
		account.sessionTime, account.level, account.coins, account.crystals, account.energy,
		account.inventory, account.consumables, account.skill, account.payed, account.paying,
		account.banned
		)
	core.isGamerActiveApi.argtypes = [s_account]
	core.isGamerActiveApi.restype = ctypes.c_bool
	return core.isGamerActiveApi(convertAccount)

def analyticsWrapper(account):
	convertAccount = s_account(
		account.number, account.nickname, account.date, account.language, account.facebook,
		account.apple, account.google, account.timeInGame, account.numberOfSessions,
		account.sessionTime, account.level, account.coins, account.crystals, account.energy,
		account.inventory, account.consumables, account.skill, account.payed, account.paying,
		account.banned
		)
	core.analyticsApi.argtypes = [s_account]
	core.analyticsApi.restype = s_analytics
	result = core.analyticsApi(convertAccount)

	return (result.active, result.coefficient, result.metrics)

def statisticsWrapper(accounts):
	arrayType = s_account * len(accounts)
	convertAccounts = arrayType()

	for index, value in enumerate(accounts):
		convertAccount = s_account(
		value.number, value.nickname, value.date, value.language, value.facebook, value.apple,
		value.google, value.timeInGame, value.numberOfSessions, value.sessionTime, value.level,
		value.coins, value.crystals, value.energy, value.inventory, value.consumables, value.skill,
		value.payed, value.paying, value.banned
		)

		convertAccounts[index] = convertAccount

	core.statisticsApi.argtypes = [arrayType, ctypes.c_uint]
	core.statisticsApi.restype = s_statistics
	result = core.statisticsApi(convertAccounts, len(accounts))

	return (result.count, result.banned, result.paying, result.active, result.money)
