import sqlalchemy as sa

from up.data.modelbase import ModelBase


from up.relation.Vorschlag import Vorschlaege


class Person(ModelBase):
    __tablename__ = "Person"

    pid = sa.Column('pid', sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column('name', sa.String, nullable=False)
  #  age = sa.Column('age', sa.String, nullable=False)
   # gender = sa.Column('gender', sa.String, nullable=False)
    #fit = sa.Column('fitnesslevel', sa.String, nullable=False)

    urlaubsziele = sa.orm.relationship('Vorschlaege', back_populates='person')

    def to_dict(self):
        return dict(pid=self.pid,
                    name=self.name
                    #age=self.age,
                    #gender=self.gender,
                    #fit=self.fit
                    )
