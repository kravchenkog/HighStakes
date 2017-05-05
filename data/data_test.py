import json
import os
import socket


def get_url(lang, currency, regulation_type_id):
    ip = socket.gethostbyname(socket.gethostname())
    game_type_id = 130008
    basic_url = "http://"+ip+"/Html5GamesForGGPMock/" + str(game_type_id) + "/Game/?gameData="
    game_data = {"integration": 1,
                 "gameId": 710,
                 "token": "1234567",
                 "url": "/mobile/default.aspx",
                 "jointype": 1,
                 "operatorid": 0,
                 "lang": lang,
                 "gametype": game_type_id,
                 "gamecurrencycode": currency,
                 "balance": 0,
                 "operatorxml": {"_888ClientData":
                                     {"ClientVersion": "Touch-0-EN-0-1.0-0-0",
                                      "ClientPlatform": 700,
                                      "ClientURL": "url",
                                      "BrandID": 0,
                                      "SubBrandID": 0,
                                      "ProductPackage": 37,
                                      "ClientType": 14,
                                      "GameLimits": -1,
                                      "EnableOperatorData": True,
                                      "IsFreePlay": 0,
                                      "RequestedGameLimit": -1,
                                      "RequestedTimeLimit": 0,
                                      "RestrictionPeriod": 0,
                                      "IntervalReminderInMinutes": 0}}}
    json_data = json.dumps(game_data)
    urla = basic_url + json_data
    return urla


def get_data_from_json_file():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../fixture')
    file = os.path.join(directory, "clients.json")
    data_from_json_file = json.load(open(file, 'r'))

    return data_from_json_file


def get_browsers_from_json():
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file = os.path.join(directory, "target.json")
    data = json.load(open(file, 'r'))

    return data


def get_parameters_from_json():
    all_client_data = get_data_from_json_file()
    target = get_browsers_from_json()
    parameters = []
    for browser in target['browser']:

        for client in all_client_data['clients']:
            i = 0
            for param in client['currencies']:
                parameters.append({browser: {client['lang']: [client['currencies'][i], client['regulationTypeID']]}})
                i += 1

    return parameters

testdata = get_parameters_from_json()
