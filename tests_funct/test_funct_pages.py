import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')



class TestHomePage(StaticLiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()


    def test_verify_elements_in_home(self):
        self.driver.get(self.live_server_url)
        time.sleep(5)
        # user opens the page and sees header section
        logo = self.driver.find_element_by_id("logo")
        source = logo.get_attribute("src")
        self.assertEquals(
            source,
            self.live_server_url
            + '/static/dist/assets/img/logo/logo_pur_beurre.png',
        )
        title = self.driver.find_element_by_id("brand").text
        self.assertEquals(title, 'Pur beurre')
        title = self.driver.find_element_by_id("main-title").text
        self.assertEquals(title, 'DU GRAS, OUI, MAIS DE QUALITÉ!')

    def test_redirection_to_login(self):
        mentions_url = self.live_server_url + reverse("login")
        self.driver.get(self.live_server_url)
        time.sleep(5)
        self.driver.find_element_by_id("selections-login").click()
        self.assertEquals(self.driver.current_url, mentions_url)
        time.sleep(5)

    def test_redirection_to_mentions(self):
        mentions_url = self.live_server_url + reverse("pages-mentions")
        self.driver.get(self.live_server_url)
        time.sleep(5)
        self.driver.find_element_by_id("legal-link").click()
        self.assertEquals(self.driver.current_url, mentions_url)
        time.sleep(5)

