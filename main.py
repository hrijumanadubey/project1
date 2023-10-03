# IMPORTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from typing import List, Type


# SETUP
URL = r"http://aws.imd.gov.in:8091/state.php?id=TAMIL_NADU"
driver = webdriver.Firefox()


# HELPER FUNCTIONS
def open_url(url: str) -> None:
    """
    Opens the URL
    """
    try:
        driver.get(url)
    except Exception as e:
        print("Error opening URL: ", e)


def click_tabular_data() -> None:
    """
    Clicks the 'Tabular Data/Graph' button
    """
    try:
        tabular_data = driver.find_element(By.ID, "b")
        tabular_data.click()
    except Exception as e:
        print("Error clicking Tabular Data button: ", e)


def select_district() -> None:
    """
    Selects the 'Chengalpattu' district from the district dropdown
    """
    district_dropdown_element = driver.find_element(By.ID, "dis")
    district_dropdown = Select(district_dropdown_element)
    district_dropdown.select_by_visible_text("CHENGALPATTU")


def select_station() -> None:
    """
    Selects the 'VIT_CHENNAI' station from the station dropdown
    """
    station_dropdown_element = driver.find_element(By.ID, "stat")
    station_dropdown = Select(station_dropdown_element)
    station_dropdown.select_by_visible_text("VIT_CHENNAI")


def click_view_data() -> None:
    """
    Clicks the 'View Data' button
    """
    try:
        view_data = driver.find_element(By.ID, "dataview")
        view_data.click()
    except Exception as e:
        print("Error clicking View Data button: ", e)


def get_table() -> Type[WebElement]:
    """
    Get the weather table data
    """
    try:
        return driver.find_element(By.TAG_NAME, "table")

    except Exception as e:
        print("Error getting table data: ", e)


def get_table_headings(table: Type[WebElement]) -> List[str]:
    """
    Get the table headings
    """
    try:
        headings = table.find_elements(By.TAG_NAME, "th")
        return [heading.text for heading in headings]

    except Exception as e:
        print("Error getting table headings: ", e)


def get_table_rows(table: Type[WebElement]) -> List[Type[WebElement]]:
    """
    Get the table rows
    """
    try:
        rows = table.find_elements(By.TAG_NAME, "tr")
        return rows

    except Exception as e:
        print("Error getting table rows: ", e)


def get_table_data() -> List[List[str]]:
    """
    Get the table data
    """
    try:
        table = get_table()
        headings = get_table_headings(table)
        rows = get_table_rows(table)

        table_data = []
        table_data.append(headings)
        for row in rows:
            row_data = []
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                row_data.append(cell.text)
            table_data.append(row_data)

        return table_data

    except Exception as e:
        print("Error getting table data: ", e)


# MAIN FUNCTION
def main():
    open_url(URL)
    sleep(10)

    click_tabular_data()
    sleep(10)

    select_district()
    sleep(10)

    select_station()
    sleep(10)

    click_view_data()
    sleep(10)

    table_data = get_table_data()
    print(table_data)
    sleep(10)

    driver.quit()


# MAIN CALL
if _name_ == "_main_":
    main()
