from robocorp import browser
import requests
from RPA.HTTP import HTTP
from RPA.Tables import Tables
from Locators import Locators as loc

class OrderRobot:
    def __init__(self):
        self.order_page_url = 'https://robotsparebinindustries.com/#/robot-order'
        self.order_csv_url = 'https://robotsparebinindustries.com/orders.csv'
        self.local_csv_filename = 'orders.csv'

    def open_robot_order_website(self):
        browser.goto(self.order_page_url)

    def get_orders(self):
        http = HTTP()
        http.download(self.order_csv_url, overwrite=True)
        library = Tables()
        orders = library.read_table_from_csv(
            self.local_csv_filename, columns=[
                "Order Number",
                "Head",
                "Body",
                "Legs",
                "Address"
                ]
        )
        return orders

    def close_annoying_modal(self):
        page = browser.page()
        page.click(loc.modal_button_xpath)

    def fill_the_form(self):
        pass

    def run(self):
        self.open_robot_order_website()
        orders = self.get_orders()
        # print(type(orders))
        for row in orders:
            print(row)
        self.close_annoying_modal()