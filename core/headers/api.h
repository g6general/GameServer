#ifndef _API_H_
#define _API_H_

struct s_account
{
	int number;
	wchar_t* nickname;
	wchar_t* date;
	wchar_t* language;
	bool facebook;
	bool apple;
	bool google;
	int timeInGame;
	int numberOfSessions;
	int sessionTime;
	int level;
	int coins;
	int crystals;
	int energy;
	int inventory;
	int consumables;
	int skill;
	int payed;
	bool paying;
	bool banned;
};

struct s_statistics
{
	int count;
	int banned;
	int paying;
	int active;
	int money;
};

struct s_analytics
{
	bool active;
	double coefficient;
	double metrics;
};

extern "C" bool isGamerActiveApi(s_account account);
extern "C" s_statistics statisticsApi(s_account* arr, unsigned size);
extern "C" s_analytics analyticsApi(s_account account);

#endif //_API_H_
