def calculate_flight_time(weight_grams):

    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")

        
    flight_time = 180 - 0.1 * weight_grams
    return max(0.0, flight_time)


def flight_time_table(max_weight_grams, step_grams):

    table = []
    current_weight = 0
    
    while current_weight <= max_weight_grams:
        flight_time = calculate_flight_time(current_weight)
        table.append((current_weight, flight_time))
        current_weight += step_grams
        
    return table