import json
import falcon
from up.person.PersonService import PersonService


class PersonRessource:
#Behandelt GET-Anfragen an den Endpunkt /persons.
#Ruft die Liste aller Personen ab und gibt sie als JSON-Antwort zurück.
    def on_get_persons(self, req, resp):
        person_list = PersonService.get_persons()
        resp.text = json.dumps([p.to_dict() for p in person_list], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

#Behandelt GET-Anfragen an den Endpunkt /person/{pid}.
#Ruft die Person mit der angegebenen ID ab und gibt sie als JSON-Antwort zurück.
    def on_get_person(self, req, resp, pid):
        resp.text = None
        p = PersonService.get_person(int(pid))
        resp.text = json.dumps(p.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

#Behandelt POST-Anfragen an den Endpunkt /person.
# Erstellt eine neue Person anhand der JSON-Daten im Anfragekörper.
    def on_post_person(self, req, resp):
        person_json = json.load(req.bounded_stream)
        PersonService.create_person(person_json)
        resp.text = "Person added successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

# Behandelt PUT-Anfragen an den Endpunkt /person/{pid}.
#Aktualisiert die Person mit der angegebenen ID anhand der JSON-Daten im Anfragekörper
    def on_put_person(self, req, resp, pid):
        person_json = json.load(req.bounded_stream)
        PersonService.update_person(int(pid), person_json)
        resp.text = f"Person with the ID {pid} updated successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

# Behandelt DELETE-Anfragen an den Endpunkt /person/{pid}.
#Löscht die Person mit der angegebenen ID
    def on_delete_person(self, req, resp, pid):
        PersonService.delete_person(int(pid))
        resp.text = f"Person with the ID {pid} deleted successfully"
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT



