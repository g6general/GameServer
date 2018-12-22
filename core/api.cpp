#include "api.h"
#include "funcs.h"

bool isGamerActiveApi(s_account account)
{
	Account obj(account);
	return isGamerActive(obj);
}

s_statistics statisticsApi(s_account* arr, unsigned size)
{
	std::vector<Account> accounts;
	std::map<std::string, int> result;
	s_statistics sResult;

	for (unsigned i = 0; i < size; ++i)
		accounts.emplace_back(arr[i]);

	result = statistics(accounts);

	sResult.count = result["count"];
	sResult.banned = result["banned"];
	sResult.paying = result["paying"];
	sResult.active = result["active"];
	sResult.money = result["money"];

	return sResult;
}

s_analytics analyticsApi(s_account account)
{
	Account obj(account);
	std::map<std::string, double> result;
	s_analytics sResult;

	result = analytics(obj);

	sResult.active = result["active"];
	sResult.coefficient = result["coefficient"];
	sResult.metrics = result["metrics"];

	return sResult;
}
