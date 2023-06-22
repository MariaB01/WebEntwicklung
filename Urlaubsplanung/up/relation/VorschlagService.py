from sqlalchemy import func
from up.data.dbsession import DBSession
from up.relation.Vorschlag import Vorschlaege
from up.relation.Vorschlag import PrioData

class VorschlagService:

    @classmethod
    def __json_to_vorschlag(cls, vorschlag, json_vorschlag):
        #Konvertiert ein JSON-Objekt in ein Vorschlag-Objekt.
        # :param vorschlag: Das Vorschlag-Objekt, das aktualisiert wird.
        # :param json_vorschlag: Das JSON-Objekt, aus dem die Daten gelesen werden.
        # :return: Das aktualisierte Vorschlag-Objekt.
        vorschlag.uz_uzid = json_vorschlag["uz_uzid"]
        vorschlag.person_id = json_vorschlag["person_id"]
        vorschlag.prio = json_vorschlag["prio"]
        return vorschlag

    @classmethod
    def get_vorschlaege(cls):
        #Ruft alle Vorschläge aus der Datenbank ab.
        # :return: Eine Liste der Vorschläge
        session = DBSession.get_session()
        vorschlag_list = session.query(Vorschlaege).all()
        print(vorschlag_list)
        return vorschlag_list

    @classmethod
    def get_sortiertprio(cls):
        #Ruft eine sortierte Liste von Vorschlägen basierend auf der Prio-Summe ab.
        # :return: Eine Liste von PrioData-Objekten, die die sortierten Vorschläge repräsentieren.
        session = DBSession.get_session()
        prio_list = (
            session.query(Vorschlaege.uz_uzid, func.max(Vorschlaege.person_id).label('person_id'), func.sum(Vorschlaege.prio).label('prio'))
            .group_by(Vorschlaege.uz_uzid)
            .order_by(func.sum(Vorschlaege.prio).desc())
            .all()
        )
        prio_objects = [PrioData(uz_uzid, vorschlaege_person_id, vorschlaege_prio) for
                        uz_uzid, vorschlaege_person_id, vorschlaege_prio in prio_list]
        return prio_objects



    @classmethod
    def create_vorschlag(cls, json_vorschlag):
        #Erstellt einen neuen Vorschlag basierend auf den angegebenen Daten.
        # :param json_vorschlag: Das JSON-Objekt mit den Vorschlagsdaten.
        vorschlag = Vorschlaege()
        vorschlag = cls.__json_to_vorschlag(vorschlag, json_vorschlag)
        session = DBSession.get_session()
        session.add(vorschlag)
        session.commit()

    @classmethod
    def delete_vorschlag(cls, person_id, uz_uzid):
        #Löscht einen vorhandenen Vorschlag anhand der angegebenen Person-ID und UZ-ID.
        # :param person_id: Die ID der Person.
        # :param uz_uzid: Die UZ-ID.
        session = DBSession.get_session()
        vorschlag = session.query(Vorschlaege).filter_by(person_id=person_id, uz_uzid=uz_uzid).first()

        if vorschlag:
            session.delete(vorschlag)
            session.commit()
        else:
            pass


    @classmethod
    def update_vorschlag(cls, uz_uzid, person_id, vorschlag_data):
        # Updated einen vorhandenen Vorschlag anhand der angegebenen Person-ID und UZ-ID.
        # :param person_id: Die ID der Person.
        # :param uz_uzid: Die UZ-ID.
        session = DBSession.get_session()
        vorschlag = session.query(Vorschlaege).filter_by(uz_uzid=uz_uzid, person_id=person_id).first()

        if vorschlag:
            # Update Vorschlag mit neuen Daten
            vorschlag.prio = vorschlag_data['prio']
            session.commit()
        else:
            pass
