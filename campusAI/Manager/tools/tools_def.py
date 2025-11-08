from datetime import datetime


def current_time() -> dict:
    """
    Get the current time in the format DD-MM-YYYY HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }