# Create A Railway Booking System:::::


def default():
    print(f"                             WELCOME TO INDIAN RAILWAY")
    print()
    print(f"                          Have you not found the right one?")
    print(f"                        Find a service suitable for you here.")
    print()


# calling all statements (main functions):
def inputt():
    default()
    print("Book Your Tricket")
    print()
    fr = input("Journey From: ")
    to = input("Journey To: ")
    if fr in ('NJP', 'njp', 'Njp', 'New Jalpaiguri', 'new jalpaiguri', 'newjalpaiguri') and to in (
            'Sealdha', 'SDHA', 'sealdha', 'sealsha', 'sdha'):
        booking_njp_to_sealdha()
    elif fr in ('Sealdha', 'SDHA', 'sealdha', 'sealsha', 'sdha') and to in (
            'NJP', 'njp', 'Njp', 'New Jalpaiguri', 'new jalpaiguri', 'newjalpaiguri'):
        booking_sealdha_to_njp()
    elif fr in ('NJP', 'njp', 'Njp', 'New Jalpaiguri', 'new jalpaiguri', 'newjalpaiguri') and to in (
            'Malda', 'malda', 'mal''mald', 'MALDA', 'MAL'):
        booking_njp_malda()
    else:
        "break"


def booking_njp_to_sealdha():
    date = input("Date: ")
    n = int(input("How many passenger are going: "))
    sh = input("Are you Senior Citizen(yes/no): ")
    av = input("Are you want to show availabe trains(yes/no): ")
    cla = input("Class(AC 3A/AC 2A/AC 1A/Sleeper): ")
    if sh in ('YES', 'Y', 'yes', 'Yes'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                njp_to_sealdha_SL_senior_citizen_male_female()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                njp_to_sealdha_1A_senior_citizen_male_female()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                njp_to_sealdha_2A_senior_citizen_male_female()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                njp_to_sealdha_3A_senior_citizen_male_female()
            else:
                "break"
        elif av in ('No', 'no', 'NO', 'n'):
            "break"
        else:
            "break"
    elif sh in ('No', 'no', 'NO', 'n'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                njp_to_sealdha_SL()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                njp_to_sealdha_1A()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                njp_to_sealdha_2A()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                njp_to_sealdha_3A()
    print()
    tra = input("Which train you want to travel: ")
    tra_no = int(input("Enter Train Number: "))
    #   1. Train Number: 13176
    #   Train Name: KUNCHAN JUNGHA EXPRESS

    if tra_no == 13176:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13176()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13176()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13176()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13176()
        else:
            "break"
    #   2.Train Number: 13142:
    #   Train Name: TEESTA TORSHA EXPRESS:

    elif tra_no == 13142:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13142()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13142()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13142()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13142()
        else:
            "break"
    #   3.Train Number: 13148
    #   Train Name: UTTAR BANG EXPRESS
    elif tra_no == 13148:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13148()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13148()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13148()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13148()
        else:
            "break"
    #   4.Train Number: 12344
    #   Train Name: DARJEELING MAIL
    elif tra_no == 12344:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_12344()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_12344()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_12344()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_12344()
        else:
            "break"
    #   5.Train Number: 13150
    #   Train NAme: KANCHAN KANYA EXPRESS
    elif tra_no == 13150:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13150()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13150()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13150()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13150()
        else:
            "break"
    #   6.Train Number: 12378
    #   Train Name: PADATIK EXPRESS
    elif tra_no == 12378:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_12378()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_12378()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_12378()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_12378()
        else:
            "break"
    #   7.Train Number: 15986
    #   Train Name: HWH SHATABDI EXPRESS
    elif tra_no == 15986:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_15986()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_15986()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_15986()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_15986()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_15986()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_15986()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_15986()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15986()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_15986()
        else:
            "break"
    #   8. Train Name: 15722
    #   Train Name: PAHARIA EXPRESS
    elif tra_no == 15722:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_15722()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_15722()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_15722()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_15722()
        else:
            "break"
    #   9.Train Number: 19654
    #   Train Name: KAMRUP EXPRESS
    elif tra_no == 19654:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_19654()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_19654()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_19654()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_19654()
        else:
            "break"
    #   10.Train Number: 15565
    #   Train Name: SCL TVC EXPRESS
    elif tra_no == 15565:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_15565()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_15565()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_15565()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_15565()
        else:
            "break"
    else:
        "break"


# Trains are from Sealdha to NJP:
def booking_sealdha_to_njp():
    date = input("Date: ")
    n = int(input("How many passenger are going: "))
    sh = input("Are you Senior Citizen(yes/no): ")
    av = input("Are you want to show availabe trains(yes/no): ")
    cla = input("Class(AC 3A/AC 2A/AC 1A/Sleeper): ")
    if sh in ('YES', 'Y', 'yes', 'Yes'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                sealdha_to_njp_SL_senior_citizen_male_female()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                sealdha_to_njp_1A_senior_citizen_male_female()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                sealdha_to_njp_2A_senior_citizen_male_female()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                sealdha_to_njp_3A_senior_citizen_male_female()
            else:
                "break"
        elif av in ('No', 'no', 'NO', 'n'):
            "break"
        else:
            "break"
    elif sh in ('No', 'no', 'NO', 'n'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                sealdha_to_njp_SL()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                sealdha_to_njp_1A()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                sealdha_to_njp_2A()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                sealdha_to_njp_3A()
    print()
    tra = input("Which train you want to travel: ")
    tra_no = int(input("Enter Train Number: "))
    #   1. Train Number: 13176
    #   Train Name: KUNCHAN JUNGHA EXPRESS

    if tra_no == 13176:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13176()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13176()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13176()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13176_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13176()
        else:
            "break"
    #   2.Train Number: 13142:
    #   Train Name: TEESTA TORSHA EXPRESS:

    elif tra_no == 13142:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13142()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13142()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13142()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13142_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13142()
        else:
            "break"
    #   3.Train Number: 13148
    #   Train Name: UTTAR BANG EXPRESS
    elif tra_no == 13148:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13148()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13148()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13148()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13148_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13148()
        else:
            "break"
    #   4.Train Number: 12344
    #   Train Name: DARJEELING MAIL
    elif tra_no == 12344:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_12344()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_12344()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_12344()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12344_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_12344()
        else:
            "break"
    #   5.Train Number: 13150
    #   Train NAme: KANCHAN KANYA EXPRESS
    elif tra_no == 13150:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_13150()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_13150()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_13150()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_13150_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_13150()
        else:
            "break"
    #   6.Train Number: 12378
    #   Train Name: PADATIK EXPRESS
    elif tra_no == 12378:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_12378()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_12378()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_12378()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_12378_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_12378()
        else:
            "break"
    #   7. Train Number: 15986.
    #   Train Name: HWH SHATABDI EXPRESS

    # HWH SHATABDI EXPRESS are not travel from sealdh to njp.

    #   8. Train Name: 15722
    #   Train Name: PAHARIA EXPRESS
    elif tra_no == 15722:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_15722()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_15722()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_15722()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15722_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_15722()
        else:
            "break"
    #   9.Train Number: 19654
    #   Train Name: KAMRUP EXPRESS
    elif tra_no == 19654:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_19654()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_19654()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_19654()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_19654_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_19654()
        else:
            "break"
    #   10.Train Number: 15565
    #   Train Name: SCL TVC EXPRESS
    elif tra_no == 15565:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_sl_sc_15565()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_1A_sc_15565()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_2A_sc_15565()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_15565_R()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_3A_sc_15565()
        else:
            "break"
    else:
        "break"


def njp_to_sealdha_SL():
    print()
    print("Train Name/Train Number/Available Seats/Fees In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        350/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        340/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          337/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          350/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          350/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         325/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(120/65)         325/-")
    print(f"08          PAHARIA EXP                 15722           Yes(20/51)          345/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          325/-")
    print(f"10          SCL TVC EXP                 15565           Yes(20/61)          345/-")


def fare_sl_13176():
    print(f"Ticket Fare:                           350/-     Rupees Three Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             367.7/-   Rupees Three Hundred Sixty Seven and Seven Paisa")


def fare_sl_13142():
    print(f"Ticket Fare:                           340/-     Rupees Three Hundred Fourty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             357.7/-   Rupees Three Hundred Fifty Seven and Seven Paisa")


def fare_sl_13148():
    print(f"Ticket Fare:                           337/-     Rupees Three Hundred Thirty Seven and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             354.7/-   Rupees Three Hundred Fifty Four and Seven Paisa")


def fare_sl_12344():
    print(f"Ticket Fare:                           350/-     Rupees Three Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             367.7/-   Rupees Three Hundred Sixty Seven and Seven Paisa")


def fare_sl_13150():
    print(f"Ticket Fare:                           350/-     Rupees Three Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             367.7/-   Rupees Three Hundred Sixty Seven and Seven Paisa")


def fare_sl_12378():
    print(f"Ticket Fare:                           325/-     Rupees Three Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             345.7/-   Rupees Three Hundred Fourty Five and Seven Paisa")


def fare_sl_15986():
    print(f"Ticket Fare:                           325/-     Rupees Three Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             345.7/-   Rupees Three Hundred Fourty Five and Seven Paisa")


def fare_sl_15722():
    print(f"Ticket Fare:                           345/-     Rupees Three Hundred Fourty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             362.7/-   Rupees Three Hundred Sixty Two and Seven Paisa")


def fare_sl_19654():
    print(f"Ticket Fare:                           325/-     Rupees Three Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             345.7/-   Rupees Three Hundred Fourty Five and Seven paisa")


def fare_sl_15565():
    print(f"Ticket Fare:                           345/-     Rupees Three Hundred Fourty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             362.7/-   Rupees Three Hundred Sixty Two and Seven Paisa")


def njp_to_sealdha_SL_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        250/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        240/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          237/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          250/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          250/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         225/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(120/65)         225/-")
    print(f"08          PAHARIA EXP                 15722           Yes(20/51)          245/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          225/-")
    print(f"10          SCL TVC EXP                 15565           Yes(20/61)          245/-")


def fare_sl_sc_13176():
    print(f"Ticket Fare:                           250/-     Rupees Two Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             267.7/-   Rupees Two Hundred Sixty Seven and Seven Paisa")


def fare_sl_sc_13142():
    print(f"Ticket Fare:                           240/-     Rupees Two Hundred Fourty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             257.7/-   Rupees Two Hundred Fifty Seven and Seven Paisa")


def fare_sl_sc_13148():
    print(f"Ticket Fare:                           237/-     Rupees Two Hundred Thirty Seven and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             254.7/-   Rupees Two Hundred Fifty Four and Seven Paisa")


def fare_sl_sc_12344():
    print(f"Ticket Fare:                           250/-     Rupees Two Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             267.7/-   Rupees Two Hundred Sixty Seven and Seven Paisa")


def fare_sl_sc_13150():
    print(f"Ticket Fare:                           250/-     Rupees Two Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             267.7/-   Rupees Two Hundred Sixty Seven and Seven Paisa")


def fare_sl_sc_12378():
    print(f"Ticket Fare:                           225/-     Rupees Two Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             245.7/-   Rupees Two Hundred Fourty Five and Seven Paisa")


def fare_sl_sc_15986():
    print(f"Ticket Fare:                           225/-     Rupees Two Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             245.7/-   Rupees Two Hundred Fourty Five and Seven Paisa")


def fare_sl_sc_15722():
    print(f"Ticket Fare:                           245/-     Rupees Two Hundred Fourty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             262.7/-   Rupees Two Hundred Sixty Two and Seven Paisa")


def fare_sl_sc_19654():
    print(f"Ticket Fare:                           225/-     Rupees Two Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             245.7/-   Rupees Two Hundred Fourty Five and Seven paisa")


def fare_sl_sc_15565():
    print(f"Ticket Fare:                           245/-     Rupees Two Hundred Fourty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             262.7/-   Rupees Two Hundred Sixty Two and Seven Paisa")


def njp_to_sealdha_1A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         2750/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         2150/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          2350/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          2500/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        2350/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         2350/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(120/165)        2150/-")
    print(f"08          PAHARIA EXP                 15722           Yes(20/51)          2500/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/65)          2350/-")
    print(f"10          SCL TVC EXP                 15565           Yes(20/67)          2150/-")


def fare_1A_13176():
    print(f"Ticket Fare:                     2750/-    Rupees Two Thousand  Seven Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2767.7/-  Rupees Three Hundred Sixty Seven and Seven Paisa")


def fare_1A_13142():
    print(f"Ticket Fare:                     2150/-    Rupees Two Thousand One Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2167.7/-  Rupees Two Thousand One Hundred SixtySeven and Seven Paisa")


def fare_1A_13148():
    print(f"Ticket Fare:                     2350/-    Rupees Two Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2367.7/-  Rupees Two Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_12344():
    print(f"Ticket Fare:                     2500/-    Rupees Two Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2517.7/-  Rupees Two Thousand Five Hundred Seventen and Seven Paisa")


def fare_1A_13150():
    print(f"Ticket Fare:                     2350/-    Rupees Two Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2367.7/-  Rupees Two Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_12378():
    print(f"Ticket Fare:                     2350/-    Rupees Two Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2367.7/-  Rupees Two Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_15986():
    print(f"Ticket Fare:                     2150/-    Rupees Two Thousand One Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2167.7/-  Rupees Two Thousand One Hundred SixtySeven and Seven Paisa")


def fare_1A_15722():
    print(f"Ticket Fare:                     2500/-    Rupees Two Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2517.7/-  Rupees Two Thousand Five Hundred Seventen and Seven Paisa")


def fare_1A_19654():
    print(f"Ticket Fare:                     2350/-    Rupees Two Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2367.7/-  Rupees Two Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_15565():
    print(f"Ticket Fare:                     2150/-    Rupees Two Thousand One Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       2167.7/-  Rupees Two Thousand One Hundred SixtySeven and Seven Paisa")


def njp_to_sealdha_1A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1375/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         1350/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          1350/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          1300/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        1350/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         1350/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(120/165)        1350/-")
    print(f"08          PAHARIA EXP                 15722           Yes(20/51)          1500/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/65)          1350/-")
    print(f"10          SCL TVC EXP                 15565           Yes(20/67)          1350/-")


def fare_1A_sc_13176():
    print(f"Ticket Fare:                     1375/-    Rupees One Thousand Three Hundred SeventyFive and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1392.7/-  Rupees One Thousand Three Hundred NinetyTwo and Seven Paisa")


def fare_1A_sc_13142():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_13148():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_12344():
    print(f"Ticket Fare:                     1300/-    Rupees One Thousand Three Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1317.7/-  Rupees One Thousand Three Hundred Seventen and Seven Paisa")


def fare_1A_sc_13150():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_12378():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_15986():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_15722():
    print(f"Ticket Fare:                     1500/-    Rupees One Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1517.7/-  Rupees One Thousand Five Hundred Seventen and Seven Paisa")


def fare_1A_sc_19654():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def fare_1A_sc_15565():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def njp_to_sealdha_2A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1650/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        1500/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         1685/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           1685/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          1675/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         1650/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(51/65)          1550/-")
    print(f"08          PAHARIA EXP                 15722           Yes(41/51)          1500/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          1450/-")
    print(f"10          SCL TVC EXP                 15565           Yes(41/61)          1350/-")


def fare_2A_13176():
    print(f"Ticket Fare:                     1650/-    Rupees One Thousand Six Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1667.7/-  Rupees One Thousand Six Hundred SixtySeven and Seven Paisa")


def fare_2A_13142():
    print(f"Ticket Fare:                     1500/-    Rupees One Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1517.7/-  Rupees One Thousand Five Hundred Seventeen and Seven Paisa")


def fare_2A_13148():
    print(f"Ticket Fare:                     1685/-    Rupees One Thousand Six Hundred EightyFive and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1702.7/-  Rupees One Thousand Seven Hundred Two and Seven Paisa")


def fare_2A_12344():
    print(f"Ticket Fare:                     1685/-    Rupees One Thousand Six Hundred EightyFive and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1702.7/-  Rupees One Thousand Seven Hundred Two and Seven Paisa")


def fare_2A_13150():
    print(f"Ticket Fare:                     1675/-    Rupees One Thousand Six Hundred SeventeenFifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1692.7/-  Rupees One Thousand Six Hundred NineteenTwo and Seven Paisa")


def fare_2A_12378():
    print(f"Ticket Fare:                     1650/-    Rupees One Thousand Six Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1667.7/-  Rupees One Thousand Six Hundred SixtySeven and Seven Paisa")


def fare_2A_15986():
    print(f"Ticket Fare:                     1550/-    Rupees One Thousand Five Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1567.7/-  Rupees One Thousand Five Hundred SixtySeven and Seven Paisa")


def fare_2A_15722():
    print(f"Ticket Fare:                     1500/-    Rupees One Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1517.7/-  Rupees One Thousand Five Hundred Seventen and Seven Paisa")


def fare_2A_19654():
    print(f"Ticket Fare:                     1450/-    Rupees One Thousand Four Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1467.7/-  Rupees One Thousand Four Hundred SixtySeven and Seven Paisa")


def fare_2A_15565():
    print(f"Ticket Fare:                     1350/-    Rupees One Thousand Three Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1367.7/-  Rupees One Thousand Three Hundred SixtySeven and Seven Paisa")


def njp_to_sealdha_2A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         850/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        800/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         885/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           885/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          875/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         850/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(51/65)          850/-")
    print(f"08          PAHARIA EXP                 15722           Yes(41/51)          800/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          850/-")
    print(f"10          SCL TVC EXP                 15565           Yes(41/61)          850/-")


def fare_2A_sc_13176():
    print(f"Ticket Fare:                     850/-     Rupees Eight Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       867.7/-   Rupees Eight Hundred SixtySeven and Seven Paisa")


def fare_2A_sc_13142():
    print(f"Ticket Fare:                     800/-     Rupees One Thousand Five Hundred and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_2A_sc_13148():
    print(f"Ticket Fare:                     885/-     Rupees Eight Hundred EightyFive and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       902.7/-   Rupees Nine Hundred Two and Seven Paisa")


def fare_2A_sc_12344():
    print(f"Ticket Fare:                     885/-     Rupees Eight Hundred EightyFive and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       902.7/-   Rupees Nine Hundred Two and Seven Paisa")


def fare_2A_sc_13150():
    print(f"Ticket Fare:                     875/-     Rupees Eight Hundred SeventeenFifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       892.7/-   Rupees Eight Hundred NineteenTwo and Seven Paisa")


def fare_2A_sc_12378():
    print(f"Ticket Fare:                     850/-     Rupees Eight Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       867.7/-   Rupees Eight Hundred SixtySeven and Seven Paisa")


def fare_2A_sc_15986():
    print(f"Ticket Fare:                     850/-     Rupees Eight Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       867.7/-   Rupees Eight Hundred SixtySeven and Seven Paisa")


def fare_2A_sc_15722():
    print(f"Ticket Fare:                     800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       817.7/-   Rupees Eight Hundred Seventen and Seven Paisa")


def fare_2A_sc_19654():
    print(f"Ticket Fare:                     850/-     Rupees Eight Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       867.7/-   Rupees Eight Hundred SixtySeven and Seven Paisa")


def fare_2A_sc_15565():
    print(f"Ticket Fare:                     850/-     Rupees Eight Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       867.7/-   Rupees Eight Hundred SixtySeven and Seven Paisa")


def njp_to_sealdha_3A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          1050/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        1200/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          1150/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          1100/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          950/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         1000/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(85/125)         1100/-")
    print(f"08          PAHARIA EXP                 15722           Yes(41/51)          900/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          1050/-")
    print(f"10          SCL TVC EXP                 15565           Yes(25/61)          1000/-")


def fare_3A_13176():
    print(f"Ticket Fare:                     1050/-    Rupees One Thousand Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1067.7/-  Rupees One Thousand SixtySeven and Seven Paisa")


def fare_3A_13142():
    print(f"Ticket Fare:                     1200/-    Rupees One Thousand Two Hundred and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1217.7/-  Rupees One Thousand Two Hundred Seventeen and Seven Paisa")


def fare_3A_13148():
    print(f"Ticket Fare:                     1150/-    Rupees One Thousand One Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1167.7/-  Rupees One Thousand One Hundred SixtySeven and Seven Paisa")


def fare_3A_12344():
    print(f"Ticket Fare:                     1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1117.7/-  Rupees One Thousand One Hundred Seventeen and Seven Paisa")


def fare_3A_13150():
    print(f"Ticket Fare:                     950/-     Rupees Nine Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       967.7/-   Rupees Nine Hundred SixtySeven and Seven Paisa")


def fare_3A_12378():
    print(f"Ticket Fare:                     1000/-    Rupees One Thousand and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_3A_15986():
    print(f"Ticket Fare:                     1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1117.7/-  Rupees One Thousand One Hundred Seventeen and Seven Paisa")


def fare_3A_15722():
    print(f"Ticket Fare:                     900/-     Rupees Nine Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       917.7/-   Rupees Nine Hundred Seventen and Seven Paisa")


def fare_3A_19654():
    print(f"Ticket Fare:                     1050/-    Rupees One Thousand Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1067.7/-  Rupees One Thousand SixtySeven and Seven Paisa")


def fare_3A_15565():
    print(f"Ticket Fare:                     1000/-    Rupees One Thousand and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def njp_to_sealdha_3A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          650/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        600/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          650/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          600/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          550/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         500/-")
    print(f"07          HWH SHATABDI EXP            15986           Yes(85/125)         625/-")
    print(f"08          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"09          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"10          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def fare_3A_sc_13176():
    print(f"Ticket Fare:                     650/-     Rupees Six Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       667.7/-   Rupees Six Hundred SixtySeven and Seven Paisa")


def fare_3A_sc_13142():
    print(f"Ticket Fare:                     600/-     Rupees Six Hundred and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       617.7/-   Rupees Six Hundred Seventeen and Seven Paisa")


def fare_3A_sc_13148():
    print(f"Ticket Fare:                     650/-     Rupees Six Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee(Incl. of GST)    17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       667.7/-   Rupees Six Hundred SixtySeven and Seven Paisa")


def fare_3A_sc_12344():
    print(f"Ticket Fare:                     600/-     Rupees Six Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       617.7/-   Rupees Six Hundred Seventeen and Seven Paisa")


def fare_3A_sc_13150():
    print(f"Ticket Fare:                     550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       567.7/-   Rupees Five Hundred SixtySeven and Seven Paisa")


def fare_3A_sc_12378():
    print(f"Ticket Fare:                     500/-     Rupees Five Hundred and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_3A_sc_15986():
    print(f"Ticket Fare:                     625/-     Rupees Six Hundred TwentyFive and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       642.7/-   Rupees Six Hundred FourtyTwo and Seven Paisa")


def fare_3A_sc_15722():
    print(f"Ticket Fare:                     475/-     Rupees Four Hundred SeventyFive and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       492.7/-   Rupees Four Hundred NineteenTwo and Seven Paisa")


def fare_3A_sc_19654():
    print(f"Ticket Fare:                     650/-     Rupees Six Hundred Fifty and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       667.7/-   Rupees Six Hundred SixtySeven and Seven Paisa")


def fare_3A_sc_15565():
    print(f"Ticket Fare:                     570/-     Rupees Five Hundred Seventy and Zero Paisa")
    print(f"Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)       587.7/-   Rupees Five Hundred EightySeven and Seven Paisa")


# Train which are travel from NJP to Sealdha.
def train_13176():
    print(f"Train Name: KUNCHAN JUNGHA EXPRESS               Train No: 13176")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 575 Km.")


def train_13142():
    print(f"Train Name: TEESTA TORSHA EXPRESS                Train No: 13142")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 580 Km.")


def train_13148():
    print(f"Train Name: UTTAR BANGA EXPRESS                  Train No: 13148")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 580 Km.")


def train_12344():
    print(f"Train Name: DARJEELING MAIL                      Train No: 13142")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 572 Km.")


def train_13150():
    print(f"Train Name: KANCHAN KANYA EXPRESS                Train No: 13150")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 576 Km.")


def train_12378():
    print(f"Train Name: PADATIK EXPRESS                      Train No: 12378")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 578 Km.")


def train_15986():
    print(f"Train Name: HWH SHATABDI EXPRESS                 Train No: 15986")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 581 Km.")


def train_15722():
    print(f"Train Name: PAHARIA EXPRESS                      Train No: 15722")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 580 Km.")


def train_19654():
    print(f"Train Name: KAMRUP EXPRESS                       Train No: 19654")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 575 Km.")


def train_15565():
    print(f"Train Name: SCL TVC EXPRESS                      Train No: 15565")
    print(f"From: New Jalpaiguri(NJP)                        To: Sealdha(SDHA)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Sealdha(SDHA)")
    print(f"Distance: 585 Km.")


# Trains which are travel from Sealdha to NJP.
def train_13176_R():
    print(f"Train Name: KUNCHAN JUNGHA EXPRESS               Train No: 13176")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 575 Km.")


def train_13142_R():
    print(f"Train Name: TEESTA TORSHA EXPRESS                Train No: 13142")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 580 Km.")


def train_13148_R():
    print(f"Train Name: UTTAR BANGA EXPRESS                  Train No: 13148")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 580 Km.")


def train_12344_R():
    print(f"Train Name: DARJEELING MAIL                      Train No: 13142")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 572 Km.")


def train_13150_R():
    print(f"Train Name: KANCHAN KANYA EXPRESS                Train No: 13150")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 576 Km.")


def train_12378_R():
    print(f"Train Name: PADATIK EXPRESS                      Train No: 12378")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 578 Km.")


def train_15986_R():
    print(f"Train Name: HWH SHATABDI EXPRESS                 Train No: 15986")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 581 Km.")


def train_15722_R():
    print(f"Train Name: PAHARIA EXPRESS                      Train No: 15722")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 580 Km.")


def train_19654_R():
    print(f"Train Name: KAMRUP EXPRESS                       Train No: 19654")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 575 Km.")


def train_15565_R():
    print(f"Train Name: SCL TVC EXPRESS                      Train No: 15565")
    print(f"From: Sealdha(SDHA)                              To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Sealdha(SDHA)                       Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 585 Km.")


# Train which are travel from sealdha to njp:
def sealdha_to_njp_SL():
    print()
    print("Train Name/Train Number/Available Seats/Fees In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        350/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        340/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          337/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          350/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          350/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         325/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_SL_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        250/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        240/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          237/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          250/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          250/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         225/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_1A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         2750/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         2150/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          2350/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          2500/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        2350/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         2350/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_1A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1375/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         1350/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          1350/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          1300/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        1350/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         1350/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_2A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1650/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        1500/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         1685/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           1685/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          1675/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         1650/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_2A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         850/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        800/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         885/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           885/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          875/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         850/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_3A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          1050/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        1200/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          1150/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          1100/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          950/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         1000/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def sealdha_to_njp_3A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          650/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        600/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          650/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          600/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          550/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         500/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          650/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          570/-")


def train_no_13176():
    print(f"KUNCHAN JUNGHA EXPRESS")


def train_no_13142():
    print(f"TEESTA TORSHA EXPRESS")


def train_no_13148():
    print(f"UTTAR BANGA EXPRESS")


def train_no_12344():
    print(f"DARJEELING MAIL")


def train_no_13150():
    print(f"KANCHAN KANYA EXPRESS")


def train_no_12378():
    print(f"PADATIK EXPRESS")


def train_no_15986():
    print(f"HWH SHATABDI EXPRESS")


def train_no_15722():
    print(f"PAHARIA EXPRESS")


def train_no_19654():
    print(f"KAMRUP EXPRESS")


def train_no_15565():
    print(f"SCL TVC EXPRESS")


# Trains NJP-->Malda

def njp_to_malda_sl():
    print()
    print("Train Name/Train Number/Available Seats/Fees In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)       193/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)       193/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)         193/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)         220/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)         190/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)        190/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)         190/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)         190/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)         193/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(12/195)        193/-")
    print(f"11          AGARTALA EXP                12500           Yes(95/165)        193/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(25/195)        193/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(56/195)        205/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(95/165)        195/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(52/195)        193/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(95/165)        193/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(52/195)        193/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(95/165)        193/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(82/195)        193/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(72/195)        195/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(95/165)        193/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(52/195)        193/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(95/165)        195/-")


# Fare of sleeper train which are travelling from njp to malda.
def fare_njp_to_malda_sl_13176():  # 1
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_13142():  # 2
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_13148():  # 3
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12344():  # 4
    print(f"Ticket Fare:                           220/-     Rupees Two Hundred Twenty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             237.7/-   Rupees Two Hundred Thirty Seven and Seven Paisa")


def fare_njp_to_malda_sl_13150():  # 5
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_njp_to_malda_sl_12378():  # 6
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_njp_to_malda_sl_15722():  # 7
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_njp_to_malda_sl_19654():  # 8
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_njp_to_malda_sl_15565():  # 9
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_13182():  # 10
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12500():  # 11
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_15640():  # 12
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12518():  # 13
    print(f"Ticket Fare:                           205/-     Rupees Two Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             222.7/-   Rupees Two Hundred Twenty TWo and Seven Paisa")


def fare_njp_to_malda_sl_55712():  # 14
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_13174():  # 15
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_15644():  # 16
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_75720():  # 17
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12508():  # 18
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12510():  # 19
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_22502():  # 20
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_12202():  # 21
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_12015():  # 22
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_njp_to_malda_sl_95745():  # 23
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def njp_to_malda_sl_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        92/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        92/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          92/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          110/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          95/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         95/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          95/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          95/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          92/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        92/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        95/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        92/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        92/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        92/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        90/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        92/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        92/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        92/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        92/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        92/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        92/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        92/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        90/-")


def fare_njp_to_malda_sl_sc_13176():  # 1
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_13142():  # 2
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_13148():  # 3
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12344():  # 4
    print(f"Ticket Fare:                           110/-     Rupees One Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             127.7/-   Rupees One Hundred Thirty Seven and Seven Paisa")


def fare_njp_to_malda_sl_sc_13150():  # 5
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_sc_12378():  # 6
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_sc_15722():  # 7
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_sc_19654():  # 8
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_sc_15565():  # 9
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_13182():  # 10
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12500():  # 11
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_njp_to_malda_sl_sc_15640():  # 12
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12518():  # 13
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_55712():  # 14
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_13174():  # 15
    print(f"Ticket Fare:                           90/-      Rupees Ninety Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             107.7/-   Rupees One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_sl_sc_15644():  # 16
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_75720():  # 17
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12508():  # 18
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12510():  # 19
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_22502():  # 20
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12202():  # 21
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_12015():  # 22
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_njp_to_malda_sl_sc_95745():  # 23
    print(f"Ticket Fare:                           90/-      Rupees Ninety Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             107.7/-   Rupees One Hundred Seven and Seven Paisa")


def njp_to_malda_1A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1100/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         1100/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          1100/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          1200/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        1100/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         1100/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          1100/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          950/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          1000/-")
    print(f"10          AGARTALA EXP                12500           Yes(152/195)        1000/-")
    print(f"11          KAMAKHA EXP                 15640           Yes(152/195)        1000/-")
    print(f"12          DIBRUGARH EXP               12518           Yes(152/195)        1000/-")
    print(f"13          GUWAHATI EXPRESS            12510           Yes(152/195)        1100/-")
    print(f"14          NEW TINSUKIA EXP            22502           Yes(152/195)        1000/-")
    print(f"15          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        1000/-")
    print(f"16          BAMANHAT EXPRESS            12015           Yes(152/195)        1100/-")
    print(f"17          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        1000/-")


def fare_njp_to_malda_1A_13176():  # 1
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_13142():  # 2
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_13148():  # 3
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_12344():  # 4
    print(f"Ticket Fare:                           1200/-    Rupees One Thousand Two Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1217.7/-  Rupees One Thousand Two Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_13150():  # 5
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_12378():  # 6
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_15722():  # 7
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_19654():  # 8
    print(f"Ticket Fare:                           950/-     Rupees Nine Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             967.7/-   Rupees Nine Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_15565():  # 9
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_12500():  # 10
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_15640():  # 11
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_12518():  # 12
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_12510():  # 13
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_22502():  # 14
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_12202():  # 15
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_12015():  # 16
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_njp_to_malda_1A_95745():  # 17
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def njp_to_malda_1A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         500/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         500/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          500/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          600/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        550/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         550/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          500/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          450/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          550/-")
    print(f"10          AGARTALA EXP                12500           Yes(152/195)        500/-")
    print(f"11          KAMAKHA EXP                 15640           Yes(152/195)        550/-")
    print(f"12          DIBRUGARH EXP               12518           Yes(152/195)        500/-")
    print(f"13          GUWAHATI EXPRESS            12510           Yes(152/195)        500/-")
    print(f"14          NEW TINSUKIA EXP            22502           Yes(152/195)        500/-")
    print(f"15          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        500/-")
    print(f"16          BAMANHAT EXPRESS            12015           Yes(152/195)        550/-")
    print(f"17          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        500/-")


def fare_njp_to_malda_1A_sc_13176():  # 1
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_13142():  # 2
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_13148():  # 3
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_12344():  # 4
    print(f"Ticket Fare:                           600/-     Rupees Six Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             617.7/-   Rupees Six Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_13150():  # 5
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12378():  # 6
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_15722():  # 7
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_19654():  # 8
    print(f"Ticket Fare:                           450/-     Rupees Four Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             467.7/-   Rupees Four Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_15565():  # 9
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12500():  # 10
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_1A_sc_15640():  # 11
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12518():  # 12
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12510():  # 13
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_22502():  # 14
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12202():  # 15
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_12015():  # 16
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_1A_sc_95745():  # 17
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def njp_to_malda_2A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         800/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        750/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         750/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           950/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          750/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         800/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          800/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          750/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        750/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        750/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        800/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        750/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        750/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        800/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        750/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        750/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        800/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        750/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        800/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        750/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        800/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        750/-")


def fare_njp_to_malda_2A_13176():  # 1
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_13142():  # 2
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_13148():  # 3
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_12344():  # 4
    print(f"Ticket Fare:                           950/-     Rupees Nine Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             967.7/-   Rupees Nine Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_13150():  # 5
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_12378():  # 6
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_15722():  # 7
    print(f"Ticket Fare:                           475/-     Rupees Four Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             492.7/-   Rupees Four Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_19654():  # 8
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_15565():  # 9
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_13182():  # 10
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_12500():  # 11
    print(f"Ticket Fare:                           700/-     Rupees Seven Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             717.7/-   Rupees Seven Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_15640():  # 12
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_12518():  # 13
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_55712():  # 14
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_13174():  # 15
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_15644():  # 16
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_75720():  # 17
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_12508():  # 18
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_12510():  # 19
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_22502():  # 20
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_12202():  # 21
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_2A_12015():  # 22
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_95745():  # 23
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def njp_to_malda_2A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         400/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        375/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         375/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           525/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          375/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         375/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          400/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          400/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          400/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        375/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        375/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        400/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        375/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        400/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        400/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        375/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        375/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        375/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        400/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        400/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        375/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        375/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        400/-")


def fare_njp_to_malda_2A_sc_13176():  # 1
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_13142():  # 2
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_13148():  # 3
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12344():  # 4
    print(f"Ticket Fare:                           525/-     Rupees Five Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             542.7/-   Rupees Five Hundred Fourty Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_13150():  # 5
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12378():  # 6
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_15722():  # 7
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_19654():  # 8
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_15565():  # 9
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_13182():  # 10
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12500():  # 11
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_15640():  # 12
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_12518():  # 13
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_55712():  # 14
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_13174():  # 15
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_15644():  # 16
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_75720():  # 17
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12508():  # 18
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12510():  # 19
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_22502():  # 20
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_2A_sc_12202():  # 21
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_12015():  # 22
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_njp_to_malda_2A_sc_95745():  # 23
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def njp_to_malda_3A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          550/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        550/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          500/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          650/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          500/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         550/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          550/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          500/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          500/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        500/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        500/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        550/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        500/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        550/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        500/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        550/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        550/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        500/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        550/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        500/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        500/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        500/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        500/-")


def fare_njp_to_malda_3A_13176():  # 1
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_13142():  # 2
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_13148():  # 3
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12344():  # 4
    print(f"Ticket Fare:                           650/-     Rupees Six Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             667.7/-   Rupees Six Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_13150():  # 5
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12378():  # 6
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_15722():  # 7
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_19654():  # 8
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_15565():  # 9
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_13182():  # 10
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12500():  # 11
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_15640():  # 12
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_12518():  # 13
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_55712():  # 14
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_13174():  # 15
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_15644():  # 16
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_75720():  # 17
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_12508():  # 18
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12510():  # 19
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_njp_to_malda_3A_22502():  # 20
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12202():  # 21
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_12015():  # 22
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_95745():  # 23
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def njp_to_malda_3A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          310/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        310/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          310/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          390/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          300/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         300/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          310/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          310/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          310/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        300/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        300/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        310/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        310/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        300/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        300/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        300/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        300/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        310/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        390/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        310/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        300/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        310/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        310/-")


def fare_njp_to_malda_3A_sc_13176():  # 1
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_13142():  # 2
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_13148():  # 3
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_12344():  # 4
    print(f"Ticket Fare:                           390/-     Rupees Three Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             407.7/-   Rupees Four Hundred Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_13150():  # 5
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_12378():  # 6
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_15722():  # 7
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_19654():  # 8
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_15565():  # 9
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_13182():  # 10
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_12500():  # 11
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_15640():  # 12
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_12518():  # 13
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_55712():  # 14
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_13174():  # 15
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_15644():  # 16
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_75720():  # 17
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_njp_to_malda_3A_sc_12508():  # 18
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_12510():  # 19
    print(f"Ticket Fare:                           390/-     Rupees Three Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             407.7/-   Rupees Four Hundred Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_22502():  # 20
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_12202():  # 21
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_12015():  # 22
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_njp_to_malda_3A_sc_95745():  # 23
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


#     Trains Malda---->Njp

def malda_to_njp_sl():
    print()
    print("Train Name/Train Number/Available Seats/Fees In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)       193/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)       193/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)         193/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)         220/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)         190/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)        190/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)         190/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)         190/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)         193/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(12/195)        193/-")
    print(f"11          AGARTALA EXP                12500           Yes(95/165)        193/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(25/195)        193/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(56/195)        205/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(95/165)        195/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(52/195)        193/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(95/165)        193/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(52/195)        193/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(95/165)        193/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(82/195)        193/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(72/195)        195/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(95/165)        193/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(52/195)        193/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(95/165)        195/-")


# Fare of sleeper train which are travelling from njp to malda.
def fare_malda_to_njp_sl_13176():  # 1
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_13142():  # 2
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_13148():  # 3
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12344():  # 4
    print(f"Ticket Fare:                           220/-     Rupees Two Hundred Twenty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             237.7/-   Rupees Two Hundred Thirty Seven and Seven Paisa")


def fare_malda_to_njp_sl_13150():  # 5
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_malda_to_njp_sl_12378():  # 6
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_malda_to_njp_sl_15722():  # 7
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_malda_to_njp_sl_19654():  # 8
    print(f"Ticket Fare:                           190/-     Rupees One Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             207.7/-   Rupees Two Hundred Seven and Seven Paisa")


def fare_malda_to_njp_sl_15565():  # 9
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_13182():  # 10
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12500():  # 11
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_15640():  # 12
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12518():  # 13
    print(f"Ticket Fare:                           205/-     Rupees Two Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             222.7/-   Rupees Two Hundred Twenty TWo and Seven Paisa")


def fare_malda_to_njp_sl_55712():  # 14
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_13174():  # 15
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_15644():  # 16
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_75720():  # 17
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12508():  # 18
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12510():  # 19
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_22502():  # 20
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_12202():  # 21
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_12015():  # 22
    print(f"Ticket Fare:                           193/-     Rupees One Hundred Nineteen Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             210.7/-   Rupees Two Hundred ten and Seven Paisa")


def fare_malda_to_njp_sl_95745():  # 23
    print(f"Ticket Fare:                           195/-     Rupees One Hundred Nineteen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             212.7/-   Rupees Two Hundred Twelve and Seven Paisa")


def malda_to_njp_sl_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In Sleeper Class")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(350/250)        92/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/310)        92/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/75)          92/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/68)          110/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          95/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         95/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          95/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          95/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          92/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        92/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        95/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        92/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        92/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        92/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        90/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        92/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        92/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        92/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        92/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        92/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        92/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        92/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        90/-")


# Fare of sleeper train which are travelling from njp to malda for sleeper senior citizen.
def fare_malda_to_njp_sl_sc_13176():  # 1
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_13142():  # 2
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_13148():  # 3
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12344():  # 4
    print(f"Ticket Fare:                           110/-     Rupees One Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             127.7/-   Rupees One Hundred Thirty Seven and Seven Paisa")


def fare_malda_to_njp_sl_sc_13150():  # 5
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_sc_12378():  # 6
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_sc_15722():  # 7
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_sc_19654():  # 8
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_sc_15565():  # 9
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_13182():  # 10
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12500():  # 11
    print(f"Ticket Fare:                           95/-      Rupees Ninety Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             112.7/-   Rupees One Hundred Twelve and Seven Paisa")


def fare_malda_to_njp_sl_sc_15640():  # 12
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12518():  # 13
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_55712():  # 14
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_13174():  # 15
    print(f"Ticket Fare:                           90/-      Rupees Ninety Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             107.7/-   Rupees One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_sl_sc_15644():  # 16
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_75720():  # 17
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12508():  # 18
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12510():  # 19
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_22502():  # 20
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12202():  # 21
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_12015():  # 22
    print(f"Ticket Fare:                           92/-      Rupees Nineteen Two and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             109.7/-   Rupees One Hundred nine and Seven Paisa")


def fare_malda_to_njp_sl_sc_95745():  # 23
    print(f"Ticket Fare:                           90/-      Rupees Ninety Three and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             107.7/-   Rupees One Hundred Seven and Seven Paisa")


def malda_to_njp_1A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         1100/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         1100/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          1100/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          1200/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        1100/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         1100/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          1100/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          950/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          1000/-")
    print(f"10          AGARTALA EXP                12500           Yes(152/195)        1000/-")
    print(f"11          KAMAKHA EXP                 15640           Yes(152/195)        1000/-")
    print(f"12          DIBRUGARH EXP               12518           Yes(152/195)        1000/-")
    print(f"13          GUWAHATI EXPRESS            12510           Yes(152/195)        1100/-")
    print(f"14          NEW TINSUKIA EXP            22502           Yes(152/195)        1000/-")
    print(f"15          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        1000/-")
    print(f"16          BAMANHAT EXPRESS            12015           Yes(152/195)        1100/-")
    print(f"17          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        1000/-")


def fare_malda_to_njp_1A_13176():  # 1
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_13142():  # 2
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_13148():  # 3
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_12344():  # 4
    print(f"Ticket Fare:                           1200/-    Rupees One Thousand Two Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1217.7/-  Rupees One Thousand Two Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_13150():  # 5
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_12378():  # 6
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_15722():  # 7
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_19654():  # 8
    print(f"Ticket Fare:                           950/-     Rupees Nine Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             967.7/-   Rupees Nine Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_15565():  # 9
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_12500():  # 10
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_15640():  # 11
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_12518():  # 12
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_12510():  # 13
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_22502():  # 14
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_12202():  # 15
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_12015():  # 16
    print(f"Ticket Fare:                           1100/-    Rupees One Thousand One Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1117.7/-  Rupees One Thousand One Hundred Seven and Seven Paisa")


def fare_malda_to_njp_1A_95745():  # 17
    print(f"Ticket Fare:                           1000/-    Rupees One Thousand and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             1017.7/-  Rupees One Thousand Seventeen and Seven Paisa")


def malda_to_njp_1A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 1-Tier(1A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         500/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(48/121)         500/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/85)          500/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/52)          600/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(121/132)        550/-")
    print(f"06          PADATIK EXP                 12378           Yes(25/165)         550/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          500/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          450/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          550/-")
    print(f"10          AGARTALA EXP                12500           Yes(152/195)        500/-")
    print(f"11          KAMAKHA EXP                 15640           Yes(152/195)        550/-")
    print(f"12          DIBRUGARH EXP               12518           Yes(152/195)        500/-")
    print(f"13          GUWAHATI EXPRESS            12510           Yes(152/195)        500/-")
    print(f"14          NEW TINSUKIA EXP            22502           Yes(152/195)        500/-")
    print(f"15          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        500/-")
    print(f"16          BAMANHAT EXPRESS            12015           Yes(152/195)        550/-")
    print(f"17          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        500/-")


def fare_malda_to_njp_1A_sc_13176():  # 1
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_13142():  # 2
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_13148():  # 3
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_12344():  # 4
    print(f"Ticket Fare:                           600/-     Rupees Six Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             617.7/-   Rupees Six Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_13150():  # 5
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12378():  # 6
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_15722():  # 7
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_19654():  # 8
    print(f"Ticket Fare:                           450/-     Rupees Four Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             467.7/-   Rupees Four Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_15565():  # 9
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12500():  # 10
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-  Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_1A_sc_15640():  # 11
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12518():  # 12
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12510():  # 13
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_22502():  # 14
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12202():  # 15
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_12015():  # 16
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_1A_sc_95745():  # 17
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def malda_to_njp_2A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         800/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        750/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         750/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           950/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          750/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         800/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          475/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          800/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          750/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        750/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        750/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        800/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        750/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        750/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        800/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        750/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        750/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        800/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        750/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        800/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        750/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        800/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        750/-")


def fare_malda_to_njp_2A_13176():  # 1
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_13142():  # 2
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_13148():  # 3
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_12344():  # 4
    print(f"Ticket Fare:                           950/-     Rupees Nine Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             967.7/-   Rupees Nine Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_13150():  # 5
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_12378():  # 6
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_15722():  # 7
    print(f"Ticket Fare:                           475/-     Rupees Four Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             492.7/-   Rupees Four Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_19654():  # 8
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_15565():  # 9
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_13182():  # 10
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_12500():  # 11
    print(f"Ticket Fare:                           700/-     Rupees Seven Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             717.7/-   Rupees Seven Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_15640():  # 12
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_12518():  # 13
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_55712():  # 14
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_13174():  # 15
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_15644():  # 16
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_75720():  # 17
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_12508():  # 18
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_12510():  # 19
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_22502():  # 20
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_12202():  # 21
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_2A_12015():  # 22
    print(f"Ticket Fare:                           800/-     Rupees Eight Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             817.7/-   Rupees Eight Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_95745():  # 23
    print(f"Ticket Fare:                           750/-     Rupees Seven Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             767.7/-   Rupees Seven Hundred Sixty Seven and Seven Paisa")


def malda_to_njp_2A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 2-Tier(2A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/250)         400/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(121/210)        375/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/175)         375/-")
    print(f"04          DARJEELING MAIL             12344           Yes(5/68)           525/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(25/95)          375/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/160)         375/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          400/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          400/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          400/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        375/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        375/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        400/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        375/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        400/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        400/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        375/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        375/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        375/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        400/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        400/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        375/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        375/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        400/-")


def fare_malda_to_njp_2A_sc_13176():  # 1
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_13142():  # 2
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_13148():  # 3
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12344():  # 4
    print(f"Ticket Fare:                           525/-     Rupees Five Hundred Twenty Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             542.7/-   Rupees Five Hundred Fourty Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_13150():  # 5
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12378():  # 6
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_15722():  # 7
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_19654():  # 8
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_15565():  # 9
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_13182():  # 10
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12500():  # 11
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_15640():  # 12
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_12518():  # 13
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_55712():  # 14
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_13174():  # 15
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_15644():  # 16
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_75720():  # 17
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12508():  # 18
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12510():  # 19
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_22502():  # 20
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_2A_sc_12202():  # 21
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_12015():  # 22
    print(f"Ticket Fare:                           375/-     Rupees Three Hundred Seventeen Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             392.7/-   Rupees Three Hundred Nineteen Two and Seven Paisa")


def fare_malda_to_njp_2A_sc_95745():  # 23
    print(f"Ticket Fare:                           400/-     Rupees Four Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             417.7/-   Rupees Four Hundred Seventeen and Seven Paisa")


def malda_to_njp_3A():
    print()
    print("Train Name/Train Number/Available Seats/Fees In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          550/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        550/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          500/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          650/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          500/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         550/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          550/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          500/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          500/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        500/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        500/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        550/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        500/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        550/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        500/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        550/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        550/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        500/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        550/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        500/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        500/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        500/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        500/-")


def fare_malda_to_njp_3A_13176():  # 1
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_13142():  # 2
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_13148():  # 3
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12344():  # 4
    print(f"Ticket Fare:                           650/-     Rupees Six Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             667.7/-   Rupees Six Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_13150():  # 5
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12378():  # 6
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_15722():  # 7
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_19654():  # 8
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_15565():  # 9
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_13182():  # 10
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12500():  # 11
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_15640():  # 12
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_12518():  # 13
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_55712():  # 14
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_13174():  # 15
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_15644():  # 16
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_75720():  # 17
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_12508():  # 18
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12510():  # 19
    print(f"Ticket Fare:                           550/-     Rupees Five Hundred Fifty and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             567.7/-   Rupees Five Hundred Sixty Seven and Seven Paisa")


def fare_malda_to_njp_3A_22502():  # 20
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12202():  # 21
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_12015():  # 22
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_95745():  # 23
    print(f"Ticket Fare:                           500/-     Rupees Five Hundred Five and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             517.7/-   Rupees Five Hundred Seventeen and Seven Paisa")


def malda_to_njp_3A_senior_citizen_male_female():
    print()
    print("Train Name/Train Number/Available Seats/Fees/Senior Citizen In AC 3-Tier(3A)")
    print()
    print(f"Sl No       Train Name                  Train Number    Available Seats     Fees")
    print()
    print(f"01          KUNCHAN JUNGHA EXPRESS      13176           Yes(35/40)          310/-")
    print(f"02          TEESTA TORSHA EXP           13142           Yes(125/210)        310/-")
    print(f"03          UTTAR BANGA EXP             13148           Yes(80/95)          310/-")
    print(f"04          DARJEELING MAIL             12344           Yes(25/98)          390/-")
    print(f"05          KANCHAN KANYA EXP           13150           Yes(85/95)          300/-")
    print(f"06          PADATIK EXP                 12378           Yes(95/165)         300/-")
    print(f"07          PAHARIA EXP                 15722           Yes(41/51)          310/-")
    print(f"08          KAMRUP EXPRESS              19654           Yes(11/25)          310/-")
    print(f"09          SCL TVC EXP                 15565           Yes(25/61)          310/-")
    print(f"10          SHILGHAT TOWN EXP-KOLKATA   13182           Yes(152/195)        300/-")
    print(f"11          AGARTALA EXP                12500           Yes(152/195)        300/-")
    print(f"12          KAMAKHA EXP                 15640           Yes(152/195)        310/-")
    print(f"13          DIBRUGARH EXP               12518           Yes(152/195)        310/-")
    print(f"14          MALDA TOWN PASSENGER        55712           Yes(152/195)        300/-")
    print(f"15          AGARTALA TOWN PASSENGER     13174           Yes(152/195)        300/-")
    print(f"16          HALDIBARI INTERCITY         15644           Yes(152/195)        300/-")
    print(f"17          SILIGURI-MALDA INTERCITY    75720           Yes(152/195)        300/-")
    print(f"18          SILCHAR PASSENGER           12508           Yes(152/195)        310/-")
    print(f"19          GUWAHATI EXPRESS            12510           Yes(152/195)        390/-")
    print(f"20          NEW TINSUKIA EXP            22502           Yes(152/195)        310/-")
    print(f"21          NEW ALIPURDUAR EXPRESS      12202           Yes(152/195)        300/-")
    print(f"22          BAMANHAT EXPRESS            12015           Yes(152/195)        310/-")
    print(f"23          DIGHA PAHARIA EXPRESS       95745           Yes(152/195)        310/-")


def fare_malda_to_njp_3A_sc_13176():  # 1
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_13142():  # 2
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_13148():  # 3
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_12344():  # 4
    print(f"Ticket Fare:                           390/-     Rupees Three Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             407.7/-   Rupees Four Hundred Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_13150():  # 5
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_12378():  # 6
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_15722():  # 7
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_19654():  # 8
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_15565():  # 9
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_13182():  # 10
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_12500():  # 11
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_15640():  # 12
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_12518():  # 13
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_55712():  # 14
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_13174():  # 15
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_15644():  # 16
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_75720():  # 17
    print(f"Ticket Fare:                           300/-     Rupees Three Hundred and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             317.7/-   Rupees Three Hundred Seventeen and Seven Paisa")


def fare_malda_to_njp_3A_sc_12508():  # 18
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_12510():  # 19
    print(f"Ticket Fare:                           390/-     Rupees Three Hundred Ninety and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             407.7/-   Rupees Four Hundred Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_22502():  # 20
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_12202():  # 21
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_12015():  # 22
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


def fare_malda_to_njp_3A_sc_95745():  # 23
    print(f"Ticket Fare:                           310/-     Rupees Three Hundred Ten and Zero Paisa")
    print(f"IRCTC Convenience Fee (Incl. of GST)   17.7/-    Rupees Seventeen and Seventy Paisa")
    print(f"Total Fare (all inclusive)             327.7/-   Rupees Three Hundred Twenty Seven and Seven Paisa")


##############################################################################################

# ---------------------------Trains which are from njp to malda--------------------------------#

def train_njp_to_malda_13176():  # 1
    print(f"Train Name: KUNCHAN JUNGHA EXPRESS               Train No: 13176")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_13142():  # 2
    print(f"Train Name: TEESTA TORSHA EXPRESS                Train No: 13142")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_13148():  # 3
    print(f"Train Name: UTTAR BANGA EXPRESS                  Train No: 13148")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 260 Km.")


def train_njp_to_malda_12344():  # 4
    print(f"Train Name: DARJEELING MAIL                      Train No: 12344")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 261 Km.")


def train_njp_to_malda_13150():  # 5
    print(f"Train Name: KANCHAN KANYA EXPRESS                Train No: 13150")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12378():  # 6
    print(f"Train Name: PADATIK EXPRESS                      Train No: 12378")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 267 Km.")


def train_njp_to_malda_15722():  # 7
    print(f"Train Name: PAHARIA EXPRESS                      Train No: 15722")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_19654():  # 8
    print(f"Train Name: KAMRUP EXPRESS                       Train No: 19654")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_15565():  # 9
    print(f"Train Name: SCL TVC EXPRESS                      Train No: 15565")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 267 Km.")


def train_njp_to_malda_13182():  # 10
    print(f"Train Name: SHILGHAT TOWN EXP-KOLKATA            Train No: 13182")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12500():  # 11
    print(f"Train Name: AGARTALA EXPRESS                     Train No: 12500")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 262 Km.")


def train_njp_to_malda_15640():  # 12
    print(f"Train Name: KAMAKHA EXPRESS                      Train No: 15640")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12518():  # 13
    print(f"Train Name: DIBRUGARH EXPRESS                    Train No: 12518")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 263 Km.")


def train_njp_to_malda_55712():  # 14
    print(f"Train Name: MALDA TOWN PASSENGER                 Train No: 55712")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_13174():  # 15
    print(f"Train Name: AGARTALA TOWN PASSENGER              Train No: 13174")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_15644():  # 16
    print(f"Train Name: HALDIBARI INTERCITY                  Train No: 15644")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_75720():  # 17
    print(f"Train Name: SILIGURI-MALDA INTERCITY             Train No: 75720")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 266 Km.")


def train_njp_to_malda_12508():  # 18
    print(f"Train Name: SILCHAR PASSENGER                    Train No: 12508")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12510():  # 19
    print(f"Train Name: GUWAHATI EXPRESS                     Train No: 12510")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 266 Km.")


def train_njp_to_malda_22502():  # 20
    print(f"Train Name: NEW TINSUKIA EXPRESS                 Train No: 22502")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12202():  # 21
    print(f"Train Name: NEW ALIPURDUAR EXPRESS               Train No: 12202")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_12015():  # 22
    print(f"Train Name: BAMANHAT EXPRESS                     Train No: 12015")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


def train_njp_to_malda_95745():  # 23
    print(f"Train Name: DIGHA PAHARIA EXPRESS                Train No: 95745")
    print(f"From: New Jalpaiguri(NJP)                        To: Malda(MLD)")
    print(f"Boarding At: New Jalpaiguri(NJP)                 Resv. Upto: Malda(MLD)")
    print(f"Distance: 265 Km.")


#################################################################################################
# -----------------------Trains which are travelling from malda to njp-------------------------#

def train_malda_to_njp_13176():  # 1
    print(f"Train Name: KUNCHAN JUNGHA EXPRESS               Train No: 13176")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_13142():  # 2
    print(f"Train Name: TEESTA TORSHA EXPRESS                Train No: 13142")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_13148():  # 3
    print(f"Train Name: UTTAR BANGA EXPRESS                  Train No: 13148")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 260 Km.")


def train_malda_to_njp_12344():  # 4
    print(f"Train Name: DARJEELING MAIL                      Train No: 12344")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 261 Km.")


def train_malda_to_njp_13150():  # 5
    print(f"Train Name: KANCHAN KANYA EXPRESS                Train No: 13150")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12378():  # 6
    print(f"Train Name: PADATIK EXPRESS                      Train No: 12378")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 267 Km.")


def train_malda_to_njp_15722():  # 7
    print(f"Train Name: PAHARIA EXPRESS                      Train No: 15722")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_19654():  # 8
    print(f"Train Name: KAMRUP EXPRESS                       Train No: 19654")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_15565():  # 9
    print(f"Train Name: SCL TVC EXPRESS                      Train No: 15565")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 267 Km.")


def train_malda_to_njp_13182():  # 10
    print(f"Train Name: SHILGHAT TOWN EXP-KOLKATA            Train No: 13182")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12500():  # 11
    print(f"Train Name: AGARTALA EXPRESS                     Train No: 12500")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 262 Km.")


def train_malda_to_njp_15640():  # 12
    print(f"Train Name: KAMAKHA EXPRESS                      Train No: 15640")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12518():  # 13
    print(f"Train Name: DIBRUGARH EXPRESS                    Train No: 12518")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 263 Km.")


def train_malda_to_njp_55712():  # 14
    print(f"Train Name: MALDA TOWN PASSENGER                 Train No: 55712")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_13174():  # 15
    print(f"Train Name: AGARTALA TOWN PASSENGER              Train No: 13174")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_15644():  # 16
    print(f"Train Name: HALDIBARI INTERCITY                  Train No: 15644")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_75720():  # 17
    print(f"Train Name: SILIGURI-MALDA INTERCITY             Train No: 75720")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 266 Km.")


def train_malda_to_njp_12508():  # 18
    print(f"Train Name: SILCHAR PASSENGER                    Train No: 12508")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12510():  # 19
    print(f"Train Name: GUWAHATI EXPRESS                     Train No: 12510")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 266 Km.")


def train_malda_to_njp_22502():  # 20
    print(f"Train Name: NEW TINSUKIA EXPRESS                 Train No: 22502")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12202():  # 21
    print(f"Train Name: NEW ALIPURDUAR EXPRESS               Train No: 12202")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_12015():  # 22
    print(f"Train Name: BAMANHAT EXPRESS                     Train No: 12015")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


def train_malda_to_njp_95745():  # 23
    print(f"Train Name: DIGHA PAHARIA EXPRESS                Train No: 95745")
    print(f"From: Malda(MLD)                                 To: New Jalpaiguri(NJP)")
    print(f"Boarding At: Malda(MLD)                          Resv. Upto: New Jalpaiguri(NJP)")
    print(f"Distance: 265 Km.")


# create function which are travelling from njp---->malda


def booking_njp_malda():
    date = input("Date: ")
    n = int(input("How many passenger are going: "))
    sh = input("Are you Senior Citizen(yes/no): ")
    av = input("Are you want to show availabe trains(yes/no): ")
    cla = input("Class(AC 3A/AC 2A/AC 1A/Sleeper): ")
    if sh in ('YES', 'Y', 'yes', 'Yes'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                njp_to_malda_sl_senior_citizen_male_female()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                njp_to_malda_1A_senior_citizen_male_female()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                njp_to_malda_2A_senior_citizen_male_female()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                njp_to_malda_3A_senior_citizen_male_female()
            else:
                "break"
        elif av in ('No', 'no', 'NO', 'n'):
            "break"
        else:
            "break"
    elif sh in ('No', 'no', 'NO', 'n'):
        if av in ('YES', 'Y', 'yes', 'Yes'):
            if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
                njp_to_malda_sl()
            elif cla in ('AC 1A', 'ac 1a', 'A1A'):
                njp_to_malda_1A()
            elif cla in ('AC 2A', 'ac 2a', 'A2A'):
                njp_to_malda_2A()
            elif cla in ('AC 3A', 'ac 3a', 'A3A'):
                njp_to_malda_3A()
    print()
    tra = input("Which train you want to travel: ")
    tra_no = int(input("Enter Train Number: "))
    #   1. Train Number: 13176
    #   Train Name: KUNCHAN JUNGHA EXPRESS

    if tra_no == 13176:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13176()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_13176()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13176()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13176()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13176()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13176()
        else:
            "break"

    #   2. Train Number: 13142
    #   Train Name: TEESTA TORSHA EXPRESS
    if tra_no == 13142:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13142()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_13142()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13142()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13142()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13142()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13142()
        else:
            "break"
    #   3.  Train Number: 13148
    #       Train Name: UTTAR BANGA EXP
    if tra_no == 13148:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13148()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_13148()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13148()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13148()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13148()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13148()
        else:
            "break"

    #   4.  Train Number: 12344
    #       Train Name: DARJEELING MAIL.
    if tra_no == 12344:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12344()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12344()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12344()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12344()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12344()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12344()
        else:
            "break"

    #   5.  Train Number: 13150
    #       Train Name: KANCHAN KANYA EXP.
    if tra_no == 13150:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13150()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_13150()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13150()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13150()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13150()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13150()
        else:
            "break"
    #   6.  Train Number: 12378
    #       Train Name: PADATIK EXPRESS

    if tra_no == 12378:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12378()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12378()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12378()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12378()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12378()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12378()
        else:
            "break"
    #   7.  Train Number: 15722
    #       Train Name: PAHARIA EXPRESS

    if tra_no == 15722:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_15722()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_15722()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_15722()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_15722()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15722()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_15722()
        else:
            "break"
    #   8.  Train Number: 19654
    #       Train Name: KAMRUP EXPRESS
    if tra_no == 19654:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_19654()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_19654()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_19654()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_19654()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_19654()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_19654()
        else:
            "break"
    #   9.  Train Number: 15565
    #       Train Name: SCL TVC EXPRESS

    if tra_no == 15565:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_15565()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_15565()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_15565()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_15565()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15565()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_15565()
        else:
            "break"
    #   10. Train Number: 13182
    #       Train Name: SHILGHAT TOWN EXP-KOLKATA

    if tra_no == 13182:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13182()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13182()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("N0 seat avaliable in 1A")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13182()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13182()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13182()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13182()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13182()
        else:
            "break"
    #   11. Train Number: 12500
    #       Train Name: AGARTALA EXPRESS
    if tra_no == 12500:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12500()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12500()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12500()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12500()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12500()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12500()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12500()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12500()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12500()
        else:
            "break"
    #   12. Train Number: 15640
    #       Train Name: KAMAKHA EXPRESS

    if tra_no == 15640:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_15640()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_15640()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_15640()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_15640()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_15640()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_15640()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_15640()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15640()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_15640()
        else:
            "break"
    #   13. Train Number: 12518
    #       Train Name: DIBRUGARH EXPRESS

    if tra_no == 12518:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12518()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12518()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12518()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12518()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12518()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12518()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12518()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12518()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12518()
        else:
            "break"

    #   14. Train Number: 55712
    #       Train Name: MALDA TOWN PASSENGER

    if tra_no == 55712:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_55712()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_55712()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("Seats are not available.")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_55712()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_55712()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_55712()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_55712()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_55712()
        else:
            "break"
    #   15. Train Number: 13174
    #       Train Name: AGARTALA TOWN PASSENGER

    if tra_no == 55712:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_13174()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_13174()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("Seats are not available.")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_13174()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_13174()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_13174()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_13174()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_13174()
        else:
            "break"
    #   16. Train Number: 15644
    #       Train Name: HALDIBARI INTERCITY

    if tra_no == 15644:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_15644()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_15644()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("Seats are not available.")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_15644()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_15644()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_15644()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_15644()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_15644()
        else:
            "break"
    #   17. Train Number: 75720
    #       Train Name: SILIGURI-MALDA INTERCITY

    if tra_no == 75720:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_75720()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_75720()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("Seats are not available.")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_75720()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_75720()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_75720()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_75720()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_75720()
        else:
            "break"
    #   18. Train Number: 12508
    #       Train Name: SILCHAR PASSENGER

    if tra_no == 12508:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12508()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12508()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            print("Seats are not available.")
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12508()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12508()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12508()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12508()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12508()
        else:
            "break"
    #   19. Train Number: 12510
    #       Train Name: GUWAHATI EXPRESS

    if tra_no == 12510:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12510()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12510()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12510()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12510()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12510()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12510()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12510()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12510()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12510()
        else:
            "break"
    #   20. Train Number: 22502
    #       Train Name: NEW TINSUKIA EXPRESS

    if tra_no == 22502:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_22502()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_22502()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_22502()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_22502()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_22502()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_22502()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_22502()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_22502()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_22502()
        else:
            "break"
    #   21. Train Number: 12202
    #       Train Name: NEW ALIPURDUAR EXPRESS

    if tra_no == 12202:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12202()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12202()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12202()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12202()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12202()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12202()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12202()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12202()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12202()
        else:
            "break"
    #   22. Train Number: 12015
    #       Train Name: BAMANHAT EXPRESS

    if tra_no == 12015:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_12015()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_12015()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_12015()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_12015()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_12015()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_12015()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_12015()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_12015()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_12015()
        else:
            "break"
    #   23. Train Number: 95745
    #       Train Name: DIGHA PAHARIA EXPRESS

    if tra_no == 95745:
        if cla in ('Sleeper', 'slp', 'sleeper', 'SLP'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_95745()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_sl_sc_95745()
        elif cla in ('AC 1A', 'ac 1a', 'A1A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_95745()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_1A_sc_95745()
        elif cla in ('AC 2A', 'ac 2a', 'A2A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_95745()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_2A_sc_95745()
        elif cla in ('AC 3A', 'ac 3a', 'A3A'):
            for i in range(n):
                na = input("Passenger Name: ")
                age = int(input("Age: "))
                gen = input("Gender(Male/Female/Others): ")
            add = input("Address: ")
            ph = int(input("Phone No: "))
            if age < 60 or sh in ('No', 'no', 'NO', 'n'):
                con1 = "None"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_95745()
            elif age >= 60 or sh in ('YES', 'Y', 'yes', 'Yes'):
                con1 = "SRCTZN"
                bok = "CNF"  # Booking Can Check latter:
                print()
                print(f"----------------------------------------------------------------------------------------------")
                print(f"INFORMATION E-Ticket PASSENGER: ")
                print(f"----------------------------------------------------------------------------------------------")
                default()
                train_njp_to_malda_95745()
                print(f"Date Of Journey: {date}")
                print(f"Date Of Arrival: {date}")
                print(f"Passenger Phone No: {ph}")
                print(f"No Of Passenger: {n}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"PASSENGER DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"Passenger Name: {na}")
                print(f"Age:{age}                                        Gender:{gen}")
                print(f"Concession: {con1}")
                print(f"Booking Status: {bok}")
                print(f"Address: {add}")
                print(f"----------------------------------------------------------------------------------------------")
                print(f"FARE DETAILS: ")
                print(f"----------------------------------------------------------------------------------------------")
                fare_njp_to_malda_3A_sc_95745()
        else:
            "break"

    else:
        print("Wrong Choice")


inputt()
