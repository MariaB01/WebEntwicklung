from up.uz.UrlaubsService import UrlaubsService

class UrlaubsController:

    def __init__(self, app, res):
        self.app = app
        self.res = res
        #self.urlaubsziel_service = UrlaubsService()

        # Routen registrieren
        self.app.add_route("/urlaubsziele", self.res, suffix="urlaubsziele")
        self.app.add_route("/urlaubsziel/{uzid}", self.res, suffix="urlaubsziel")
        self.app.add_route("/urlaubsziel", self.res, suffix="urlaubsziel")

        #self.app.add_route("/Urlaubsziel", self.res, suffix="urlaubsziele")
        #self.app.add_route("/Urlaubsziel/{uzid}", self.res, suffix="urlaubsziel")
        #self.app.add_route("/video", self.res, suffix="video")
        #self.app.add_route("/videosbygenre/{genre}", self.res, suffix="videosbygenre")
        #self.app.add_route("/videosbyagerating/{age_rating}", self.res, suffix="videosbyagerating")
        #self.app.add_route("/videogenres", self.res, suffix="videogenres")
        #self.app.add_route("/videonumbers", self.res, suffix="videonumbers")

        # self.app.add_static_route('/', 'C:/Users/ZBook/OneDrive/Studium/Dozent/Webentwicklung/Übungen/Rest-API')
        self.app.add_static_route('/', 'C:/Users/Admin/PycharmProjects/Urlaubsplanung')

