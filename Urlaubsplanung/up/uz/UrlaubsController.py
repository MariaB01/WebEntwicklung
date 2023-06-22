class UrlaubsController:
    # Der Konstruktor der Urlaubsziel-Klasse
    def __init__(self, app, res):
        self.app = app # Die Flask-App, mit der der Controller verknüpft ist
        self.res = res # Die Ressourcenklasse, die die Anfragen verarbeitet
        # Routen registrieren
        self.app.add_route("/urlaubsziele", self.res, suffix="urlaubsziele")
        self.app.add_route("/urlaubsziel/{uzid}", self.res, suffix="urlaubsziel")
        self.app.add_route("/urlaubsziel", self.res, suffix="urlaubsziel")

        self.app.add_static_route('/', 'C:/Users/Admin/PycharmProjects/Urlaubsplanung')

