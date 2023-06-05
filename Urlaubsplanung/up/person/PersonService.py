from up.person.Person import Person
from up.data.dbsession import DBSession
from up.relation.Vorschlag import Vorschlaege


class PersonService:
    @classmethod
    def __json_to_person(cls, person, json_person):
        person.name = json_person["name"]
       # person.age = json_person["age"]
       # person.gender = json_person["gender"]
        #person.fit = json_person["fit"]

        return person

    @classmethod
    def get_persons(cls):
        session = DBSession.get_session()
        person_list = session.query(Person).all()
        return person_list

    @classmethod
    def get_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        print(person)
        return person

    @classmethod
    def create_person(cls, json_person):
        person = Person()
        person = cls.__json_to_person(person, json_person)
        session = DBSession.get_session()
        session.add(person)
        session.commit()

    @classmethod
    def update_person(cls, pid, json_person):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        cls.__json_to_person(person, json_person)
        session.commit()

    @classmethod
    def delete_person(cls, pid):
        session = DBSession.get_session()
        person = session.query(Person).get(int(pid))
        session.delete(person)
        session.commit()

