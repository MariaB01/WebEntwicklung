class VorschlagController:
    # Der Konstruktor der Vorschlag-Klasse
    def __init__(self, app, res):
        self.app = app  #Die Flask-App, mit der der Controller verknüpft ist
        self.res = res  #Die Ressourcenklasse, die die Anfragen verarbeitet
        self.app.add_route("/vorschlaege", self.res, suffix="vorschlaege")
        self.app.add_route("/vorschlag", self.res, suffix="vorschlag")
        self.app.add_route("/vorschlag/{person_id}/{uz_uzid}", self.res, suffix="vorschlag")
        self.app.add_route("/sortiertprio", self.res, suffix="sortiertprio")