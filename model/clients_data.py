# coding=utf-8


class ClientData:
    def __init__(self, clients=None):
        self.clients = clients


class Client:
    def __init__(self, name=None, regulationTypeID=None, lang=None, currencies=None):
        self.name = name
        self.regulationTypeID = regulationTypeID
        self.lang = lang
        self.currencies = currencies