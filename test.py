import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe",chrome_options =chrome_options)

# https://cdn.shopify.com/s/files/1/0094/0716/8559/products/Untitled-1_0006_DSC02981_9487af4f-159a-4115-bd2b-82b296a6c8d6_600x.jpg?v=1654678270
# https://lp2.hm.com/hmgoepprod?set=source[/39/41/3941d20cfa98d43c11ffec84a324b73266ef3eed.jpg],origin[dam],category[],type[LOOKBOOK],res[z],hmver[1]&call=url[file:/product/main]
# http://static3.businessinsider.com/image/527ba0b06bb3f78972df1735-480-360/coat-1.jpg?maxX=480&maxY=360

#TEST_CASE_1(CHECKING UPDATE PROFILE OPTION)
# driver.get("http://localhost:5000/")
# driver.find_element("id","dropdown01").click()
# driver.find_element("id","click").click()
# s = driver.find_element("id","profile_image")
# s.send_keys(r"C:\abhinav.jpeg")
# driver.find_element("id","submit").click()

#TEST_CASE_2(CHHCEKING WHOLE WEBSITE)
# driver.get("http://localhost:5000/")
# driver.find_element("id","keshav").click()
# s = driver.find_element("id","profile_image")
# s.send_keys(r"C:\abhinav.jpeg")
# driver.find_element("id","submit").click()
# s = driver.find_element("id","source_image_url")
# s.send_keys("https://cdn.shopify.com/s/files/1/0094/0716/8559/products/Untitled-1_0006_DSC02981_9487af4f-159a-4115-bd2b-82b296a6c8d6_600x.jpg?v=1654678270")
# driver.find_element("id","submit").click()
# time.sleep(30)
# driver.find_element("id","view").click()

# TEST_CASE_3 (CHECKING BACK BUTTON)
# driver.get("http://localhost:5000/")
# driver.find_element("id","dropdown01").click()
# driver.find_element("id","click").click()
# driver.find_element("id","back").click()

# TESTCASE4(CHECK TRYNEXT BUTTON)
# driver.get("http://localhost:5000/tryon")
# driver.find_element("id","trynext").click()