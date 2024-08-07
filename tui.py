def display_menu():
    print("Main Menu:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")


def get_main_menu_choice():
    choice = input("Enter your choice (A/B/X): ").strip().upper()
    while choice not in ['A', 'B', 'X']:
        print(f"Invalid choice '{choice}'. Please enter A, B, or X.")
        choice = input("Enter your choice (A/B/X): ").strip().upper()
    return choice


def display_sub_menu_A():
    print("Please enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    sub_choice = input("Enter your choice (A-D): ").strip().upper()
    while sub_choice not in ['A', 'B', 'C', 'D']:
        print(f"Invalid choice '{sub_choice}'. Please enter A, B, C, or D.")
        sub_choice = input("Enter your choice (A-D): ").strip().upper()
    return sub_choice


def display_sub_menu_B():
    print("Please enter one of the following options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    sub_choice = input("Enter your choice (A-D): ").strip().upper()
    while sub_choice not in ['A', 'B', 'C', 'D']:
        print(f"Invalid choice '{sub_choice}'. Please enter A, B, C, or D.")
        sub_choice = input("Enter your choice (A-D): ").strip().upper()
    return sub_choice


def get_park_name():
    park_name = input("Enter the name of the park: ").strip()
    return park_name


def get_year():
    while True:
        year_str = input("Enter the year (e.g., 2023): ").strip()
        if year_str.isdigit():
            return int(year_str)
        else:
            print(f"Invalid year '{year_str}'. Please enter a valid year.")
