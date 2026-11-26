import csv
import io

from pydantic import ValidationError

from backend.schemas.feedback import FeedbackCreate


def read_feedback_csv(file_content: bytes):

    valid_records = []
    errors = []

    csv_file = io.StringIO(file_content.decode("utf-8-sig"))

    reader = csv.DictReader(csv_file)
    print("reader --- ", reader)
    required_columns = {"feedback_text", "created_at"}

    if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
        raise ValueError("Missing required CSV columns")

    for row_number, row in enumerate(reader, start=2):
        try:
            # Convert empty optional values to None
            row = {key: value if value != "" else None for key, value in row.items()}

            # Validate CSV row
            feedback = FeedbackCreate.model_validate(row)

            valid_records.append(feedback)

        except (ValidationError, ValueError) as error:
            errors.append({"row": row_number, "error": str(error)})

    return valid_records, errors
