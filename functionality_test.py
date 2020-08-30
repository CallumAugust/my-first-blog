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
		header_text = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('CV', header_text)
		#They click on the link and are re-directed to the CV page
		link = self.browser.find_element_by_link_text('CV')
		link.click()
		time.sleep(1)
		self.assertIn('CV', self.browser.title)

	def test_cv_title(self):
		self.browser.get('http://127.0.0.1:8000/cv/')
		#The page title is CV
		self.assertIn('CV', self.browser.title)
		#At the top of the page is Callum August as a heading
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Callum August', header_text)
		#Curriculum vitae as a subtitle
		subtitle = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('Curriculum Vitae', subtitle)

	def test_contact_details(self):
		self.browser.get('http://127.0.0.1:8000/cv/')
		#Below that there is an address, email and phone number		
		address = self.browser.find_element_by_tag_name('address').text
		self.assertIn('24 Long Rd', address)
		self.assertIn('Cambridge', address)
		self.assertIn('Cambridgeshire', address)
		self.assertIn('UK', address)
		telephone = self.browser.find_element_by_class_name('phone').text
		self.assertIn("07459 264859", telephone)
		email = self.browser.find_element_by_class_name('email').text
		self.assertIn("callum@august-family.org.uk", email)
		

	def test_find_sections(self):
		self.browser.get('http://127.0.0.1:8000/cv/')
		#They see 5 sections titled: "Personal Statement", "Education", "Tech Skills", "Work Experience" and 			"Interests"
		#Within each section they see the information
		section_titles = self.browser.find_elements_by_tag_name('h3')
		self.assertTrue(len(section_titles)==5)
		self.assertIn('Personal Statement', section_titles[0].text)
		self.assertIn('Education', section_titles[1].text)
		self.assertIn('Tech Skills', section_titles[2].text)
		self.assertIn('Work Experience', section_titles[3].text)
		self.assertIn('Interests', section_titles[4].text)		

	#The employer is done looking at the CV and clicks a link "Back to Blog" in order to go back to the blog.
	def test_can_go_back_to_blog(self):
		self.browser.get('http://127.0.0.1:8000/cv/')
		link = self.browser.find_element_by_link_text('Back to Blog')
		link.click()
		time.sleep(1)
		self.assertIn("Callum's Blog", self.browser.title)

class EditorVisitor(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def tearDown(self):
		self.browser.quit()

	def test_edit_button(self):
		pass
	#The editor visits the cv page and sees the same view as the employer but with an edit button by the title
	#of each section.
	#The editor clicks on the edit button and it taken to a form
	#The form has the section title and a text box below with the current section contents in it.
	#The editor changes an item and then clicks a save button
	#The editor is taken back to the CV page with the new edited text

if __name__ == '__main__':
	unittest.main(warnings='ignore')
