from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.student import Student

from app.schemas.student import (
    StudentCreate,
    StudentRead,
    StudentUpdate
)

from app.dependencies import get_session

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

SessionDep = Annotated[Session,Depends(get_session)]

@router.post("/", response_model=StudentRead)
def create_student(student: StudentCreate, session: SessionDep):
    db_student = Student.model_validate(student)
    session.add(db_student)
    session.commit()
    session.refresh(db_student)

    return db_student