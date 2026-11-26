from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.models.feedback import Feedback


def create_feedback(db: Session, feedback: Feedback):
    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback


def get_feedback_by_id(db: Session, feedback_id):
    statement = select(Feedback).where(Feedback.id == feedback_id)

    return db.scalar(statement)


def get_feedback_by_date_range(
    db: Session,
    start_date: datetime,
    end_date: datetime,
):
    statement = (
        select(Feedback)
        .where(Feedback.created_at >= start_date, Feedback.created_at < end_date)
        .order_by(Feedback.created_at.desc())
    )

    return db.scalars(statement).all()
