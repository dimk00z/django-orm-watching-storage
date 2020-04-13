def get_duration(duration):
    td_in_seconds = duration.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    is_strange = True if hours > 1 else False
    return "{}:{:02d}:{:02d}".format(hours, int(minutes), int(seconds)), is_strange
