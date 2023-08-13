def trip_calculator():
    # Show welcome:
    print(
        "Welcome in Trip Calculator.\n"
        "I'll ask you a few questions and then, I'll show you my results.\n"
        "I promise, it won't be long!\n"
        "****************************************************************"
    )
    # Destination:
    while True:
        destination = input(
            "1/7: Where would you like to go? "
        )
        destination = destination.capitalize()
        if destination != "":
            break
    # Distance:
    while True:
        try:
            distance = float(input(
                "2/7: How far it is? "
            ))
        except ValueError:
            print(
                "Please enter the number!"
            )
        else:
            break
    # Unit distance:
    unit_distance = input(
        "3/7: Is it in: [k] for kilometres or [m] for miles? "
    )
    while unit_distance not in ("k", "m"):
        print(
            "Please enter [k] or [m]!"
        )
        unit_distance = input(
            "3/7: Is it in: [k] for kilometres or [m] for miles? "
        )
    # Fuel price:
    while True:
        try:
            fuel_price = float(input(
                "4/7: What's the cost of petrol/diesel (per litre)? "
            ))
        except ValueError:
            print(
                "Please enter the number!"
            )
        else:
            break
    # Unit price:
    unit_fuel_price = input(
        "5/7: Is it in: [p] for pounds or [z] for zloty? "
    )
    # Unit fuel price:
    while unit_fuel_price not in ("p", "z"):
        print(
            "Please enter [p] or [z]!"
        )
        unit_fuel_price = input(
            "5/7: Is it in: [p] for pounds or [z] for zloty? "
        )
    # Fuel consumption:
    while True:
        try:
            fuel_consumption = float(input(
                "6/7: What's the fuel consumption of your car? "
            ))
        except ValueError:
            print(
                "Please enter the number!"
            )
        else:
            break
    # Unit fuel consumption:
    unit_fuel_consumption = input(
        "7/7: Is it in: [km] for l/100km or [mpg] for UK MPG? "
    )
    while unit_fuel_consumption not in ("km", "mpg"):
        print(
            "7/7: Please enter [km] or [z]!"
        )
        unit_fuel_consumption = input("7/7: Is it in: [km] for km/100 or [mpg] for UK MPG?")
    print(
        "****************************************************************"
    )
    # Creating variables for km and miles:
    if unit_distance == "m":
        m_distance = distance
        k_distance = distance * 1.609344
    else:
        k_distance = distance
        m_distance = distance * 0.6214

    # Creating variables for l/100km and UK MPG:
    if unit_fuel_consumption == "km":
        km_fuel_consumption = fuel_consumption
        mpg_fuel_consumption = 282.481 / fuel_consumption
    else:
        mpg_fuel_consumption = fuel_consumption
        km_fuel_consumption = 282.481 / fuel_consumption

    # Creating variables for total cost in desired currency:
    total_cost = (k_distance / 100) * fuel_consumption * fuel_price

    # # TESTING:
    # print(f"k_distance: {k_distance}")
    # print(f"m_distance: {m_distance}")
    # print(f"destination: {destination}")
    # print(f"distance: {distance}")
    # print(f"unit_distance: {unit_distance}")
    # print(f"fuel_price: {fuel_price}")
    # print(f"unit_fuel_price: {unit_fuel_price}")
    # print(f"fuel_consumption: {fuel_consumption}")
    # print(f"unit_fuel_consumption: {unit_fuel_consumption}")
    # print(f"km_fuel_consumption: {km_fuel_consumption}")
    # print(f"mpg_fuel_consumption: {mpg_fuel_consumption}")
    # print(f"total_cost: {total_cost}")

    # Displaying the results:
    print("****************************************************************")
    print("Summary of Your Trip:\n")
    print(f"Destination:        {destination}")
    print(f"Distance:           {k_distance:.2f} kilometres\n"
          f"                    {m_distance:.2f} miles")
    print(f"Fuel Consumption:   {km_fuel_consumption:.2f} l/100km\n"
          f"                    {mpg_fuel_consumption:.2f} UK MPG")
    if unit_fuel_price == "p":
        print(f"Total Cost:         £{total_cost:.2f}\n"
              f"Return:             £{total_cost * 2:.2f}")
    else:
        print(f"Total Cost:         {total_cost:.2f}zl\n"
              f"Return:             {total_cost * 2:.2f}zl")
    print("\n****************************************************************")

trip_calculator()

