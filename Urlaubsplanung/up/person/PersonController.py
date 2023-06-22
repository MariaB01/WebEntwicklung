class PersonController:
    # Der Konstruktor der PersonController-Klasse
    def __init__(self, app, res):
        self.app = app  # Die Flask-App, mit der der Controller verknüpft ist
        self.res = res  # Die Ressourcenklasse, die die Anfragen verarbeitet
        # Routen hinzufügen
        self.app.add_route("/persons", self.res, suffix="persons")
        self.app.add_route("/person/{pid}", self.res, suffix="person")
        self.app.add_route("/person", self.res, suffix="person")
