"""
 Copyright (c) 2022 GNU GENERAL PUBLIC

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """
import time
import requests
import random
from bs4 import BeautifulSoup
from helper import printer
from utils.randomuser import users


class Search:
    """
    Searches for a given query on DuckDuckGo.

    :param query: The query to search for.
    """
    def __init__(self, query):
        url = "https://duckduckgo.com/html/?q=" + query
        headers = {"User-Agent": random.choice(users)}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("div", {"class": "result__body"})

        if len(results) == 0:
            printer.error(f"Error : No results found for {query}..!")
            return

        printer.info(f"Searching for '{query}' -- With the agent {headers['User-Agent']}")
        time.sleep(1)
        for result in results:
            title = result.find("a", {"class": "result__a"}).text
            link = result.find("a", {"class": "result__a"})["href"]
            printer.success(f"{title} - {link}")
