import sqlalchemy as sa
from up.data.modelbase import ModelBase

class Urlaubsziel(ModelBase):
    __tablename__ = 'Urlaubsziel'
    # Spaltendefinitionen
    uzid = sa.Column("uzid", sa.Integer, primary_key=True, autoincrement=True)
    land = sa.Column('land', sa.String, nullable=False)
    ort = sa.Column('ort', sa.String, nullable= False )
    distanz = sa.Column('distanz', sa.Integer, nullable=False)
    transportmittel = sa.Column('transportmittel', sa.String, nullable=False)
    kostenrahmen = sa.Column('kostenrahmen', sa.String, nullable=False)
    kurzbeschreibung = sa.Column('kurzbeschreibung', sa.String, nullable=False)
    startdatum=sa.Column('startdatum', sa.String, nullable=False)
    enddatum=sa.Column('enddatum', sa.String, nullable=False)

    # Beziehung zu anderen Tabelle
    persons = sa.orm.relationship('Vorschlaege', back_populates='urlaubsziele')

    # Methode zum Konvertieren des Objekts in ein Wörterbuch
    def to_dict(self):
        return dict(uzid=self.uzid,
                    land=self.land,
                    ort=self.ort,
                    distanz=self.distanz,
                    transportmittel=self.transportmittel,
                    kostenrahmen=self.kostenrahmen,
                    kurzbeschreibung=self.kurzbeschreibung,
                    startdatum= self.startdatum,
                    enddatum= self.enddatum)


