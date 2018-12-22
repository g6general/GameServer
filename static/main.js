var BASE_URL = 'http://127.0.0.1:8000/';
var ADD_URL = 'add/';
var SAVE_URL = 'save/';
var REMOVE_URL = 'remove/';
var INFO_URL = 'info/';
var ANALYTICS_URL = 'analytics/';
var STATISTICS_URL = 'statistics/';

var BANNED_COLOR = '#FFB6C1';
var SELECTED_COLOR = '#87CEFA';
var OVERLAY_COLOR = '#EE82EE';

function PageState() {
	this.getId = function() {
		if (sessionStorage.getItem("current_id")) {
			return sessionStorage.getItem("current_id");
		}
		else {
			return -1;
		}
	};

	this.setId = function(id) {
		sessionStorage.setItem("current_id", id);
	};

	this.isValid = function() {
		if (this.getId() < 0)
			return false;
		else
			return true;
	};
}

var pageState = new PageState();

var tableData = document.getElementById('data');

var numberField = document.getElementById('number-field');
var nicknameField = document.getElementById('nickname-field');
var timeField = document.getElementById('time-field');
var numberOfSessionsField = document.getElementById('number-of-sessions-field');
var averageSessionTimeField = document.getElementById('average-session-time-field');

var languageField = document.getElementById('language-field');
var facebookField = document.getElementById('facebook-field');
var appleField = document.getElementById('apple-field');
var googleField = document.getElementById('google-field');

var buttonAdd = document.getElementById('button-add');
var buttonSave = document.getElementById('button-save');
var buttonRemove = document.getElementById('button-remove');

var buttons = [
	buttonSave,
	buttonRemove,
	document.getElementById('button-plus-1'),
	document.getElementById('button-minus-1'),
	document.getElementById('button-plus-2'),
	document.getElementById('button-minus-2'),
	document.getElementById('button-plus-3'),
	document.getElementById('button-minus-3'),
	document.getElementById('button-plus-4'),
	document.getElementById('button-minus-4'),
	document.getElementById('button-plus-5'),
	document.getElementById('button-minus-5'),
	document.getElementById('button-plus-6'),
	document.getElementById('button-minus-6'),
	document.getElementById('button-plus-7'),
	document.getElementById('button-minus-7'),
	document.getElementById('button-plus-8'),
	document.getElementById('button-minus-8'),
	document.getElementById('button-yes-1'),
	document.getElementById('button-no-1'),
	document.getElementById('button-yes-2'),
	document.getElementById('button-no-2')
];

function saveAccount() {
	var level = document.getElementById('gamer-level').value;
	var coins = document.getElementById('gamer-coins').value;
	var crystals = document.getElementById('gamer-crystals').value;
	var energy = document.getElementById('gamer-energy').value;
	var inventory = document.getElementById('gamer-inventory').value;
	var consumables = document.getElementById('gamer-consumables').value;
	var skill = document.getElementById('gamer-skill').value;
	var payed = document.getElementById('gamer-payed').value;
	var paying = document.getElementById('gamer-paying').value;
	var banned = document.getElementById('gamer-banned').value;

	var xhr = new XMLHttpRequest();
	xhr.open('POST', BASE_URL + SAVE_URL, false);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.setRequestHeader('X-CSRFToken', csrf_token);

	var body = 'id=' + encodeURIComponent(pageState.getId()) +
		'&level=' + encodeURIComponent(level) +
		'&coins=' + encodeURIComponent(coins) +
		'&crystals=' + encodeURIComponent(crystals) +
		'&energy=' + encodeURIComponent(energy) +
		'&inventory=' + encodeURIComponent(inventory) +
		'&consumables=' + encodeURIComponent(consumables) +
		'&skill=' + encodeURIComponent(skill) +
		'&payed=' + encodeURIComponent(payed) +
		'&paying=' + encodeURIComponent(paying) +
		'&banned=' + encodeURIComponent(banned);
	xhr.send(body);

	showStatistics();
	showGamerAnalytics();
}

function addAccount() {
	var xhr = new XMLHttpRequest();
	xhr.open('POST', BASE_URL + ADD_URL, false);
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.setRequestHeader('X-CSRFToken', csrf_token);

	var body = 'from-whom=' + encodeURIComponent('browser') +
		'&nick=' + encodeURIComponent(nicknameField.value) +
		'&date=' + encodeURIComponent(((new Date()).toString()).substring(0, 15)) +
		'&language=' + encodeURIComponent(languageField.value) +
		'&facebook=' + encodeURIComponent(facebookField.value) +
		'&apple=' + encodeURIComponent(appleField.value) +
		'&google=' + encodeURIComponent(googleField.value) +
		'&time-in-game=' + encodeURIComponent(timeField.value) +
		'&number-of-sessions=' + encodeURIComponent(numberOfSessionsField.value) +
		'&session-time=' + encodeURIComponent(averageSessionTimeField.value);
	xhr.send(body);

	pageState.setId(-1);
	window.location.reload();
}

function removeAccount() {
	if (pageState.isValid()) {
		var xhr = new XMLHttpRequest();
		xhr.open('GET', BASE_URL + REMOVE_URL + `${pageState.getId()}/`, false);
		xhr.send();

		pageState.setId(-1);
		window.location.reload();
	}
}

function checkAddButton() {
	if (nicknameField.value.length == 0 || timeField.value.length == 0 ||
		numberOfSessionsField.value.length == 0 || averageSessionTimeField.value.length == 0) {
		if (!buttonAdd.hasAttribute('disabled'))
			buttonAdd.setAttribute('disabled', true);
	}
	else {
		if (buttonAdd.hasAttribute('disabled'))
			buttonAdd.removeAttribute('disabled');
	}
}

function controller(event) {
	switch(event.target.id) {
		case 'button-plus-1': {
			document.getElementById('gamer-level').value++;
			break;
		}
		case 'button-minus-1': {
			document.getElementById('gamer-level').value--;
			break;
		}
		case 'button-plus-2': {
			document.getElementById('gamer-coins').value++;
			break;
		}
		case 'button-minus-2': {
			document.getElementById('gamer-coins').value--;
			break;
		}
		case 'button-plus-3': {
			document.getElementById('gamer-crystals').value++;
			break;
		}
		case 'button-minus-3': {
			document.getElementById('gamer-crystals').value--;
			break;
		}
		case 'button-plus-4': {
			document.getElementById('gamer-energy').value++;
			break;
		}
		case 'button-minus-4': {
			document.getElementById('gamer-energy').value--;
			break;
		}
		case 'button-plus-5': {
			document.getElementById('gamer-inventory').value++;
			break;
		}
		case 'button-minus-5': {
			document.getElementById('gamer-inventory').value--;
			break;
		}
		case 'button-plus-6': {
			document.getElementById('gamer-consumables').value++;
			break;
		}
		case 'button-minus-6': {
			document.getElementById('gamer-consumables').value--;
			break;
		}
		case 'button-plus-7': {
			document.getElementById('gamer-skill').value++;
			break;
		}
		case 'button-minus-7': {
			document.getElementById('gamer-skill').value--;
			break;
		}
		case 'button-plus-8': {
			document.getElementById('gamer-payed').value++;
			break;
		}
		case 'button-minus-8': {
			document.getElementById('gamer-payed').value--;
			break;
		}
		case 'button-yes-1': {
			document.getElementById('gamer-paying').value = 'True';
			break;
		}
		case 'button-no-1': {
			document.getElementById('gamer-paying').value = 'False';
			break;
		}
		case 'button-yes-2': {
			document.getElementById('gamer-banned').value = 'True';

			var rowIndex = getTableRowFromId(pageState.getId());
			if (!tableData.rows[rowIndex].hasAttribute('banned'))
				tableData.rows[rowIndex].setAttribute('banned', true);

			break;
		}
		case 'button-no-2': {
			document.getElementById('gamer-banned').value = 'False';

			var rowIndex = getTableRowFromId(pageState.getId());
			if (tableData.rows[rowIndex].hasAttribute('banned'))
				tableData.rows[rowIndex].removeAttribute('banned');

			break;
		}
	}

	highlightRows();
}

function getIdFromTableRow(index) {
	return tableData.rows[index].cells[0].innerHTML;
}

function getTableRowFromId(id) {
	var rowIndex = 0;

	for (rowIndex = 1; rowIndex < tableData.rows.length; rowIndex++) {
		if (id == getIdFromTableRow(rowIndex))
			break;
	}

	return rowIndex;
}

function selectRow(event) {
	var currentId = getIdFromTableRow(event.currentTarget.rowIndex);
	pageState.setId(currentId);

	highlightRows();
	showGamerData();
	showGamerAnalytics();
	showStatistics();
}

function highlightRows() {
	for (var i = 1; i < tableData.rows.length; i++) {
		var selected = (pageState.getId() == getIdFromTableRow(i));
		var banned = tableData.rows[i].hasAttribute('banned');

		if (selected && banned) {
			tableData.rows[i].setAttribute('bgcolor', OVERLAY_COLOR);
		}
		else if (selected) {
			tableData.rows[i].setAttribute('bgcolor', SELECTED_COLOR);
		}
		else if (banned) {
			tableData.rows[i].setAttribute('bgcolor', BANNED_COLOR);
		}
		else {
			if (tableData.rows[i].hasAttribute('bgcolor'))
				tableData.rows[i].removeAttribute('bgcolor');
		}
	}
}

function showGamerData() {
	if (!pageState.isValid()) {
		document.getElementById('gamer-level').value = '';
		document.getElementById('gamer-coins').value = '';
		document.getElementById('gamer-crystals').value = '';
		document.getElementById('gamer-energy').value = '';
		document.getElementById('gamer-inventory').value = '';
		document.getElementById('gamer-consumables').value = '';
		document.getElementById('gamer-skill').value = '';
		document.getElementById('gamer-payed').value = '';
		document.getElementById('gamer-paying').value = '';
		document.getElementById('gamer-banned').value = '';

		for (var i = 0; i < buttons.length; i++) {
			if (!buttons[i].hasAttribute('disabled'))
				buttons[i].setAttribute('disabled', true);
		}

		return;
	}

	for (var i = 0; i < buttons.length; i++) {
		if (buttons[i].hasAttribute('disabled'))
			buttons[i].removeAttribute('disabled');
	}

	var xhr = new XMLHttpRequest();
	xhr.open('GET', BASE_URL + INFO_URL + `${pageState.getId()}/`, false);
	xhr.send();

	data = JSON.parse(xhr.responseText);

	document.getElementById('gamer-level').value = data.level;
	document.getElementById('gamer-coins').value = data.coins;
	document.getElementById('gamer-crystals').value = data.crystals;
	document.getElementById('gamer-energy').value = data.energy;
	document.getElementById('gamer-inventory').value = data.inventory;
	document.getElementById('gamer-consumables').value = data.consumables;
	document.getElementById('gamer-skill').value = data.skill;
	document.getElementById('gamer-payed').value = data.payed;
	document.getElementById('gamer-paying').value = data.paying;
	document.getElementById('gamer-banned').value = data.banned;
}

function showGamerAnalytics() {
	if (!pageState.isValid()) {
		document.getElementById('analytics_active').value = '';
		document.getElementById('analytics_coefficient').value = '';
		document.getElementById('analytics_metrics').value = '';
		return;
	}

	var xhr = new XMLHttpRequest();
	xhr.open('GET', BASE_URL + ANALYTICS_URL + `${pageState.getId()}/`, false);
	xhr.send();

	data = JSON.parse(xhr.responseText)

	document.getElementById('analytics_active').value = data.active;
	document.getElementById('analytics_coefficient').value = data.coefficient;
	document.getElementById('analytics_metrics').value = data.metrics;
}

function showStatistics() {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', BASE_URL + STATISTICS_URL, false);
	xhr.send();

	data = JSON.parse(xhr.responseText)

	document.getElementById('all-gamers').value = data.count;
	document.getElementById('all-banned').value = data.banned;
	document.getElementById('all-paying').value = data.paying;
	document.getElementById('all-active').value = data.active;
	document.getElementById('all-money').value = data.money;
}

window.onload = function() {
	showStatistics();
	showGamerData();
	showGamerAnalytics();
	highlightRows();
}

for (var i = 1; i < tableData.rows.length; i++) {
	tableData.rows[i].addEventListener('click', selectRow);
}

numberField.addEventListener('input', checkAddButton);
nicknameField.addEventListener('input', checkAddButton);
timeField.addEventListener('input', checkAddButton);
numberOfSessionsField.addEventListener('input', checkAddButton);
averageSessionTimeField.addEventListener('input', checkAddButton);

buttonSave.addEventListener('click', saveAccount);
buttonAdd.addEventListener('click', addAccount);
buttonRemove.addEventListener('click', removeAccount);

for (var i = 2; i < buttons.length; i++) {
	buttons[i].addEventListener('click', controller);
}

//alert('Success!');
