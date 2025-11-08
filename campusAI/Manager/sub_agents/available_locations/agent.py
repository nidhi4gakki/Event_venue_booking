from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool


CAMPUS_SCHEDULE = {
    "Auditorium": [{"date": "22-11-2025", "time_start": "10:00", "time_end": "14:00", "club": "DECA"}],
    "ESB seminar hall 1": [{"date": "20-11-2025", "time_start": "14:00", "time_end": "15:30", "club": "CodeRIT"}],
    "ESB seminar hall 2": [{"date": "21-11-2025", "time_start": "13:00", "time_end": "16:30", "club": "IEEE"}],
    "DES hitech seminar hall": [{"date": "20-11-2025", "time_start": "11:00", "time_end": "14:00", "club": "DEBSOC"}],
    "LHC seminar hall": [{"date": "21-11-2025", "time_start": "11:00", "time_end": "13:00", "club": "MUNSOC"}]

}

def find_available_locations(date: str, time_start: str, time_end: str) -> dict:
    """
    Checks all campus locations and returns a list of those that are completely free 
    during the requested time slot.

    Args:
        date: The date for the availability check (DD-MM-YYYY, example: '21-11-2025').
        time_start: Start time (HH:MM format, e.g., '10:00').
        time_end: End time (HH:MM format).

    Returns:
        dict: A dictionary containing a list of available locations and a summary status.
    """
    FMT = '%H:%M'
    req_start = datetime.strptime(time_start, FMT).time()
    req_end = datetime.strptime(time_end, FMT).time()
    
    available_locations = []
    
    # Assuming CAMPUS_SCHEDULE is accessible (imported or defined)
    for location, bookings in CAMPUS_SCHEDULE.items():
        is_free = True
        
        for booking in bookings:
            if booking['date'] == date:
                existing_start = datetime.strptime(booking['time_start'], FMT).time()
                existing_end = datetime.strptime(booking['time_end'], FMT).time()
                
                # Check for conflict (Time overlap logic)
                is_conflict = (req_start < existing_end) and (req_end > existing_start)
                
                if is_conflict:
                    is_free = False
                    break  # This location is booked, move to the next one
        
        if is_free:
            available_locations.append(location)

    if available_locations:
        return {"status": "success", "available_locations": available_locations, "message": "The following locations are free for your entire slot."}
    else:
        return {"status": "none_available", "available_locations": [], "message": "No locations are available during that time."}
    
available_locations = Agent(
    name="available_locations",
    model="gemini-2.0-flash",
    description="Specializes in checking the entire campus schedule to find a list of all locations that are currently available for a given date and time.",
    instruction="""You are a Campus Location Search Assistant. 
                   When the user asks 'what is available' or 'list all free rooms' or something similar, 
                   you MUST use the find_available_locations tool to retrieve a comprehensive list. 
                   Use the tool even to suggest the user locations if their prefered one is not available.
                   Present the final list clearly to the user with the available time slots.
                   """,
    tools=[FunctionTool(find_available_locations)]
)

