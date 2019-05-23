from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import re
import sys
import os

<<<<<<< HEAD
=======
# first thing first. We have to create product, just to make sure there is atleast 1 product available
# to assign endpoints to when creating or editing any.
# importing Product_selenium_unittest as a module
# This style is for python2 alone
import imp
product_unit_test = imp.load_source('product_selenium_unittest',
    os.path.join(os.environ['DD_ROOT'], 'tests', 'product_selenium_unittest.py'))

>>>>>>> 773b97d15f37bd3b5a6f90f2547379ff2c1322ab

class EndpointTest(unittest.TestCase):
    def setUp(self):
        # Initialize the driver
        # When used with Travis, chromdriver is stored in the same
        # directory as the unit tests
        self.driver = webdriver.Chrome('chromedriver')
        # Allow a little time for the driver to initialize
        self.driver.implicitly_wait(30)
        # Set the base address of the dojo
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login_page(self):
        # Make a member reference to the driver
        driver = self.driver
        # Navigate to the login page
        driver.get(self.base_url + "login")
        # Good practice to clear the entry before typing
        driver.find_element_by_id("id_username").clear()
        # These credentials will be used by Travis when testing new PRs
        # They will not work when testing on your own build
        # Be sure to change them before submitting a PR
        driver.find_element_by_id("id_username").send_keys(os.environ['DD_ADMIN_USER'])
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(os.environ['DD_ADMIN_PASSWORD'])
        # "Click" the but the login button
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        return driver

    def test_create_endpoint(self):
        # Login to the site.
        # Username and password will be gotten from environ
        driver = self.login_page()
        # Navigate to the Endpoint page
        driver.get(self.base_url + "endpoint")
        # "Click" the dropdown button to see options
        driver.find_element_by_id("dropdownMenu1").click()
        # "Click" the New Endpoint
        driver.find_element_by_link_text("New Endpoint").click()
        # Keep a good practice of clearing field before entering value
        # Endpoints
        driver.find_element_by_id("id_endpoint").clear()
        driver.find_element_by_id("id_endpoint").send_keys("123.22.43.101\nmoving.com.rnd\nhttps://gorand.in/publish")
        # Select product to assign endpoint to
        Select(driver.find_element_by_id("id_product")).select_by_visible_text("QA Test")
        # submit
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # Query the site to determine if the finding has been added
        productTxt = driver.find_element_by_tag_name("BODY").text
        # Assert ot the query to dtermine status of failure
        self.assertTrue(re.search(r'Endpoint added successfully', productTxt))

    def test_edit_endpoint(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.login_page()
        # Navigate to the endpoint page
        driver.get(self.base_url + "endpoint")
        # Select one of the previously created endpoint to edit
        driver.find_element_by_link_text("moving.com.rnd").click()
        # "Click" the dropdown button to see options
        driver.find_element_by_id("dropdownMenu1").click()
        # "Click" the Edit Endpoint
        driver.find_element_by_link_text("Edit Endpoint").click()
        # Clear the old endpoint host name
        driver.find_element_by_id("id_host").clear()
        # Fill in the endpoint host name
        driver.find_element_by_id("id_host").send_keys("https://moving.com/")
        # Fill in port for endpoint
        driver.find_element_by_id("id_port").clear()
        driver.find_element_by_id("id_port").send_keys("8080")
        # "Click" the submit button to complete the transaction
        driver.find_element_by_css_selector("input.btn.btn-primary").click()
        # Query the site to determine if the product has been added
        productTxt = driver.find_element_by_tag_name("BODY").text
        # Assert ot the query to dtermine status of failure
        self.assertTrue(re.search(r'Endpoint updated successfully', productTxt))

    def test_delete_endpoint(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.login_page()
        # Navigate to the endpoint page
        driver.get(self.base_url + "endpoint")
        # Select one of the previously created endpoint to delete
        driver.find_element_by_link_text("123.22.43.101").click()
        # "Click" the dropdown button to see options
        driver.find_element_by_id("dropdownMenu1").click()
        # "Click" the Delete Endpoint
        driver.find_element_by_link_text("Delete Endpoint").click()
        # "Click" the delete button to complete the transaction
        driver.find_element_by_css_selector("button.btn.btn-danger").click()
        # Query the site to determine if the product has been added
        productTxt = driver.find_element_by_tag_name("BODY").text
        # Assert ot the query to dtermine status of failure
        self.assertTrue(re.search(r'Endpoint and relationships removed.', productTxt))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def suite():
    suite = unittest.TestSuite()
    # Add each test the the suite to be run
    # success and failure is output by the test
<<<<<<< HEAD
    suite.addTest(EndpointTest('test_create_product'))
=======
    suite.addTest(product_unit_test.ProductTest('test_create_product'))
>>>>>>> 773b97d15f37bd3b5a6f90f2547379ff2c1322ab
    suite.addTest(EndpointTest('test_create_endpoint'))
    suite.addTest(EndpointTest('test_edit_endpoint'))
    suite.addTest(EndpointTest('test_delete_endpoint'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(descriptions=True, failfast=True)
    ret = not runner.run(suite()).wasSuccessful()
    sys.exit(ret)
