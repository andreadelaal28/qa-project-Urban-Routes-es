# pages.py
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_button = (By.CLASS_NAME, 'np-button')
    phone_field = (By.ID, 'phone')
    phone_confirm_button = (By.CSS_SELECTOR, 'button.button.full')
    sms_code_field = (By.ID, 'code')
    sms_confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    payment_method_button = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_option = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, 'input#code.card-input')
    card_add_button = (By.XPATH, '//button[text()="Agregar"]')
    card_added_confirmation = (By.XPATH, '//div[@class="pp-title" and text()="Tarjeta"]')
    message_field = (By.ID, 'comment')
    blanket_option = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/following-sibling::div//input')
    ice_cream_plus_button = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[@class="counter-plus"]')
    ice_cream_value = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[@class="counter-value"]')
    final_order_button = (By.CSS_SELECTOR, 'button.smart-button')
    search_taxi_modal = (By.CSS_SELECTOR, 'div.order')
    order_header = (By.CSS_SELECTOR, '.order-header')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_icon))

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_icon_assert))

    def click_phone_button(self):
        self.wait.until(EC.element_to_be_clickable(self.phone_button)).click()

    def set_phone_number(self, phone_number):
        self.wait.until(EC.visibility_of_element_located(self.phone_field)).send_keys(phone_number)

    def click_phone_confirm_button(self):
        self.wait.until(EC.element_to_be_clickable(self.phone_confirm_button)).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_field).get_property('value')

    def set_sms_code(self, code):
        self.wait.until(EC.visibility_of_element_located(self.sms_code_field)).send_keys(code)

    def click_sms_confirm_button(self):
        self.wait.until(EC.element_to_be_clickable(self.sms_confirm_button)).click()

    def click_payment_method_button(self):
        self.wait.until(EC.element_to_be_clickable(self.payment_method_button)).click()

    def click_add_card_option(self):
        self.wait.until(EC.element_to_be_clickable(self.add_card_option)).click()

    def set_card_number(self, card_number):
        card_input = self.wait.until(EC.element_to_be_clickable(self.card_number_field))
        card_input.click()
        card_input.send_keys(card_number)

    def set_card_code(self, card_code):
        card_input = self.wait.until(EC.element_to_be_clickable(self.card_code_field))
        card_input.send_keys(str(card_code))
        card_input.send_keys(Keys.TAB)

    def click_card_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.card_add_button)).click()

    def get_card_added_confirmation(self):
        return self.wait.until(EC.visibility_of_element_located(self.card_added_confirmation)).text

    def set_message(self, message):
        self.wait.until(EC.visibility_of_element_located(self.message_field)).send_keys(message)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def is_blanket_selected(self):
        checkbox = self.driver.find_element(*self.blanket_option)
        return checkbox.is_selected()

    def click_blanket_button(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.blanket_option))
        self.driver.execute_script("arguments[0].click();", checkbox)

    def click_ice_cream_plus(self):
        self.wait.until(EC.element_to_be_clickable(self.ice_cream_plus_button)).click()

    def order_ice_creams(self, quantity=2):
        for _ in range(quantity):
            self.click_ice_cream_plus()

    def get_ice_cream_count(self):
        return self.wait.until(EC.visibility_of_element_located(self.ice_cream_value)).text

    def click_final_order_button(self):
        button = self.wait.until(EC.presence_of_element_located(self.final_order_button))
        self.driver.execute_script("arguments[0].click();", button)

    def wait_for_search_taxi_modal(self):
        return self.wait.until(EC.visibility_of_element_located(self.search_taxi_modal)).text

    def get_order_header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.order_header)).text