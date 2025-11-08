from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from datetime import datetime, timedelta

CAMPUS_SCHEDULE = {
    "Auditorium": [{"date": "22-11-2025", "time_start": "10:00", "time_end": "14:00", "club": "DECA"}],
    "ESB seminar hall 1": [{"date": "20-11-2025", "time_start": "14:00", "time_end": "15:30", "club": "CodeRIT"}],
    "ESB seminar hall 2": [{"date": "21-11-2025", "time_start": "13:00", "time_end": "16:30", "club": "IEEE"}],
    "DES hitech seminar hall": [{"date": "20-11-2025", "time_start": "11:00", "time_end": "14:00", "club": "DEBSOC"}],
    "LHC seminar hall": [{"date": "21-11-2025", "time_start": "11:00", "time_end": "13:00", "club": "MUNSOC"}]

}


def finalize_booking(location_name: str, date: str, time_start: str, time_end: str, club_name: str) -> dict:
    """
    Finalizes the booking and updates the central schedule. 
    (Assumes availability check has already passed.)

    Args:
        location_name: Name of the campus space.
        date: The date for the booking (DD-MM-YYYY).
        time_start: Start time (HH:MM format).
        time_end: End time (HH:MM format).
        club_name: The name of the requesting club.

    Returns:
        dict: Confirmation or error.
    """
   
    new_booking = {"date": date, "time_start": time_start, "time_end": time_end, "club": club_name}
    if location_name in CAMPUS_SCHEDULE:
        CAMPUS_SCHEDULE[location_name].append(new_booking)
        return {"status": "success", "confirmation_id": "BK-" + str(len(CAMPUS_SCHEDULE[location_name])), 
                "message": f"Booking confirmed for {club_name} at {location_name} on {date}."}
    else:
        return {"status": "error", "message": "Booking failed. Location not found."}


reservation_manager = Agent(
    name="reservation_manager",
    model="gemini-2.0-flash",
    description="Handles making or canceling room reservations. Use this agent only when the user explicitly requests a booking or cancellation.",
    instruction="You finalize bookings. You MUST use the finalize_booking tool for any confirmed reservation request.",
    tools=[FunctionTool(finalize_booking)]
)