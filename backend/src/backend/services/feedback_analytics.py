from sqlalchemy import func, literal_column, select
from sqlalchemy.orm import Session

from backend.models.feedback import Feedback


def calculate_category_counts(db):

    statement = (
        select(Feedback.category, func.count(Feedback.id).label("total"))
        .group_by(Feedback.category)
        .order_by(func.count(Feedback.id).desc())
    )

    results = db.execute(statement).all()

    return [
        {"category": category or "Uncategorized", "count": total}
        for category, total in results
    ]


def calculate_sentiment_distribution(db):

    statement = select(
        Feedback.sentiment, func.count(Feedback.id).label("total")
    ).group_by(Feedback.sentiment)

    results = db.execute(statement).all()

    return [
        {"sentiment": sentiment or "Unclassified", "count": total}
        for sentiment, total in results
    ]


def calculate_rating_distribution(db):

    statement = (
        select(Feedback.rating, func.count(Feedback.id).label("total"))
        .where(Feedback.rating.is_not(None))
        .group_by(Feedback.rating)
        .order_by(Feedback.rating)
    )

    results = db.execute(statement).all()

    return [{"rating": rating, "count": total} for rating, total in results]


def calculate_trends(db: Session):
    date_column = func.date_trunc(literal_column("'day'"), Feedback.created_at)

    statement = (
        select(date_column.label("date"), func.count(Feedback.id).label("total"))
        .group_by(date_column)
        .order_by(date_column)
    )

    results = db.execute(statement).all()

    return [{"date": result.date, "total": result.total} for result in results]


def calculate_feedback_summary(db):

    statement = select(
        func.count(Feedback.id).label("total_feedback"),
        func.avg(Feedback.rating).label("average_rating"),
    )

    result = db.execute(statement).one()

    return {
        "total_feedback": result.total_feedback,
        "average_rating": (
            round(float(result.average_rating), 2)
            if result.average_rating is not None
            else None
        ),
    }
