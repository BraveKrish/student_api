from sqlmodel import SQLModel, create_engine

DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_practice_student_api"

# create engine: handle connection with database
engine = create_engine(
    DATABASE_URL,
    echo= True
)

# create table and database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



