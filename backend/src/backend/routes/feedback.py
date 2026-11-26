from datetime import datetime

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.database.connection import get_db
from backend.models.feedback import Feedback
from backend.services.feedback_ingestion import import_feedback_csv
from backend.services.feedback_analytics import (
    calculate_feedback_summary,
    calculate_category_counts,
    calculate_sentiment_distribution,
    calculate_rating_distribution,
    calculate_trends,
)
from backend.handler.error_handler import AppException, app_exception_handler
from backend.handler.messages import BAD_REQUEST, custom_message
from backend.handler.status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from backend.handler.error import Error

router = APIRouter(prefix="/feedback", tags=["Feedback"])


@router.post("/import")
async def import_feedback(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith(".csv"):
        raise AppException(
            Error(
                status_code=HTTP_400_BAD_REQUEST,
                message=custom_message("Only CSV files are supported"),
            )
        )

    content = await file.read()

    return import_feedback_csv(db, content)


@router.get("")
def get_feedback(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    db: Session = Depends(get_db),
):
    if start_date and end_date and start_date >= end_date:
        raise HTTPException(
            status_code=400, detail="start_date must be earlier than end_date"
        )

    statement = select(Feedback)

    if start_date:
        statement = statement.where(Feedback.created_at >= start_date)

    if end_date:
        statement = statement.where(Feedback.created_at < end_date)

    statement = statement.order_by(Feedback.created_at.desc())

    return db.scalars(statement).all()


@router.get("/summary")
def feedback_summary(db: Session = Depends(get_db)):

    return {
        **calculate_feedback_summary(db),
        "sentiment_distribution": calculate_sentiment_distribution(db),
        "rating_distribution": calculate_rating_distribution(db),
        "trends": calculate_trends(db),
    }


@router.get("/categories")
def feedback_categories(db: Session = Depends(get_db)):

    return calculate_category_counts(db)
