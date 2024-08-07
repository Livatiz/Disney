import csv
from collections import Counter, defaultdict
from datetime import datetime


def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            data.append(headers)  # Add headers to the data
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
    return data


def get_column_index(header_row, column_name):
    try:
        return header_row.index(column_name)
    except ValueError:
        print(f"Error: Column '{column_name}' not found in the header.")
        return None


def view_reviews_by_park(data, park_name):
    park_index = get_column_index(data[0], "Branch")
    if park_index is None:
        return

    reviews = [row for row in data[1:] if row[park_index].lower() == park_name.lower()]
    if reviews:
        print(f"\nReviews for {park_name}:")
        for review in reviews:
            print(review)
    else:
        print(f"No reviews found for park: {park_name}")


def number_of_reviews_by_park_and_location(data):
    park_index = get_column_index(data[0], "Branch")
    location_index = get_column_index(data[0], "Reviewer_Location")

    if park_index is None or location_index is None:
        return

    park_location_count = defaultdict(Counter)

    for row in data[1:]:
        park = row[park_index]
        location = row[location_index]
        park_location_count[park][location] += 1

    print("Number of Reviews by Park and Reviewer Location:")
    for park, locations in park_location_count.items():
        print(f" {park}:")
        for location, count in locations.items():
            print(f"  {location}: {count} reviews")


def average_score_per_year_by_park(data, park_name, year):
    relevant_reviews = (review for review in data
                        if review['Branch'] == park_name
                        and review['year_month'].startswith(str(year)))

    name_rating = [int(review['Rating']) for review in relevant_reviews]
    if len(name_rating) > 0:
        average_score = sum(name_rating) / len(name_rating)
        print(f"The average score for {park_name} and in the year{year} is {average_score : .2f}. ")
    else:
        print(f"No reviews found in selected year{year} for {park_name}:")


def number_of_reviews_by_park(data):
    park_index = get_column_index(data[0], "Branch")
    if park_index is None:
        return

    review_count_by_park = defaultdict(int)

    for row in data[1:]:
        park = row[park_index]
        review_count_by_park[park] += 1

    return review_count_by_park


def average_score_per_year_by_park(data, park_name, year):
    park_index = get_column_index(data[0], "Branch")
    date_index = get_column_index(data[0], "Year_Month")
    score_index = get_column_index(data[0], "Rating")

    if park_index is None or date_index is None or score_index is None:
        return

    scores = []

    for row in data[1:]:
        try:
            date_str = row[date_index]
            if date_str.lower() == 'missing' or date_str == '':
                continue
            date = datetime.strptime(date_str, "%Y-%m")
            print(f"Processing row: Date={date}, Park={row[park_index]}, Rating={row[score_index]}")
            if date.year == year and row[park_index].lower() == park_name.lower():
                score = float(row[score_index])
                scores.append(score)
        except ValueError as e:
            print(f"Error parsing row: {row} - {str(e)}")
            continue

    if scores:
        average_score = sum(scores) / len(scores)
        print(f"\nAverage rating for {park_name} in {year}: {average_score:.2f}")
    else:
        print(f"No reviews found for {park_name} in {year}.")


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


def most_reviewed_park(data):
    park_index = get_column_index(data[0], "Branch")
    if park_index is None:
        return

    park_reviews = [row[park_index] for row in data[1:]]
    park_count = Counter(park_reviews)

    most_reviewed = park_count.most_common(1)
    if most_reviewed:
        park, count = most_reviewed[0]
        print(f"The most reviewed park is {park} with {count} reviews.")
    else:
        print("No reviews found.")


def average_score_per_park_by_location(data):
    park_index = get_column_index(data[0], "Branch")
    location_index = get_column_index(data[0], "Reviewer_Location")
    score_index = get_column_index(data[0], "Rating")

    if park_index is None or location_index is None or score_index is None:
        return

    scores_by_park_and_location = defaultdict(lambda: defaultdict(list))

    for row in data[1:]:
        try:
            park = row[park_index]
            location = row[location_index]
            score = float(row[score_index])
            scores_by_park_and_location[park][location].append(score)
        except ValueError as e:
            print(f"Error parsing row: {row} - {str(e)}")
            continue

    print("Average Score per Park by Reviewer Location:")
    for park, locations in scores_by_park_and_location.items():
        print(f"Park: {park}")
        for location, scores in locations.items():
            average_score = sum(scores) / len(scores)
            print(f"  {location}: {average_score:.2f}")