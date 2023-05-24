from wsgiref.simple_server import make_server
import falcon

# class TestRessource:
#     def on_get(self, req, resp):
#         resp.text = "Hello folks!"
#         resp.status = falcon.HTTP_200
#
#     def on_get_whoami(self, req, resp):
#         resp.text = "I am your computer"
#         resp.status = falcon.HTTP_200
#
#     def on_get_bye(self, req, resp):
#         resp.text = "Adios!"
#         resp.status = falcon.HTTP_200
#
#     def on_get_goodnight(self, req, resp):
#         resp.text = "Schlaf gut!"
#         resp.status = falcon.HTTP_200
#
#
# app = application = falcon.App()
# res = TestRessource()
#
# app.add_route("/", res)
# app.add_route("/who", res, suffix="whoami")
# app.add_route("/bye", res, suffix="bye")
# app.add_route("/goodnight", res, suffix="goodnight")
#
# if __name__ == "__main__":
#     with make_server("", 8081, app) as httpd:
#         print("Serving on port 8081...")
#
#         httpd.serve_forever()

#from fh.aalen.video.VideoController import VideoController
#from fh.aalen.video.VideoRessource import VideoRessource
from up.uz.UrlaubsController import UrlaubsController
from up.uz.UrlaubsRessource import UrlaubRessource
from up.person.PersonController import PersonController
from up.person.PersonRessource import PersonRessource
from up.relation.VorschlagRessource import VorschlagRessource
from up.relation.VorschlagController import VorschlagController


app = application = falcon.App()
#video_ressource = VideoRessource()
uz_ressource = UrlaubRessource()
uz_controller = UrlaubsController(app, uz_ressource)
person_ressource = PersonRessource()
#video_controller = VideoController(app, video_ressource)
person_controller = PersonController(app, person_ressource)

vorschlag_ressource = VorschlagRessource()
vorschlag_controller = VorschlagController(app, vorschlag_ressource )

if __name__ == '__main__':
    with make_server("", 8082, app) as httpd:
        print("Serving on port 8082...")

        httpd.serve_forever()