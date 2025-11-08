from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from datetime import datetime, timedelta


CAMPUS_SCHEDULE = {
    "auditorium": [{"date": "22-11-2025", "time_start": "10:00", "time_end": "14:00", "club": "DECA"}],
    "esb seminar hall 1": [{"date": "20-11-2025", "time_start": "14:00", "time_end": "15:30", "club": "CodeRIT"}],
    "esb seminar hall 2": [{"date": "21-11-2025", "time_start": "13:00", "time_end": "16:30", "club": "IEEE"}],
    "des hitech seminar hall": [{"date": "20-11-2025", "time_start": "11:00", "time_end": "14:00", "club": "DEBSOC"}],
    "lhc seminar hall": [{"date": "21-11-2025", "time_start": "11:00", "time_end": "13:00", "club": "MUNSOC"}]
}


CLUB_STATUS_DB = {"Chess Club": "Active", "Film Club": "Active", "Unregistered Club": "Inactive"}


def check_availability(location_name: str, date: str, time_start: str, time_end: str) -> dict:
    """
    Checks if a specific location is free during the requested time slot. 
    It handles case-insensitivity and performs precise time overlap checking.

    Args:
        location_name: Name of the campus space (e.g., 'LHC seminar hall').
        date: The date for the booking (DD-MM-YYYY).
        time_start: Start time (HH:MM format, e.g., '17:00').
        time_end: End time (HH:MM format).

    Returns:
        dict: Status and a descriptive message (includes club name on conflict).
    """
    
    normalized_input = location_name.strip().lower()
    
    if normalized_input not in CAMPUS_SCHEDULE:
        return {"status": "error", "message": f"Location '{location_name}' is not recognized."}
        
    location_key = normalized_input 

   
    FMT = '%H:%M'
    try:
        req_start = datetime.strptime(time_start, FMT).time()
        req_end = datetime.strptime(time_end, FMT).time()
    except ValueError:
        return {"status": "error", "message": "Time format error. Please use HH:MM format (e.g., 14:00)."}

    
    for booking in CAMPUS_SCHEDULE.get(location_key, []):
        
        
        if booking['date'] == date:
            
            existing_start = datetime.strptime(booking['time_start'], FMT).time()
            existing_end = datetime.strptime(booking['time_end'], FMT).time()

            
            is_conflict = (req_start < existing_end) and (req_end > existing_start)
            
            if is_conflict:
                return {"status": "conflict", 
                        "message": f"Conflict found. The space is already booked on {date} by the {booking['club']} from {booking['time_start']} to {booking['time_end']}."}
    
    
    return {"status": "available", "message": f"{location_key.title()} is available on {date} from {time_start} to {time_end}."}

availability_checker = Agent(
    name="AvailabilityChecker",
    model="gemini-2.5-flash",
    description="Specializes in checking the current schedule for location availability. Use this agent for all 'is it free' questions.",
    instruction="""You are an expert on campus location schedules. You MUST use the check_availability tool to verify any time slot requested by the user. 
                   When a conflict is found, you MUST mention the club name and the conflicting time slot.""",
    tools=[FunctionTool(check_availability)]
)