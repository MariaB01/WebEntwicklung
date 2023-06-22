import sqlalchemy as sa
from up.data.modelbase import ModelBase

class Person(ModelBase):
    __tablename__ = "Person"

    # Spaltendefinitionen
    pid = sa.Column('pid', sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column('name', sa.String, nullable=False)

    # Beziehung zu anderen Tabelle
    urlaubsziele = sa.orm.relationship('Vorschlaege', back_populates='person')

    # Methode zum Konvertieren des Objekts in ein Wörterbuch
    def to_dict(self):
        return dict(pid=self.pid,
                    name=self.name
                    )
