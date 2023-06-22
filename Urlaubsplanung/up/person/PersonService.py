from up.person.Person import Person
from up.data.dbsession import DBSession

class PersonService:

# Konvertiert ein JSON-Objekt in ein Person-Objekt.
# :param person: Das Person-Objekt, das aktualisiert wird.
#:param json_person: Das JSON-Objekt, aus dem die Daten gelesen werden.
# :return: Das aktualisierte Person-Objekt.
    @classmethod
    def __json_to_person(cls, person, json_person):
        person.name = json_person["name"]
        return person

#Ruft alle Personen aus der Datenbank ab.
# :return: Eine Liste der Personen.
    @classmethod
    def get_persons(cls):
        session = DBSession.get_session()
        person_list = session.query(Person).all()
        return person_list

#Ruft eine einzelne Person anhand der angegebenen ID ab.
#:param pid: Die ID der Person.
#:return: Das Person-Objekt.
    @classmethod
    def get_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        return person

# Erstellt eine neue Person basierend auf den angegebenen Daten.
# :param json_person: Das JSON-Objekt mit den Personendaten.
    @classmethod
    def create_person(cls, json_person):
        person = Person()
        person = cls.__json_to_person(person, json_person)
        session = DBSession.get_session()
        session.add(person)
        session.commit()

#Aktualisiert eine vorhandene Person mit den angegebenen Daten.
#:param pid: Die ID der zu aktualisierenden Person.
#:param json_person: Das JSON-Objekt mit den aktualisierten Personendaten.
    @classmethod
    def update_person(cls, pid, json_person):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        cls.__json_to_person(person, json_person)
        session.commit()

# Löscht eine vorhandene Person anhand der angegebenen ID.
#:param pid: Die ID der zu löschenden Person.
    @classmethod
    def delete_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        session.delete(person)
        session.commit()

