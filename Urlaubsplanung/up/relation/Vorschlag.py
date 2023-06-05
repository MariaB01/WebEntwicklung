import sqlalchemy as sa
from sqlalchemy.orm import relationship

from up.data.modelbase import ModelBase


class Vorschlaege(ModelBase):
    __tablename__ = 'Vorschlaege'

    uz_uzid = sa.Column(sa.ForeignKey('Urlaubsziel.uzid'), primary_key=True)
    person_id = sa.Column(sa.ForeignKey('Person.pid'), primary_key=True)
    urlaubsziele = relationship('Urlaubsziel', back_populates='persons')
    person = relationship('Person', back_populates='urlaubsziele')
    prio = sa.Column('prio', sa.Integer, nullable=False)

    def to_dict(self):
        return dict(uz_uzid=self.uz_uzid,
                    person_id=self.person_id,
                    prio=self.prio)

class PrioData:
    def __init__(self, uz_uzid, vorschlaege_person_id, vorschlaege_prio):
        self.uz_uzid = uz_uzid
        self.person_id = vorschlaege_person_id
        self.prio = vorschlaege_prio

    def to_dict_2(self):
        return dict(uz_uzid=self.uz_uzid,
                    person_id=self.person_id,
                    prio=self.prio)
