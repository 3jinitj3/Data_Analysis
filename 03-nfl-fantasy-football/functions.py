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