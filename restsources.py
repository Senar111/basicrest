from typing import Dict

from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)
klienci = [
    {
        "klientName": "Mikolaj_kolataj",
        "klient_adres": "Rzepakowa 61"
    },
    {
        "klientName": "Andzrej_kowalczyk",
        "klient_adres": "Bez nadziei 111"

    },
    {
        "klientName": "Karol_tengri",
        "klient_adres": "Swieta 2137"
    }
]
def memento_logger(type,logact):
    memento_writer(type,logact)
def memento_writer(type,logact):
    log = open("log.txt","a")
    log.write(type + " ")
    log.write(str(logact) + "\n")
@app.route('/klient')
def klint():
    return json.dumps(klienci)


uslugi = [
    {
        "uslug_id": "Nap-urz-el",
        "uslug_name": "Naprawa urzadzenia elektrycznego",
        "uslug_cost": 450.00
    },
    {
        "uslug_id": "Nap-Dor",
        "uslug_name": "Doradztwo Techniczne",
        "uslug_cost": 150.00
    },
    {
        "uslug_id": "Nap-urz-gaz",
        "uslug_name": "Naprawa urzadzenia gazowego",
        "uslug_cost": 1050.00
    }
]


@app.route('/usluga')
def serw():
    return json.dumps(uslugi)


zlecenia = [
    {
        "zlec_id": 210212001,
        "zlec_klient": "Mikolaj_kolataj",
        "zlec_uslug": "Nap-urz-gaz"
    },
    {
        "zlec_id": 210212002,
        "zlec_klient": "Karol_tengri",
        "zlec_uslug": "Nap-Dor",
    },
    {
        "zlec_id": 210212003,
        "zlec_klient": "Andzrej_kowalczyk",
        "zlec_uslug": "Nap-urz-el"
    },
]


@app.route('/zlecenie')
def zlec():
    return json.dumps(zlecenia)


class klient(Resource):
    def get(self, klientName):
        klient: dict[str, str]
        for klient in klienci:
            if klient["klientName"] == klientName:
                return klient, 200
        return "Nie znaleziono klienta", 404

    def post(self, klientName):
        parser = reqparse.RequestParser()
        parser.add_argument("klient_adres", required=True, help="wyslij adres")
        args = parser.parse_args()

        for klient in klienci:
            if (klientName == klient["klientName"]):
                return "Taki klient juz istnieje", 409

        klient = {
            "klientName": klientName,
            "klient_adres": args["klient_adres"]
        }
        klienci.append(klient)
        memento_logger("post",klient)
        return klient, 201

    def put(self, klientName):
        parser = reqparse.RequestParser()
        parser.add_argument("klient_adres", required=True, help="wyslij adres")
        args = parser.parse_args()

        for klient in klienci:
            if klientName == klient["klientName"]:
                klient["klientName"] = klientName
                klient["klient_adres"] = args["klient_adres"]
                return klient, 200
        memento_logger("put",klient)
        klienci.append(klient)
        return klient, 201

    def delete(self, klientName):
        global klienci
        x = [klient for klient in klienci if klient["klientName"] == klientName]
        for zlecenie in zlecenia:
            if zlecenie["klientName"] == klientName:
                return "{} nie moze zostac usuniety z powodu przypisanego zlecenia.".format(x), 409
        klienci = [klient for klient in klienci if klient["klientName"] != klientName]
        memento_logger("delete", klientName)
        return "{} zostal usuniety.".format(x), 200


class usluga(Resource):
    def get(self, uslug_id):
        for usluga in uslugi:
            if usluga["uslug_id"] == uslug_id:
                return usluga, 200
        return "Nie znaleziono uslugi", 404

    def post(self, uslug_id):
        parser = reqparse.RequestParser()
        parser.add_argument("uslug_name", required=True, help="wyslij nazwe uslugi")
        parser.add_argument("uslug_cost", required=True, help="wyślij cene uslugi")
        args = parser.parse_args()

        for usluga in uslugi:
            if (args["uslug_name"] == usluga["uslug_name"]):
                return "Taka usluga juz istnieje", 409

        usluga = {
            "uslug_id": uslug_id,
            "uslug_name": args["uslug_name"],
            "uslug_cost": args["uslug_cost"]
        }
        uslugi.append(usluga)
        memento_logger("post",usluga)
        return usluga, 201

    def put(self, uslug_id):
        parser = reqparse.RequestParser()
        parser.add_argument("uslug_name", required=True, help="wyslij nazwe uslugi")
        parser.add_argument("uslug_cost", required=True, help="wyślij cene uslugi")
        args = parser.parse_args()

        for usluga in uslugi:
            if uslug_id == usluga["uslug_id"]:
                usluga["uslug_name"] = args["uslug_name"]
                usluga["uslug_cost"] = args["uslug_cost"]
                return usluga, 200

        klienci.append(uslug_id)
        memento_logger("put", usluga)
        return usluga, 201

    def delete(self, uslug_id):
        global uslugi
        x = [usluga for usluga in uslugi if usluga["uslug_id"] == uslug_id]
        for zlecenie in zlecenia:
            if zlecenie["uslug_id"] == uslug_id:
                return "{} nie moze zostac usuniety z powodu przypisanego zlecenia.".format(x), 409
        uslugi = [usluga for usluga in uslugi if usluga["uslug_id"] != uslug_id]
        memento_logger("post", uslug_id)
        return "{} zostala usunieta.".format(x), 200


class zlecenie(Resource):
    def get(self, zlec_id):
        for zlecenie in zlecenia:
            if zlecenie["zlec_id"] == zlec_id:
                memento_logger("get",zlecenie)
                return zlecenie, 200
        return "Nie znaleziono zlecenia", 404

    def post(self, zlec_id):
        parser = reqparse.RequestParser()
        parser.add_argument("zlec_klient", required=True, help="wyslij imie klienta")
        parser.add_argument("zlec_uslug", required=True, help="wyslij id uslugi")
        args = parser.parse_args()
        for zlecenie in zlecenia:
            if (zlec_id == zlecenie["zlec_id"]):
                return "Takie zlecenie juz istnieje", 409
        warunek = False # idiotyczne ale dziala
        for klient in klienci:  # Żeby nie można było dodać z zlym klientem/usluga
            if args["zlec_klient"] == klient["klientName"]:
                warunek = True
        if warunek == False:
            return "{} Nie ma takiego klienta".format(args["zlec_klient"]), 409
        warunek = False
        for usluga in uslugi:
            if args["zlec_uslug"] == usluga["uslug_id"]:
                warunek = True
        if warunek == False:
            return "{} Nie ma takiej uslugi".format(args["zlec_uslug"]), 409
        zlecenie = {
            "zlec_id": zlec_id,
            "zlec_klient": args["zlec_klient"],
            "zlec_uslug": args["zlec_uslug"]
        }
        zlecenia.append(zlecenie)
        memento_logger("post",zlecenie)
        return zlecenie, 201

    def put(self, zlec_id):
        parser = reqparse.RequestParser()
        parser.add_argument("zlec_klient", required=True, help="wyslij imie klienta")
        parser.add_argument("zlec_uslug", required=True, help="wyslij id uslugi")
        args = parser.parse_args()
        warunek = False # idiotyczne ale dziala
        for klient in klienci:  # Żeby nie można było dodać z zlym klientem/usluga
            if args["zlec_klient"] == klient["klientName"]:
                warunek = True
        if warunek == False:
            return "{} Nie ma takiego klienta".format(args["zlec_klient"]), 409
        warunek = False
        for usluga in uslugi:
            if args["zlec_uslug"] == usluga["uslug_id"]:
                warunek = True
        if warunek == False:
            return "{} Nie ma takiej uslugi".format(args["zlec_uslug"]), 409
        for zlecenie in zlecenia:
            if zlec_id == zlecenie["zlec_id"]:
                zlecenie["zlec_klient"] = args["zlec_klient"]
                zlecenie["zlec_uslug"] = args["zlec_uslug"]
                memento_logger("put", zlecenie)
                return zlecenie, 200

        klienci.append(zlec_id)
        return zlecenie, 201

    def delete(self, zlec_id):
        global zlecenia
        x = [zlecenie for zlecenie in zlecenia if zlecenie["zlec_id"] == zlec_id]
        zlecenia = [zlecenie for zlecenie in zlecenia if zlecenie["zlec_id"] != zlec_id]
        memento_logger("delete", zlec_id)
        return "zlecenie {} zostalo usuniete.".format(x), 200


api.add_resource(klient, "/klient/<string:klientName>")
api.add_resource(usluga, "/usluga/<string:uslug_id>")
api.add_resource(zlecenie, "/zlecenie/<int:zlec_id>")

app.run(debug=True)
