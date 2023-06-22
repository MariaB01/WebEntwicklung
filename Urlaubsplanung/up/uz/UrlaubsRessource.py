import json
import falcon
from up.uz.UrlaubsService import UrlaubsService

class UrlaubRessource:
    def on_get_urlaubsziele(self, req, resp):
        #Behandelt GET-Anfragen für die URL "/urlaubsziele" und gibt eine Liste der Urlaubsziele zurück.
        urlaub_list = UrlaubsService.get_urlaubsziele()
        resp.text = json.dumps([v.to_dict() for v in urlaub_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_urlaubsziel(self, req, resp, uzid):
        #Behandelt GET-Anfragen für die URL "/urlaubsziel/{uzid}" und gibt das Urlaubsziel mit der angegebenen ID zurück.
        resp.text = None
        uz = UrlaubsService.get_urlaubsziel(int(uzid))
        resp.text = json.dumps(uz.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_post_urlaubsziel(self, req, resp):
        #Behandelt POST-Anfragen für die URL "/urlaubsziel" und erstellt ein neues Urlaubsziel mit den angegebenen Daten.
        uz_json = json.load(req.bounded_stream)
        UrlaubsService.create_urlaubsziel(uz_json)
        resp.text = "Urlaubsziel added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_urlaubsziel(self, req, resp, uzid):
        #Behandelt PUT-Anfragen für die URL "/urlaubsziel/{uzid}" und aktualisiert das Urlaubsziel mit der angegebenen ID.
        uz_json = json.load(req.bounded_stream)
        UrlaubsService.update_urlaubsziel(int(uzid), uz_json)
        resp.text = f"Urlaubsziel with the ID {uzid} updated successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_delete_urlaubsziel(self, req, resp, uzid):
        # Behandelt DELETE-Anfragen für die URL "/urlaubsziel/{uzid}" und löscht das Urlaubsziel mit der angegebenen ID.
        UrlaubsService.delete_urlaubsziel(int(uzid))
        resp.text = f"Urlaubsziel with the ID {uzid} deleted successfully!"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT
