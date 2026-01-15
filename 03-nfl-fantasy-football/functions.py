import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import datetime

class ValidSeasonError(Exception):
    def __init__(self, season):
        self.season = season

    def __str__(self):
        return "The " + str(self.season) + " Season is not within the database ranging from 1970 to the current season. "
    
class NFLDataScraper:
    def __init__(self):
        self.base_url = "https://www.nfl.com"
        self.current_season = None
        self.current_week = None
        self.current_date = datetime.date.today()
        self.adjusted_start_date = datetime.date(self.current_date.year - 1, 9, 7) if 1 <= self.current_date.month <= 5 else datetime.date(self.current_date.year, 9, 7)
        self.unit_link = {
            "player": {},
            "team": {}
        }
        self.season = None
        print(f"|---| Current Date: {self.current_date}, Adjusted Start Date: {self.adjusted_start_date} |---|")

    def set_current_season_and_week(self):
        if self.current_date > self.adjusted_start_date:
            self.current_season = self.current_date.year - 1
        else:
            self.current_season = int(self.current_date.year)
        self.days_since_season_start = (self.current_date - self.adjusted_start_date).days
        self.current_week = (self.days_since_season_start // 7) + 1
        print(f"Current Season: {self.current_season}, Current Week: {self.current_week}")

    def get_links(self, level):
        if level == "player":
            # Request the raw HTML for player statistics page
            html = requests.get("https://www.nfl.com/stats/player-stats/")
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html.content, "html.parser")
            # Find all list items with class 'd3-o-tabs__list-item'
            li_elements = soup.find_all("li", class_ = "d3-o-tabs__list-item")
        elif level == "team":
            # Request the raw HTML for team statistics page
            html = requests.get("https://www.nfl.com/stats/team-stats/")
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html.content, "html.parser")
            # Find the unordered list element with class "d3-o-tabbed-controls-selector__list"
            ul_element = soup.find("ul", class_ = "d3-o-tabbed-controls-selector__list")
            # Find all list items within the unordered list
            li_elements = ul_element.find_all("li")

        # Initialize a list to store the href values
        href_values = []

        # Iterate through the list items and extract href values from anchor tags
        for li in li_elements:
            a_tag = li.find("a")
            if a_tag:
                href = a_tag["href"]
                href_values.append(href)

        # List to store the links
        links = []

        # Loop through href_values and fetch links for each URL
        for href in href_values:
            url = self.base_url + href
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser")
            # Find all list items with class "d3-o-tabs__list-item"
            a_elements = soup.find_all("li", class_ = "d3-o-tabs__list-item")
            # Extract and store links from anchor tags
            links += [self.base_url + element.find("a")["href"] for element in a_elements]

        # Replace "2023" with the value of the season variable we want to scrape
        links = [link.replace("2023", str(self.season)) for link in links]

        return links
    
    def get_sub_pages(self, unit_links):
        # Create dictionary to store the category names and their corresponding page links
        sub_pages = {}
        base_url = "https://www.nfl.com" # Assuming you have a base URL

        for unit, category_links in unit_links.items():
            sub_pages[unit] = {}

            for category, link in category_links.items():
                page_count = 0 # Initialize page count
                current_link = link # Use the provided link as the starting point
                current_stat = category # Set the current_stat to the category name

                # Initialize the category's dictionary
                sub_pages[unit][current_stat] = {page_count: current_link}

                # Create an infinite loop to scrape data from multiple pages
                while True:
                    # Request raw HTML for the current page
                    response = requests.get(current_link)

                    # Check if the request was successful
                    if response.status_code == 200:
                        # Create a BeautifulSoup object to parse the HTML
                        soup = BeautifulSoup(response.content, "html.parser")

                        # Find the "Next Page" link
                        next_page_link = soup.find("a", class_ = "nfl-o-table-pagination__next")

                        if next_page_link:
                            # Extract the href attribute
                            href = next_page_link["href"]

                            # Update current link with the next page's URL
                            current_link = base_url + href
                            page_count += 1 # Increment page count

                            # Add the link to the category's dictionary
                            sub_pages[unit][current_stat][page_count] = current_link
                        else:
                            print(f"No more pages to scrape for {unit} - {current_stat}.")
                            break # Exit the loop when there are no more pages
                    else:
                        print(f"Error: Unable to fetch data from {current_link} for {unit} - {current_stat}.")
                        break # Exit the loop on request error
        
        # Display the collected category pages and their links
        for unit, categories in sub_pages.items():
            for category, pages in categories.items():
                print(f"{unit} - {category} Sub-Pages:")
                for page_num, page_link in pages.items():
                    print(f"Page {page_num}: {page_link}")
        return sub_pages
                                              