#include "funcs.h"

const int ACTIVE_GAMER_LIMIT = 100;

bool isGamerActive(const Account& account)
{
	return (account.getNumberOfSessions() > ACTIVE_GAMER_LIMIT && account.getPaying());
}

std::map<std::string, int> statistics(const std::vector<Account>& accounts)
{
	std::map<std::string, int> result;
	result.insert({"count", accounts.size()});

	for (auto account : accounts)
	{
		if (account.getBanned())
			result["banned"]++;

		if (account.getPaying())
			result["paying"]++;

		if (isGamerActive(account))
			result["active"]++;

		result["money"] += account.getPayed();
	}

	return result;
}

std::map<std::string, double> analytics(const Account& account)
{
	std::map<std::string, double> result;
	result.insert({"active", isGamerActive(account)});

	if (!account.getBanned() && account.getPaying())
		result["coefficient"] = account.getPayed() / account.getNumberOfSessions();
	else
		result["coefficient"];

	const double coefA = 0.57;
	const double coefB = 0.23;
	const double coefC = 0.16;

	result["metrics"] = coefA * account.getLevel() + coefB * account.getCrystals()
		+ coefC * account.getSkill();

	return result;
}
