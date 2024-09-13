from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40) #Preguntar anely

    # Localizadores de la página de rutas urbanas
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    REQUEST_TAXI_BUTTON = (By.CLASS_NAME, 'button.round')
    COMFORT_OPTION = (By.CLASS_NAME, 'tcard-icon')  # Opción Comfort
    PHONE_CLICK = (By.CLASS_NAME, 'np-text')
    PHONE_FIELD = (By.ID, 'phone')
    NEXT_BUTTON = (By.CLASS_NAME, 'button.full')
    CODE_INPUT_FIELD = (By.XPATH, '//*[@id="code"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-button.filled')
    ADD_CARD_BUTTON = (By.CLASS_NAME, 'pp-title')
    CARD_NUMBER_FIELD = (By.ID, 'number')
    CARD_CODE_FIELD = (By.ID, 'code')
    ADD_BUTTON = (By.CLASS_NAME, 'button.full')
    CLOSE_CARD_MODAL_BUTTON = (By.CLASS_NAME, 'close-button.section-close')
    DRIVER_MESSAGE_FIELD = (By.CLASS_NAME, 'label')
    BLANKET_AND_TISSUES_CHECKBOX = (By.CLASS_NAME, 'slider.round')
    ICE_CREAM_COUNTER_PLUS = (By.CLASS_NAME, 'counter-plus')
    REQUEST_TAXI_BUTTON_SMART = (By.CLASS_NAME, 'smart-button')
    CARD_NUMBER_TEXT = (By.CLASS_NAME, 'pp-value-text')  # Elemento para validar el número de tarjeta

    # Métodos de interacción con los elementos
    def set_from(self, from_address):
        """Rellena el campo 'Desde'."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        ).send_keys(from_address)

    def is_from_field_filled(self, from_address):
        """Verifica si el campo 'Desde' está lleno."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.FROM_FIELD)
        ).get_attribute('value') == from_address

    def set_to(self, to_address):
        """Rellena el campo 'Hasta'."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.TO_FIELD)
        ).send_keys(to_address)

    def is_to_field_filled(self, to_address):
        """Verifica si el campo 'Hasta' está lleno."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.TO_FIELD)
        ).get_attribute('value') == to_address

    def click_request_taxi(self):
        """Hace clic en el botón 'Pedir un taxi'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.REQUEST_TAXI_BUTTON)
        ).click()

    def is_request_taxi_button_displayed(self):
        """Verifica si el botón 'Pedir un taxi' está visible."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.REQUEST_TAXI_BUTTON)
        ).is_displayed()

    def select_comfort_option(self):
        """Selecciona la opción 'Comfort'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.COMFORT_OPTION)
        ).click()

    def is_comfort_option_selected(self):
        """Verifica si la opción 'Comfort' está seleccionada."""
        return 'selected' in WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.COMFORT_OPTION)
        ).get_attribute('class')

    def click_phone_field(self):
        """Hace clic en el campo de número de teléfono."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.PHONE_CLICK)
        ).click()

    def set_phone_number(self, phone_number):
        """Rellena el campo de número de teléfono."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.PHONE_FIELD)
        ).send_keys(phone_number)

    def is_phone_number_filled(self, phone_number):
        """Verifica si el número de teléfono está lleno y visible en el campo correspondiente."""
        phone_field = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.PHONE_FIELD)
        )
        #Modificado segun comentarios del revisor
        return phone_field.get_attribute('value') == phone_number and phone_number in self.driver.find_element(By.CLASS_NAME, 'np-text').text

    def click_next_button(self):
        """Hace clic en el botón 'Siguiente'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()

    def is_code_input_field_displayed(self):
        """Verifica si el campo de código de confirmación está visible."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CODE_INPUT_FIELD)
        ).is_displayed()

    def enter_confirmation_code(self, code):
        """Ingresa el código de confirmación."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CODE_INPUT_FIELD)
        ).send_keys(code)

    def is_confirmation_code_correct(self, code):
        """Verifica si el código de confirmación ingresado es correcto."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CODE_INPUT_FIELD)
        ).get_attribute('value') == code

    def click_confirm_button(self):
        """Hace clic en el botón 'Confirmar'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()

    def is_confirmation_successful(self):
        """Verifica si la confirmación fue exitosa."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CONFIRM_BUTTON)
        ).is_displayed()

    def click_payment_method(self):
        """Hace clic en el botón del método de pago."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)
        ).click()

    def is_payment_method_displayed(self):
        """Verifica si el método de pago está desplegado."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.PAYMENT_METHOD_BUTTON)
        ).is_displayed()

    def click_add_card(self):
        """Hace clic en el botón 'Agregar tarjeta'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.ADD_CARD_BUTTON)
        ).click()

    def is_add_card_form_displayed(self):
        """Verifica si el formulario para agregar una tarjeta está visible."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)
        ).is_displayed()

    def set_card_number(self, card_number):
        """Rellena el campo de número de tarjeta."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)
        ).send_keys(card_number)

    def is_card_number_filled(self, card_number):
        """Verifica si el número de tarjeta está lleno y visible en el campo correspondiente."""
        card_number_field = WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CARD_NUMBER_FIELD)
        )
        return card_number_field.get_attribute('value') == card_number and card_number in self.driver.find_element(By.CLASS_NAME, 'pp-value-text').text

    def set_card_code(self, card_code):
        """Rellena el campo de código de tarjeta."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CARD_CODE_FIELD)
        ).send_keys(card_code)

    def is_card_code_filled(self, card_code):
        """Verifica si el código de tarjeta está lleno."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CARD_CODE_FIELD)
        ).get_attribute('value') == card_code

    def click_add_button(self):
        """Hace clic en el botón 'Agregar'."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

    def is_payment_method_added(self):
        """Verifica si el método de pago ha sido agregado."""
        # Ajusta el método según cómo se indica que el método de pago fue agregado en tu aplicación
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.ADD_BUTTON)
        ).is_displayed()

    def close_card_modal(self):
        """Hace clic en el botón de cerrar modal de tarjeta."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.CLOSE_CARD_MODAL_BUTTON)
        ).click()

    def is_card_modal_open(self):
        """Verifica si el modal de tarjeta está abierto."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.CLOSE_CARD_MODAL_BUTTON)
        ).is_displayed()

    def set_driver_message(self, message):
        """Rellena el mensaje para el conductor."""
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.DRIVER_MESSAGE_FIELD)
        ).send_keys(message)

    def is_driver_message_set(self, message):
        """Verifica si el mensaje para el conductor ha sido ingresado."""
        return WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.DRIVER_MESSAGE_FIELD)
        ).get_attribute('value') == message

    def select_blanket_and_tissues(self):
        """Selecciona manta y pañuelos."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.BLANKET_AND_TISSUES_CHECKBOX)
        ).click()

    def is_blanket_and_tissues_selected(self):
        """Verifica si la manta y los pañuelos están seleccionados."""
        return 'selected' in WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.BLANKET_AND_TISSUES_CHECKBOX)
        ).get_attribute('class')

    def request_two_ice_creams(self):
        """Solicita dos helados."""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.ICE_CREAM_COUNTER_PLUS)
        ).click()
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.ICE_CREAM_COUNTER_PLUS)
        ).click()

    def click_request_taxi_smart(self):
        """Pedir un taxi"""
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(self.REQUEST_TAXI_BUTTON_SMART)
        ).click()
