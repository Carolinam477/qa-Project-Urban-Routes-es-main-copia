import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage  # Importamos la clase que contiene las interacciones
from Helpers import retrieve_phone_code  # Importamos la función auxiliar que obtiene el código de confirmación

class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        """Configuración inicial de la clase de prueba."""
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)  # Accede a la URL de las rutas urbanas
        cls.routes_page = UrbanRoutesPage(cls.driver)  # Inicializa la página de rutas urbanas

    #aserciones validadas y modificadas.

    def test_set_from_field(self):
        """Paso 1: Rellenar el campo 'Desde'."""
        self.routes_page.set_from(data.address_from)
        assert self.routes_page.is_from_field_filled(data.address_from), "El campo 'Desde' no fue llenado correctamente."

    def test_set_to_field(self):
        """Paso 2: Rellenar el campo 'Hasta'."""
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.is_to_field_filled(data.address_to), "El campo 'Hasta' no fue llenado correctamente."

    def test_click_request_taxi(self):
        """Paso 3: Hacer clic en el botón 'Pedir un taxi'."""
        self.routes_page.click_request_taxi()
        assert self.routes_page.is_request_taxi_button_displayed(), "El botón 'Pedir un taxi' no está visible."

    def test_select_comfort_option(self):
        """Paso 4: Seleccionar la opción 'Comfort'."""
        # Modificado segun comentario del revisor
        self.routes_page.select_comfort_option()
        assert self.routes_page.is_comfort_option_selected(), "La opción 'Comfort' no fue seleccionada correctamente."

    def test_phone_field(self):
        """Paso 5 y 6: Rellenar el campo de número de teléfono y validar su ingreso."""
        # Modificado segun comentario del revisor
        self.routes_page.click_phone_field()
        self.routes_page.set_phone_number(data.phone_number)
        assert self.routes_page.is_phone_number_filled(data.phone_number), "El número de teléfono no fue ingresado correctamente."

    def test_click_next_button(self):
        """Paso 7: Clic en el botón 'Siguiente'."""
        self.routes_page.click_next_button()
        assert self.routes_page.is_code_input_field_displayed(), "El campo de código no se mostró después de hacer clic en 'Siguiente'."

    def test_enter_confirmation_code(self):
        """Paso 8: Introducir el código de confirmación."""
        confirmation_code = retrieve_phone_code(self.driver)
        self.routes_page.enter_confirmation_code(confirmation_code)
        assert self.routes_page.is_confirmation_code_correct(confirmation_code), "El código de confirmación no fue ingresado correctamente."

    def test_click_confirm_button(self):
        """Paso 9: Clic en el botón 'Confirmar'."""
        self.routes_page.click_confirm_button()
        assert self.routes_page.is_confirmation_successful(), "El código de confirmación no fue aceptado."

    def test_click_payment_method(self):
        """Paso 10: Clic en el método de pago."""
        self.routes_page.click_payment_method()
        assert self.routes_page.is_payment_method_displayed(), "El método de pago no se desplegó correctamente."

    def test_click_add_card(self):
        """Paso 11: Clic en el botón 'Agregar tarjeta'."""
        self.routes_page.click_add_card()
        assert self.routes_page.is_add_card_form_displayed(), "El formulario para agregar tarjeta no se mostró."

    def test_set_card_number(self):
        """Paso 12: Ingresar el número de tarjeta."""
        self.routes_page.set_card_number(data.card_number)
        # Modificado segun comentario del revisor 'pp-value-text'
        assert self.routes_page.is_card_number_displayed(data.card_number), "El número de tarjeta no fue ingresado correctamente."

    def test_set_card_code(self):
        """Paso 13: Ingresar el código de tarjeta."""
        self.routes_page.set_card_code(data.card_code)
        assert self.routes_page.is_card_code_filled(data.card_code), "El código de tarjeta no fue ingresado correctamente."

    def test_click_add_button(self):
        """Paso 14: Clic en el botón 'Agregar'."""
        self.routes_page.click_add_button()
        assert self.routes_page.is_payment_method_added(), "El método de pago no se agregó correctamente."

    def test_close_card_modal(self):
        """Paso 15: Cerrar el modal de tarjeta."""
        self.routes_page.close_card_modal()
        assert not self.routes_page.is_card_modal_open(), "El modal de tarjeta no se cerró correctamente."

    def test_set_driver_message(self):
        """Paso 16: Ingresar el mensaje para el conductor."""
        # Modificado segun comentario del revisor
        self.routes_page.set_driver_message(data.message_for_driver)
        assert self.routes_page.is_driver_message_set(data.message_for_driver), "El mensaje para el conductor no fue ingresado correctamente."

    def test_select_blanket_and_tissues(self):
        """Paso 17: Agregar manta y pañuelos."""
        # Modificado segun comentario del revisor
        self.routes_page.select_blanket_and_tissues()
        assert self.routes_page.is_blanket_and_tissues_selected(), "No se seleccionaron correctamente la manta y los pañuelos."

    def test_request_two_ice_creams(self):
        """Paso 18: Pedir dos helados."""
        # Modificado segun comentario del revisor
        self.routes_page.request_two_ice_creams()
        assert self.routes_page.is_ice_cream_requesteis_request_taxi_button_displayedd(), "Los helados no fueron solicitados correctamente."

    def test_click_request_taxi_smart(self):
        """Paso 19: Clic en el botón 'Pedir un taxi' con Smart."""
        # Modificado segun comentario del revisor
        self.routes_page.click_request_taxi_smart()
        assert self.routes_page.is_taxi_smart_requested(), "El taxi no fue pedido correctamente usando la opción Smart."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
