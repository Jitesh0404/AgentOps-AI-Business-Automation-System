from sqlalchemy.orm import Session

from backend.schemas.feedback import FeedbackCreate
from backend.models.feedback import Feedback
from backend.utils.csv_reader import read_feedback_csv


def import_feedback_csv(db: Session, file_content: bytes):
    valid_records, errors = read_feedback_csv(file_content)

    feedback_objects = [
        Feedback(**record.model_dump()) for record in valid_records
    ]

    try:
        db.add_all(feedback_objects)
        db.commit()

    except Exception:
        db.rollback()
        raise

    return {
        "total_rows": len(valid_records) + len(errors),
        "imported": len(feedback_objects),
        "failed": len(errors),
        "errors": errors,
    }
