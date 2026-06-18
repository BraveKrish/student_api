from sqlmodel import Session
from app.database import engine

# create session dependencies
def get_session():
    with Session(engine) as session:
        yield session