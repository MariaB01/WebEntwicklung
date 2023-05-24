from up.person.Person import Person
from up.uz.Urlaubsziel import Urlaubsziel
from up.data.dbsession import DBSession

class UrlaubsService:
    @classmethod
    def __json_to_uz(cls, urlaubsziel, json_urlaubsziel):
        urlaubsziel.land = json_urlaubsziel["land"]
        urlaubsziel.ort = json_urlaubsziel["ort"]
        urlaubsziel.distanz = json_urlaubsziel["distanz"]
        urlaubsziel.dauer = json_urlaubsziel["dauer"]
        urlaubsziel.zeitraum = json_urlaubsziel["zeitraum"]
        urlaubsziel.transportmittel = json_urlaubsziel["transportmittel"]
        urlaubsziel.kostenrahmen = json_urlaubsziel["kostenrahmen"]
        return urlaubsziel

    @classmethod
    def get_urlaubsziele(cls):
        session = DBSession.get_session()
        uz_list = session.query(Urlaubsziel).all()
        return uz_list

    @classmethod
    def get_urlaubsziel(cls, uzid):
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        return uz


    @classmethod
    def create_urlaubsziel(cls, json_urlaubsziel):
        uz = Urlaubsziel()
        uz = cls.__json_to_uz(uz, json_urlaubsziel)
        session = DBSession.get_session()
        session.add(uz)
        session.commit()


    @classmethod
    def update_urlaubsziel(cls, uzid, json_urlaubsziel):
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        cls.__json_to_uz(uz, json_urlaubsziel)
        session.commit()



    @classmethod
    def delete_urlaubsziel(cls, uzid):
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        session.delete(uz)
        session.commit()





