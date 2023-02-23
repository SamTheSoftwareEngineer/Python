def weekday_name(day_of_week):
    # Need to create an array that contains all the days of the week 
        Days = [
            "Sunday"
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday", 
            "Saturday",
        ]
    # If the day of the week isn't between 1 and 7, return none
        if day_of_week < 1 or day_of_week > 7:
            return None
    # Otherwise, return the day of the week as indicated in the array 
        return Days[day_of_week - 1]

print(weekday_name(2))            