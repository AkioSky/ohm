
from app_main import app
from tests import OhmTestCase
from selenium.webdriver import Chrome, ChromeOptions
from app_main import app, config
import time


class CommunityTest(OhmTestCase):
    def __init__(self, *args, **kwargs):
        super(CommunityTest, self).__init__(*args, **kwargs)
        chrome_info = config()['chrome-path']
        options = ChromeOptions()
        options.add_argument('--headless')
        self.driver = Chrome(executable_path=chrome_info['executable_path'],
            options=options)

    def setUp(self):
        super(CommunityTest, self).setUp()

    def test_get(self):
        # with app.test_client() as c:
        response = self.client.get('/community')
        self.assert200(response)
        # Should show correct template
        self.assertIn("This is teh users list you want to see.", response.data)
        
        # Should show user email and point balance
        self.assertIn(self.chuck.email_address, response.data)
        self.assertIn(str(self.chuck.point_balance), response.data)

    def test_behaviors(self):
        self.driver.get('http://localhost:6543/community')
        # Less than 5 records only should be rendered.
        records = self.driver.find_elements_by_css_selector('tr.user-with-phone')
        self.assertLessEqual(len(records), 5, "Table limit is 5. But more than records were rendered.")

        # Check if modal does work?
        record = records[1]
        name = record.find_element_by_css_selector('span.user-display_name')
        name.click()
        time.sleep(1)
        modal_selector = name.get_attribute('data-target')
        modal = self.driver.find_element_by_css_selector(modal_selector)
        self.assertTrue(modal.is_displayed(), "Modal doesn't work for the clickable name.")

        # Check if the location is correct.
        location = modal.find_element_by_css_selector('.user-location')
        self.assertEqual(location.text.lower(), 'usa', "User's location mismatch!")

        # Community link should be added below the dashboard link
        menu_toggle_button = self.driver.find_element_by_id('header-name')
        self.driver.execute_script("arguments[0].click();", menu_toggle_button)
        time.sleep(0.1)
        top_right_links = self.driver.find_elements_by_css_selector('li.top-right-dropdown a')
        self.assertGreater(len(top_right_links), 1, "Only 1 top right navigation link found.")
        community_link = top_right_links[1]
        self.assertEqual(community_link.find_element_by_css_selector('.dropdown-menu-text').text.lower(), 'community')
        self.assertEqual(community_link.get_attribute('href'), 'http://localhost:6543/community')


    def tearDown(self):
        self.driver.quit()
