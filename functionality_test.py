from selenium import webdriver
import unittest
import time

class EmployeeVisitor(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()

	def test_can_visit_cv_page(self):
		self.browser.get('http://127.0.0.1:8000')
		#An employer wishes to view the CV
		#On the blog homepage they see a link in the header which says CV
		header_text = header_text = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('CV', header_text)
		#They click on the link and are re-directed to the CV page
		link = self.browser.find_element_by_link_text('CV')
		link.click()
		time.sleep(1)
		#The page title is CV
		self.assertIn('CV', self.browser.title)
		self.fail("Finish this Test!")


#At the top of the page is Callum August as a title and Curriculum vitae as a subtitle
#Below that there is an address, email and phone number.
#They see 5 sections titled: "Personal Statement", "Education", "Tech Skills", "Work Experience" and "Interests"
#Within each section they see the information
#The employer is done looking at the CV and clicks a link "Blog" in order to go back to the blog.

if __name__ == '__main__':
	unittest.main(warnings='ignore')
