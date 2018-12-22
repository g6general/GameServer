#ifndef _FUNCS_H_
#define _FUNCS_H_

#include <vector>
#include <map>
#include "account.h"

bool isGamerActive(const Account& account);
std::map<std::string, int> statistics(const std::vector<Account>& accounts);
std::map<std::string, double> analytics(const Account& account);

#endif	//_FUNCS_H_
