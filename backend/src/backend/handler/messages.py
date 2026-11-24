# ==========================================
# SUCCESS MESSAGES (2xx)
# ==========================================

SUCCESS = "Operation completed successfully."
OK = "Request completed successfully."
CREATED = "Resource created successfully."
UPDATED = "Resource updated successfully."
DELETED = "Resource deleted successfully."
FETCHED = "Data fetched successfully."
SAVED = "Data saved successfully."
SUBMITTED = "Data submitted successfully."
ACCEPTED = "Request accepted successfully."


# ==========================================
# REDIRECTION MESSAGES (3xx)
# ==========================================

REDIRECT = "Resource has been redirected."
MOVED_PERMANENTLY = "Resource has been moved permanently."
NOT_MODIFIED = "Resource has not been modified."


# ==========================================
# CLIENT ERROR MESSAGES (4xx)
# ==========================================

BAD_REQUEST = "Invalid request. Please check your input."
UNAUTHORIZED = "Authentication is required."
FORBIDDEN = "You do not have permission to perform this action."
NOT_FOUND = "Requested resource was not found."
METHOD_NOT_ALLOWED = "HTTP method is not allowed."
NOT_ACCEPTABLE = "Requested format is not supported."
REQUEST_TIMEOUT = "Request timed out."
CONFLICT = "A conflict occurred with the existing resource."
GONE = "Requested resource is no longer available."
PAYLOAD_TOO_LARGE = "Request payload is too large."
UNSUPPORTED_MEDIA_TYPE = "Unsupported media type."
UNPROCESSABLE_ENTITY = "Unable to process the provided data."
TOO_MANY_REQUESTS = "Too many requests. Please try again later."
VALIDATION_ERROR = "Validation failed. Please check your input."


# ==========================================
# AUTHENTICATION MESSAGES
# ==========================================

LOGIN_SUCCESS = "Login successful."
LOGIN_FAILED = "Invalid email or password."
LOGOUT_SUCCESS = "Logout successful."
REGISTER_SUCCESS = "Registration completed successfully."
ACCOUNT_NOT_FOUND = "Account not found."
ACCOUNT_ALREADY_EXISTS = "An account with these details already exists."
INVALID_CREDENTIALS = "Invalid credentials."
INVALID_TOKEN = "Invalid or expired token."
TOKEN_EXPIRED = "Your session has expired. Please log in again."
TOKEN_GENERATED = "Authentication token generated successfully."
ACCESS_DENIED = "Access denied."
OTP_SENT = "OTP sent successfully."
OTP_VERIFIED = "OTP verified successfully."
INVALID_OTP = "Invalid OTP."
OTP_EXPIRED = "OTP has expired."
OTP_LIMIT_EXCEEDED = "OTP request limit exceeded."


# ==========================================
# USER MESSAGES
# ==========================================

USER_CREATED = "User created successfully."
USER_UPDATED = "User updated successfully."
USER_DELETED = "User deleted successfully."
USER_FETCHED = "User details fetched successfully."
USER_NOT_FOUND = "User not found."
USER_ALREADY_EXISTS = "User already exists."
USER_PROFILE_UPDATED = "User profile updated successfully."


# ==========================================
# SERVER ERROR MESSAGES (5xx)
# ==========================================

INTERNAL_SERVER_ERROR = "Internal server error. Please try again later."
NOT_IMPLEMENTED = "This functionality has not been implemented yet."
BAD_GATEWAY = "Invalid response received from the upstream server."
SERVICE_UNAVAILABLE = "Service is temporarily unavailable."
GATEWAY_TIMEOUT = "The server took too long to respond."


# ==========================================
# DATABASE MESSAGES
# ==========================================

DATABASE_ERROR = "A database error occurred."
DATABASE_CONNECTION_ERROR = "Unable to connect to the database."
RECORD_NOT_FOUND = "Requested record was not found."
RECORD_ALREADY_EXISTS = "Record already exists."
RECORD_CREATED = "Record created successfully."
RECORD_UPDATED = "Record updated successfully."
RECORD_DELETED = "Record deleted successfully."


# ==========================================
# FILE MESSAGES
# ==========================================

FILE_UPLOADED = "File uploaded successfully."
FILE_UPLOAD_FAILED = "File upload failed."
FILE_NOT_FOUND = "File not found."
FILE_DELETED = "File deleted successfully."
INVALID_FILE_FORMAT = "Invalid file format."
FILE_TOO_LARGE = "File size exceeds the allowed limit."


# ==========================================
# GENERAL MESSAGES
# ==========================================

SOMETHING_WENT_WRONG = "Something went wrong."
INVALID_INPUT = "Invalid input provided."
MISSING_REQUIRED_FIELDS = "Required fields are missing."
OPERATION_FAILED = "Operation failed."
REQUEST_RECEIVED = "Request received successfully."
