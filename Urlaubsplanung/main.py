from wsgiref.simple_server import make_server
import falcon
from up.uz.UrlaubsController import UrlaubsController
from up.uz.UrlaubsRessource import UrlaubRessource
from up.person.PersonController import PersonController
from up.person.PersonRessource import PersonRessource
from up.relation.VorschlagRessource import VorschlagRessource
from up.relation.VorschlagController import VorschlagController

# Erstelle eine neue Falcon-Anwendung
app = application = falcon.App()

# Instanziere Ressourcen und Controller
uz_ressource = UrlaubRessource()
uz_controller = UrlaubsController(app, uz_ressource)
person_ressource = PersonRessource()
person_controller = PersonController(app, person_ressource)
vorschlag_ressource = VorschlagRessource()
vorschlag_controller = VorschlagController(app, vorschlag_ressource )

# Überprüfe, ob das Skript direkt ausgeführt wird
if __name__ == '__main__':
    # Erstelle einen HTTP-Server und starte ihn auf Port 8082
    with make_server("", 8082, app) as httpd:
        print("Serving on port 8082...")
        # Starte den Server und warte auf Anfragen
        httpd.serve_forever()