import json
import falcon

from up.person.PersonService import PersonService


class PersonRessource:
    def on_get_persons(self, req, resp):
        person_list = PersonService.get_persons()
        resp.text = json.dumps([p.to_dict() for p in person_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_person(self, req, resp, pid):
        resp.text = None
        p = PersonService.get_person(int(pid))
        resp.text = json.dumps(p.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_post_person(self, req, resp):
        person_json = json.load(req.bounded_stream)
        PersonService.create_person(person_json)
        resp.text = "Person added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_person(self, req, resp, pid):
        person_json = json.load(req.bounded_stream)
        PersonService.update_person(int(pid), person_json)
        resp.text = f"Person with the ID {pid} updated successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_delete_person(self, req, resp, pid):
        PersonService.delete_person(int(pid))
        resp.text = f"Person with the ID {pid} deleted successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT



