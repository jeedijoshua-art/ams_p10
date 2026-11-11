
VALID_STATUSES = {
    "present": "Present",
    "absent": "Absent",
    "late": "Late",
    "excused": "Excused",
}


def attendance_status(raw_status):
    """
    Validate and normalize an attendance status.

    Args:
        raw_status: Attendance status as a string.

    Returns:
        Normalized attendance status.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is empty or unsupported.
    """
    if not isinstance(raw_status, str):
        raise TypeError("Attendance status must be a string")

    status = raw_status.strip().lower()

    if not status:
        raise ValueError("Attendance status cannot be empty")

    if status not in VALID_STATUSES:
        raise ValueError(f"Invalid attendance status: {raw_status}")

    return VALID_STATUSES[status]
