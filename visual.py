"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""
import matplotlib.pyplot as plt


def plot_pie_chart(data):
    labels = data.keys()
    sizes = data.values()

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title("Number of Reviews per Park")
    plt.show()


def plot_top_10_locations(data, park_name):
    if data:
        locations, scores = zip(*data)

        plt.figure(figsize=(10, 6))
        plt.barh(locations, scores, color='skyblue')
        plt.xlabel('Average Rating')
        plt.ylabel('Location')
        plt.title(f'Top 10 Locations with Highest Average Rating for {park_name}')
        plt.gca().invert_yaxis()  # Invert y-axis to show the highest rating at the top
        plt.show()
    else:
        print(f"No reviews found for park: {park_name}")
