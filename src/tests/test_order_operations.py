from src.common import base_test
from src.page_object import order_page
from src.page_object import menu_page
from src.page_object import product_details_page
from src.common.base_test import setup_module
from src.common.base_test import teardown_module


class Test_Order:
    def test_order_process(self):
        order_page.navigate_to_order()
        order_page.search_address(base_test.configs.get('search_order_address').data)
        order_page.click_delivery_for_store(base_test.configs.get('delivery_store').data)
        order_page.click_continue_confirm_address_popup()
        order_page.select_delivery_time_and_continue()
        menu_page.wait_for_menu_page_to_load()
        assert base_test.get_driver().current_url == base_test.configs.get('Url').data + '/order/catalog'
        menu_page.click_item(base_test.configs.get('item').data)
        product_details_page.verify_description_should_be_present(base_test.configs.get('item_description').data)
