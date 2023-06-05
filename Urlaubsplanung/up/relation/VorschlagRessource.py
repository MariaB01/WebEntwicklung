import json
import falcon

from up.relation.VorschlagService import VorschlagService
from up.relation.Vorschlag import PrioData
from up.relation.Vorschlag import Vorschlaege

class VorschlagRessource:

    def on_post_vorschlag(self, req, resp):
        vorschlag_json = json.load(req.bounded_stream)
        VorschlagService.create_vorschlag(vorschlag_json)
        resp.text = "Vorschlag added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_get_adduzvorschlag(self, req, resp, person_id, uz_id):
        resp.text = None
        VorschlagService.add_urlaubsziel_to_Vorschlaege(person_id, uz_id)
        resp.text = "Vorschlag connected successfully"
        resp.status = falcon.HTTP_200


    def on_get_vorschlaege(self, req, resp):
        vorschlag_list = VorschlagService.get_vorschlaege()
        resp.text = json.dumps([p.to_dict() for p in vorschlag_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_delete_vorschlag(self, req, resp, uz_uzid, person_id):
        VorschlagService.delete_vorschlag(int(person_id), int(uz_uzid))
        resp.text = f"Vorschlag {uz_uzid} von Person {person_id}  deleted successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_vorschlag(self, req, resp, uz_uzid, person_id):
        vorschlag_json = json.load(req.bounded_stream)
        VorschlagService.update_vorschlag(int(uz_uzid), int(person_id), vorschlag_json)
        resp.text = f"Vorschlag {uz_uzid} von Person {person_id} updated successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_get_sortiertprio(self, req, resp):
        vorschlag_prio_list = VorschlagService.get_sortiertprio()
        print(vorschlag_prio_list)
        vorschlag_dict_list = [v.to_dict_2() for v in vorschlag_prio_list]# if isinstance(v, Vorschlaege)]
        print(vorschlag_dict_list)
        resp.text = json.dumps(vorschlag_dict_list, ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

