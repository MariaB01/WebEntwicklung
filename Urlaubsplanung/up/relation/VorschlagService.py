from up.person.Person import Person
from sqlalchemy import func
from up.data.dbsession import DBSession
from up.relation.Vorschlag import Vorschlaege

class VorschlagService:

    @classmethod
    def __json_to_vorschlag(cls, vorschlag, json_vorschlag):
        vorschlag.uz_uzid = json_vorschlag["uz_uzid"]
        vorschlag.person_id = json_vorschlag["person_id"]
        vorschlag.prio = json_vorschlag["prio"]
        return vorschlag

    @classmethod
    def add_urlaubsziel_to_Vorschlaege(cls, person_id, uz_id):
        session = DBSession.get_session()
        fav = Vorschlaege()
        fav.person_id = person_id
        fav.uz_uzid = uz_id
        session.add(fav)
        session.commit()


    @classmethod
    def get_vorschlaege(cls):
        session = DBSession.get_session()
        vorschlag_list = session.query(Vorschlaege).all()
        return vorschlag_list

    @classmethod
    def get_sortiertprio(cls):
        session = DBSession.get_session()
        prio_list = (
            session.query(Vorschlaege.uz_uzid, func.sum(Vorschlaege.prio))
            .group_by(Vorschlaege.uz_uzid)
            .order_by(func.sum(Vorschlaege.prio).desc())
            .all()
        )
        return prio_list



    @classmethod
    def create_vorschlag(cls, json_vorschlag):
        vorschlag = Vorschlaege()
        vorschlag = cls.__json_to_vorschlag(vorschlag, json_vorschlag)
        session = DBSession.get_session()
        session.add(vorschlag)
        session.commit()

    #@classmethod
    #def delete_vorschlag(cls, person_id, uz_uzid):
     #   session = DBSession.get_session()
      #  vorschlag = session.query(Vorschlaege).get(int(person_id), int(uz_uzid))
       # session.delete(vorschlag)
        #session.commit()

    @classmethod
    def delete_vorschlag(cls, person_id, uz_uzid):
        session = DBSession.get_session()
        vorschlag = session.query(Vorschlaege).filter_by(person_id=person_id, uz_uzid=uz_uzid).first()

        if vorschlag:
            session.delete(vorschlag)
            session.commit()
        else:
            pass

    #@classmethod
    #def update_vorschlag(cls, person_id, uz_uzid, json_vorschlag):
     #   session = DBSession.get_session()
      #  vorschlag = session.query(Vorschlaege).get(int(person_id), int(uz_uzid))
       # cls.__json_to_vorschlag(vorschlag, json_vorschlag)
        #session.commit()
    @classmethod
    def update_vorschlag(cls, uz_uzid, person_id, vorschlag_data):
        session = DBSession.get_session()

        vorschlag = session.query(Vorschlaege).filter_by(uz_uzid=uz_uzid, person_id=person_id).first()

        if vorschlag:
            # Update the vorschlag object with new data
          #  vorschlag.uz_uzid = vorschlag_data['uz_uzid']
           # vorschlag.person_id = vorschlag_data['person_id']
            vorschlag.prio = vorschlag_data['prio']
            # ...

            session.commit()
        else:
            # Handle error or raise exception if vorschlag is not found
            pass
