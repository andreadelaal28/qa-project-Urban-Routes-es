import time
import data
from pages import UrbanRoutesPage
from helpers import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_1_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_2_set_comfort_tariff(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        comfort_tariff = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == 'Comfort'

    def test_3_add_phone_number(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_confirm_button()
        time.sleep(2)
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(code)
        self.routes_page.click_sms_confirm_button()
        assert self.routes_page.get_phone_number() == data.phone_number

    def test_4_add_credit_card(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_option()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_card_add_button()
        assert self.routes_page.get_card_added_confirmation() == 'Tarjeta'

    def test_5_add_message(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.set_message(data.message_for_driver)
        assert self.routes_page.get_message() == data.message_for_driver

    def test_6_blanket_button(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_blanket_button()
        assert self.routes_page.is_blanket_selected() is True

    def test_7_order_two_ice_creams(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.order_ice_creams(2)
        assert self.routes_page.get_ice_cream_count() == '2'

    def test_8_search_taxi_modal_appears(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_confirm_button()
        time.sleep(2)
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(code)
        self.routes_page.click_sms_confirm_button()
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_option()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_card_add_button()
        assert self.routes_page.get_card_added_confirmation() == 'Tarjeta'
        self.routes_page.click_final_order_button()
        self.routes_page.wait_for_search_taxi_modal()
        header_text = self.routes_page.get_order_header_text()
        assert header_text != ''

    def teardown_method(self):
        self.driver.quit()