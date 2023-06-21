import sqlalchemy as sa

from up.data.modelbase import ModelBase
from up.relation.Vorschlag import Vorschlaege



class Urlaubsziel(ModelBase):
    __tablename__ = 'Urlaubsziel'

    uzid = sa.Column("uzid", sa.Integer, primary_key=True, autoincrement=True)
    land = sa.Column('land', sa.String, nullable=False)
    ort = sa.Column('ort', sa.String, nullable= False )
    distanz = sa.Column('distanz', sa.Integer, nullable=False)
    #dauer = sa.Column('dauer', sa.String, nullable=False)
    #zeitraum = sa.Column('zeitraum', sa.String, nullable=False)
    transportmittel = sa.Column('transportmittel', sa.String, nullable=False)
    kostenrahmen = sa.Column('kostenrahmen', sa.String, nullable=False)
    kurzbeschreibung = sa.Column('kurzbeschreibung', sa.String, nullable=False)
    startdatum=sa.Column('startdatum', sa.String, nullable=False)
    enddatum=sa.Column('enddatum', sa.String, nullable=False)




    persons = sa.orm.relationship('Vorschlaege', back_populates='urlaubsziele')

    def to_dict(self):
        return dict(uzid=self.uzid,
                    land=self.land,
                    ort=self.ort,
                    distanz=self.distanz,
                    #dauer=self.dauer,
                    #zeitraum=self.zeitraum,
                    transportmittel=self.transportmittel,
                    kostenrahmen=self.kostenrahmen,
                    kurzbeschreibung=self.kurzbeschreibung,
                    startdatum= self.startdatum,
                    enddatum= self.enddatum)


