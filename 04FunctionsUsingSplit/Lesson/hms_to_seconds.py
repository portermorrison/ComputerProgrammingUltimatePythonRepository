def hms_to_seconds(timestring):
    hours, minutes, seconds = timestring.split(":")

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    total_seconds = seconds + minutes * 60 + hours * 60 * 60
    return total_seconds


print("00:00:12 => ", hms_to_seconds("00:00:12"))
print("00:02:00 => ", hms_to_seconds("00:02:00"))
print("02:30:00 => ", hms_to_seconds("02:30:0"))

