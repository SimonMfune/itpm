"""Single-request tests. They pass for BOTH versions, which is the point:
tests like these did not find the double booking."""
from datetime import datetime

import pytest

import booking_original
import booking_fixed

NOW = datetime(2027, 3, 1, 8, 0)
SLOT = "2027-03-01T09:00"


@pytest.fixture(params=[booking_original, booking_fixed], ids=["original", "fixed"])
def svc(request, tmp_path):
    module = request.param
    db = str(tmp_path / "bookings.db")
    module.init_db(db)
    return module, db


def test_books_a_free_slot(svc):
    module, db = svc
    assert module.book_slot(db, "DR-01", SLOT, "PT-001", now=NOW) is True
    assert module.bookings_for(db, "DR-01", SLOT) == 1


def test_rejects_a_slot_already_booked(svc):
    module, db = svc
    module.book_slot(db, "DR-01", SLOT, "PT-001", now=NOW)
    assert module.book_slot(db, "DR-01", SLOT, "PT-002", now=NOW) is False
    assert module.bookings_for(db, "DR-01", SLOT) == 1


def test_rejects_a_slot_in_the_past(svc):
    module, db = svc
    with pytest.raises(ValueError):
        module.book_slot(db, "DR-01", "2027-03-01T07:00", "PT-001", now=NOW)


def test_same_slot_with_another_clinician_is_allowed(svc):
    module, db = svc
    assert module.book_slot(db, "DR-01", SLOT, "PT-001", now=NOW) is True
    assert module.book_slot(db, "DR-02", SLOT, "PT-002", now=NOW) is True
