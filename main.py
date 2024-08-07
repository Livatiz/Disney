"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
import process
import visual


print("--------------------------")
print("DisneyLand Review Analyzer")
print("--------------------------")


def main():
    file_path = r'C:\Users\Lavitz\Desktop\Phyton\disneyland_reviews.csv'
    data = process.read_csv_file(file_path)
    if not data:
        print("No data found or failed to read the file.")
        return

    num_rows = len(data)
    print(f"Finished reading the dataset. The dataset contains {num_rows} rows.")

    try:
        while True:
            tui.display_menu()
            choice = tui.get_main_menu_choice()

            if choice == 'A':
                sub_choice = tui.display_sub_menu_A()
                if sub_choice == 'A':
                    park_name = tui.get_park_name()
                    process.view_reviews_by_park(data, park_name)
                elif sub_choice == 'B':
                    process.number_of_reviews_by_park_and_location(data)
                elif sub_choice == 'C':
                    park_name = tui.get_park_name()
                    year = tui.get_year()
                    process.average_score_per_year_by_park(data, park_name, year)
                elif sub_choice == 'D':
                    process.average_score_per_park_by_location(data)
            elif choice == 'B':
                sub_choice = tui.display_sub_menu_B()
                if sub_choice == 'A':
                    review_data = process.number_of_reviews_by_park(data)
                    visual.plot_pie_chart(review_data)
                elif sub_choice == 'B':
                    park_name = tui.get_park_name()
                    location_data = process.top_10_locations_highest_avg_rating(data, park_name)
                    visual.plot_top_10_locations(location_data, park_name)
            elif choice == 'X':
                print("Exiting the program.")
                break
            else:
                print(f"Invalid choice '{choice}'. Please enter A, B, or X.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")


if __name__ == "__main__":
    main()

