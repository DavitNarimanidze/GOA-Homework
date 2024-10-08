def number(bus_stops):
    total_people = 0
    for stop in bus_stops:
        people_get_on, people_get_off = stop
        total_people += people_get_on - people_get_off
    return total_people if total_people >= 0 else 0