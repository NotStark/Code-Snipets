

def readable_time(seconds : int) -> str:
    time = seconds
    time_string = ""
    if time < 60:
        time_string = f"{time}s"
    else:
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        if days > 0:
            time_string += f"{days}days, "
        if hours > 0:
            time_string += f"{hours}h:"
        time_string += f"{minutes}m:{seconds}s"

    return time_string
