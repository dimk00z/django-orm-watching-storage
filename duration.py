def get_duration(duration):
    td_in_seconds = duration.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    is_strange = False
    if hours > 1:
        is_strange = True
    minutes = int(minutes)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "{:02d}".format(minutes)
    if seconds < 10:
        seconds = "{:02d}".format(seconds)
    return "{}:{}:{}".format(hours, minutes, seconds), is_strange
