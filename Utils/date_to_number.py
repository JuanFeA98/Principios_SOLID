"Function to convert datatime into number"
from datetime import datetime

def run(date: datetime):
    """Change the format of datetime

    Args:
        date (datetime): date to format

    Returns:
        int: date in numeric format
    """
    return int(str(date).replace('-', '')[:8])
