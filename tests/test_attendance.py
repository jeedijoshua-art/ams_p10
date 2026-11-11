
import pytest

from attendance import attendance_status


@pytest.mark.parametrize(
    "raw_status, expected",
    [
        ("present", "Present"),
        ("absent", "Absent"),
        ("late", "Late"),
        ("excused", "Excused"),
        ("PRESENT", "Present"),
        ("Absent", "Absent"),
        ("LaTe", "Late"),
        (" present ", "Present"),
        (" absent ", "Absent"),
        ("late ", "Late"),
        ("excused\n", "Excused"),
    ],
)
def test_valid_attendance_status(raw_status, expected):
    assert attendance_status(raw_status) == expected


@pytest.mark.parametrize(
    "raw_status",
    [
        "",
        " ",
        "holiday",
        "unknown",
        "P",
        "presented",
    ],
)
def test_invalid_attendance_status(raw_status):
    with pytest.raises(ValueError):
        attendance_status(raw_status)


@pytest.mark.parametrize(
    "raw_status",
    [
        None,
        123,
    ],
)
def test_non_string_attendance_status(raw_status):
    with pytest.raises(TypeError):
        attendance_status(raw_status)
