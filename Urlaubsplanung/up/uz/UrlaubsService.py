from up.uz.Urlaubsziel import Urlaubsziel
from up.data.dbsession import DBSession

class UrlaubsService:
    @classmethod
    def __json_to_uz(cls, urlaubsziel, json_urlaubsziel):
        #Konvertiert JSON-Daten in ein Urlaubsziel-Objekt.
        urlaubsziel.land = json_urlaubsziel["land"]
        urlaubsziel.ort = json_urlaubsziel["ort"]
        urlaubsziel.distanz = json_urlaubsziel["distanz"]
        urlaubsziel.transportmittel = json_urlaubsziel["transportmittel"]
        urlaubsziel.kostenrahmen = json_urlaubsziel["kostenrahmen"]
        urlaubsziel.kurzbeschreibung= json_urlaubsziel['kurzbeschreibung']
        urlaubsziel.startdatum=json_urlaubsziel['startdatum']
        urlaubsziel.enddatum= json_urlaubsziel['enddatum']
        return urlaubsziel

    @classmethod
    def get_urlaubsziele(cls):
        #Holt alle Urlaubsziele aus der Datenbank.
        session = DBSession.get_session()
        uz_list = session.query(Urlaubsziel).all()
        return uz_list

    @classmethod
    def get_urlaubsziel(cls, uzid):
        #Holt das Urlaubsziel mit der angegebenen ID aus der Datenbank.
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        return uz


    @classmethod
    def create_urlaubsziel(cls, json_urlaubsziel):
    #Erstellt ein neues Urlaubsziel mit den angegebenen Daten und fügt es der Datenbank hinzu.
        uz = Urlaubsziel()
        uz = cls.__json_to_uz(uz, json_urlaubsziel)
        session = DBSession.get_session()
        session.add(uz)
        session.commit()


    @classmethod
    def update_urlaubsziel(cls, uzid, json_urlaubsziel):
        #Aktualisiert das Urlaubsziel mit der angegebenen ID anhand der gegebenen Daten.
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        cls.__json_to_uz(uz, json_urlaubsziel)
        session.commit()



    @classmethod
    def delete_urlaubsziel(cls, uzid):
        #Löscht das Urlaubsziel mit der angegebenen ID aus der Datenbank.
        session = DBSession.get_session()
        uz = session.query(Urlaubsziel).get(int(uzid))
        session.delete(uz)
        session.commit()





