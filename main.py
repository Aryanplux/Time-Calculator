def add_time(start, duration, starting_day=None):
    # Parse start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if meridian == 'PM':
        start_hour += 12

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate total minutes and hours
    total_minutes = start_minute + duration_minute
    additional_hours = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + additional_hours
    final_hour = total_hours % 24
    days_later = total_hours // 24

    # Determine AM/PM and convert to 12-hour format
    final_meridian = 'AM' if final_hour < 12 else 'PM'
    if final_hour == 0:
        final_hour = 12
    elif final_hour > 12:
        final_hour -= 12

    # Determine the day of the week if provided
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if starting_day:
        starting_day_index = week_days.index(starting_day.capitalize())
        final_day_index = (starting_day_index + days_later) % 7
        final_day = week_days[final_day_index]
    else:
        final_day = None

    # Format the final time
    new_time = f"{final_hour}:{final_minute:02d} {final_meridian}"
    if final_day:
        new_time += f", {final_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Examples
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
