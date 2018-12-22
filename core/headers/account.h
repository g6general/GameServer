#ifndef _ACCOUNT_H_
#define _ACCOUNT_H_

#include <iostream>
#include <string>

#include "api.h"

class Account
{
private:
	int m_Number;
	std::wstring m_Nickname;
	std::wstring m_Date;
	std::wstring m_Language;
	bool m_Facebook;
	bool m_Apple;
	bool m_Google;
	int m_TimeInGame;
	int m_NumberOfSessions;
	int m_SessionTime;
	int m_Level;
	int m_Coins;
	int m_Crystals;
	int m_Energy;
	int m_Inventory;
	int m_Consumables;
	int m_Skill;
	int m_Payed;
	bool m_Paying;
	bool m_Banned;

public:
	Account(): m_Number(-1), m_Nickname(L"noname"), m_Date(L"today"), m_Language(L"ru"),
		m_Facebook(false), m_Apple(false), m_Google(false), m_TimeInGame(0), m_NumberOfSessions(0),
		m_SessionTime(0), m_Level(0), m_Coins(0), m_Crystals(0), m_Energy(0), m_Inventory(0),
		m_Consumables(0), m_Skill(0), m_Payed(0), m_Paying(false), m_Banned(false) {}

	Account(s_account account): m_Number(account.number), m_Nickname(account.nickname),
		m_Date(account.date), m_Language(account.language), m_Facebook(account.facebook),
		m_Apple(account.apple), m_Google(account.google), m_TimeInGame(account.timeInGame),
		m_NumberOfSessions(account.numberOfSessions), m_SessionTime(account.sessionTime),
		m_Level(account.level), m_Coins(account.coins), m_Crystals(account.crystals),
		m_Energy(account.energy), m_Inventory(account.inventory),
		m_Consumables(account.consumables), m_Skill(account.skill),
		m_Payed(account.payed), m_Paying(account.paying), m_Banned(account.banned) {}

	int getNumber() const;
	std::wstring getNickname() const;
	std::wstring getDate() const;
	std::wstring getLanguage() const;
	bool getFacebook() const;
	bool getApple() const;
	bool getGoogle() const;
	int getTimeInGame() const;
	int getNumberOfSessions() const;
	int getSessionTime() const;
	int getLevel() const;
	int getCoins() const;
	int getCrystals() const;
	int getEnergy() const;
	int getInventory() const;
	int getConsumables() const;
	int getSkill() const;
	int getPayed() const;
	bool getPaying() const;
	bool getBanned() const;

	void setNumber(int number);
	void setNickname(std::wstring nickname);
	void setDate(std::wstring date);
	void setLanguage(std::wstring language);
	void setFacebook(bool facebook);
	void setApple(bool apple);
	void setGoogle(bool google);
	void setTimeInGame(int timeInGame);
	void setNumberOfSessions(int numberOfSessions);
	void setSessionTime(int sessionTime);
	void setLevel(int level);
	void setCoins(int coins);
	void setCrystals(int crystals);
	void setEnergy(int energy);
	void setInventory(int inventory);
	void setConsumables(int consumables);
	void setSkill(int skill);
	void setPayed(int payed);
	void setPaying(bool paying);
	void setBanned(bool banned);
};

#endif	//_ACCOUNT_H_
