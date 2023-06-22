import json
import falcon
from up.relation.VorschlagService import VorschlagService

class VorschlagRessource:

    # Behandelt POST-Anfragen an den Endpunkt /vorschlag.
    # Erstellt einen neuen Vorschlag anhand der JSON-Daten im Anfragekörper.
    def on_post_vorschlag(self, req, resp):
        vorschlag_json = json.load(req.bounded_stream)
        VorschlagService.create_vorschlag(vorschlag_json)
        resp.text = "Vorschlag added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    # Behandelt GET-Anfragen an den Endpunkt /vorschlaege.
    # Ruft die Liste aller Vorschläge ab und gibt sie als JSON-Antwort zurück.
    def on_get_vorschlaege(self, req, resp):
        vorschlag_list = VorschlagService.get_vorschlaege()
        resp.text = json.dumps([p.to_dict() for p in vorschlag_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    # Behandelt DELETE-Anfragen an den Endpunkt /vorschlag/{uzid}/{pid}.
    # Löscht den Vorschlag mit der angegebenen ID
    def on_delete_vorschlag(self, req, resp, uz_uzid, person_id):
        VorschlagService.delete_vorschlag(int(person_id), int(uz_uzid))
        resp.text = f"Vorschlag {uz_uzid} von Person {person_id}  deleted successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    # Behandelt PUT-Anfragen an den Endpunkt /vorschlag/{uzid}/{pid}.
    # Aktualisiert den Vorschlag mit der angegebenen ID anhand der JSON-Daten im Anfragekörper
    def on_put_vorschlag(self, req, resp, uz_uzid, person_id):
        vorschlag_json = json.load(req.bounded_stream)
        VorschlagService.update_vorschlag(int(uz_uzid), int(person_id), vorschlag_json)
        resp.text = f"Vorschlag {uz_uzid} von Person {person_id} updated successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    # Behandelt GET-Anfragen an den Endpunkt /sortiertprio.
    # Ruft die Liste aller Vorschläge sortiert nach Prio ab und gibt sie als JSON-Antwort zurück.
    def on_get_sortiertprio(self, req, resp):
        vorschlag_prio_list = VorschlagService.get_sortiertprio()
        vorschlag_dict_list = [v.to_dict_2() for v in vorschlag_prio_list]# if isinstance(v, Vorschlaege)]
        resp.text = json.dumps(vorschlag_dict_list, ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

