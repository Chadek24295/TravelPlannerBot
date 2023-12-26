def get_travel_inputs():
    # Get departure location from the user
    departure = input("Enter your departure location: ")

    # Get destination location from the user
    destination = input("Enter your destination location: ")

    # Get travel date from the user
    travel_date = input("Enter your travel date (YYYY-MM-DD): ")

    return departure, destination, travel_date

# Example usage
departure, destination, travel_date = get_travel_inputs()
print(f"Departure: {departure}, Destination: {destination}, Travel Date: {travel_date}")
