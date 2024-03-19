from locators import MainPageLocators
from linksst import LinksStorage


class TestConstructorPage:
    def test_transition_to_bun_success(self, driver):
        """Проверка перехода к разделу 'Булки' """
        driver.get(LinksStorage.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()
        class_bun_ul = driver.find_element(*MainPageLocators.bun_ul).get_attribute('class')
        assert 'tab_tab_type' in class_bun_ul

    def test_transition_to_sauces_success(self, driver):
        """Проверка перехода к разделу 'Соусы' """
        driver.get(LinksStorage.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        class_sauces_ul = driver.find_element(*MainPageLocators.sauces_ul).get_attribute('class')
        assert 'tab_tab_type' in class_sauces_ul

    def test_transition_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки' """
        driver.get(LinksStorage.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        class_topping_ul = driver.find_element(*MainPageLocators.topping_ul).get_attribute('class')
        assert 'tab_tab_type' in class_topping_ul
