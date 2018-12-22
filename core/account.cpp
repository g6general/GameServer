#include "account.h"

int Account::getNumber() const { return m_Number; }
std::wstring Account::getNickname() const { return m_Nickname; }
std::wstring Account::getDate() const { return m_Date; }
std::wstring Account::getLanguage() const { return m_Language; }
bool Account::getFacebook() const { return m_Facebook; }
bool Account::getApple() const { return m_Apple; }
bool Account::getGoogle() const { return m_Google; }
int Account::getTimeInGame() const { return m_TimeInGame; }
int Account::getNumberOfSessions() const { return m_NumberOfSessions; }
int Account::getSessionTime() const { return m_SessionTime; }
int Account::getLevel() const { return m_Level; }
int Account::getCoins() const { return m_Coins; }
int Account::getCrystals() const { return m_Crystals; }
int Account::getEnergy() const { return m_Energy; }
int Account::getInventory() const { return m_Inventory; }
int Account::getConsumables() const { return m_Consumables; }
int Account::getSkill() const { return m_Skill; }
int Account::getPayed() const { return m_Payed; }
bool Account::getPaying() const { return m_Paying; }
bool Account::getBanned() const { return m_Banned; }

void Account::setNumber(int number) { m_Number = number; }
void Account::setNickname(std::wstring nickname) { m_Nickname = nickname; }
void Account::setDate(std::wstring date) { m_Date = date; }
void Account::setLanguage(std::wstring language) { m_Language = language; }
void Account::setFacebook(bool facebook) { m_Facebook = facebook; }
void Account::setApple(bool apple) { m_Apple = apple; }
void Account::setGoogle(bool google) { m_Google = google; }
void Account::setTimeInGame(int timeInGame) { m_TimeInGame = timeInGame; }
void Account::setNumberOfSessions(int numberOfSessions) { m_NumberOfSessions = numberOfSessions; }
void Account::setSessionTime(int sessionTime) { m_SessionTime = sessionTime; }
void Account::setLevel(int level) { m_Level = level; }
void Account::setCoins(int coins) { m_Coins = coins; }
void Account::setCrystals(int crystals) { m_Crystals = crystals; }
void Account::setEnergy(int energy) { m_Energy = energy; }
void Account::setInventory(int inventory) { m_Inventory = inventory; }
void Account::setConsumables(int consumables) { m_Consumables = consumables; }
void Account::setSkill(int skill) { m_Skill = skill; }
void Account::setPayed(int payed) { m_Payed = payed; }
void Account::setPaying(bool paying) { m_Paying = paying; }
void Account::setBanned(bool banned) { m_Banned = banned; }
