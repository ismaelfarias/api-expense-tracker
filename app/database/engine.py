from sqlmodel import create_engine, Session, SQLModel


DATABASE_URL = "mysql+pymysql://user_exp:password@db:3306/etracker_db"

engine = create_engine(DATABASE_URL, echo=True, future=True)   

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    with Session(engine) as session:
        yield session
