import sqlalchemy as sa
import sqlalchemy.orm as orm
from up.data.modelbase import ModelBase


class DBSession:
    __session = None

    @classmethod
    def get_session(cls):
        if cls.__session != None:
            return cls.__session

        connection_string = "postgresql+psycopg2://postgres:bienenstich@localhost/urlaubsplanung"
        print(f"Connection to database: {connection_string}")

        engine = sa.create_engine(connection_string, echo=True)
        Session = orm.sessionmaker(bind=engine)
        cls.__session = Session()

        ModelBase.metadata.create_all(engine)
        return cls.__session
