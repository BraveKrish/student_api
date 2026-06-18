from sqlmodel import SQLModel

class StudentBase(SQLModel):
    name: str
    email: str
    course: str
    age: int

class StudentCreate(StudentBase):
    pass

# public schema
class StudentRead(StudentBase):
    id: int

class StudentUpdate(SQLModel):
    name: str | None = None
    email: str | None = None
    course: str | None = None
    age: int | None = None