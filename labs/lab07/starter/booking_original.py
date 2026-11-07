"""HealthSync booking service: the ORIGINAL version that went to the pilot.

It checks that a slot is free and then saves the booking. It passed code
review and every single-request test. It is fictional teaching code.
"""
import sqlite3
import time
from datetime import datetime

# Simulates the network and service time between the check and the save
# in the real system. Do not remove it: it makes the race easy to see.
CHECK_TO_SAVE_DELAY = 0.05


def init_db(path: str) -> None:
    """Create the bookings table (no constraint on clinician and slot)."""
    with sqlite3.connect(path) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS bookings ("
            " id INTEGER PRIMARY KEY,"
            " clinician_id TEXT NOT NULL,"
            " slot TEXT NOT NULL,"
            " patient_id TEXT NOT NULL)"
        )


def book_slot(path: str, clinician_id: str, slot: str, patient_id: str,
              now: datetime | None = None) -> bool:
    """Book a slot. Return True if booked, False if the slot is taken."""
    now = now or datetime.now()
    if datetime.fromisoformat(slot) <= now:
        raise ValueError("Cannot book a slot in the past")
    conn = sqlite3.connect(path, timeout=5)
    try:
        taken = conn.execute(
            "SELECT 1 FROM bookings WHERE clinician_id = ? AND slot = ?",
            (clinician_id, slot),
        ).fetchone()
        if taken:
            return False
        time.sleep(CHECK_TO_SAVE_DELAY)
        conn.execute(
            "INSERT INTO bookings (clinician_id, slot, patient_id) VALUES (?, ?, ?)",
            (clinician_id, slot, patient_id),
        )
        conn.commit()
        return True
    finally:
        conn.close()


def bookings_for(path: str, clinician_id: str, slot: str) -> int:
    """Count bookings for one clinician and slot."""
    with sqlite3.connect(path) as conn:
        return conn.execute(
            "SELECT COUNT(*) FROM bookings WHERE clinician_id = ? AND slot = ?",
            (clinician_id, slot),
        ).fetchone()[0]
