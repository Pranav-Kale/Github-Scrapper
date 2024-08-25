import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
scrape = input("Enter the page would you like to scrape : ")

driver.get(f"{scrape}")
res = driver.find_elements(By.CLASS_NAME, "repo")

links = []
final_link = []
def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME,"cpVEZe")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html :
        print(f"Found Password at {second_page}")

def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "react-directory-row")
    
    file_types = ["py", "txt", "md", "html", "css", "js", "json", "csv", "xml"]

    for a in res2:
        for file_type in file_types:
            if file_type in a.text:
                second_page = f"{next_page}/blob/main/{a.text}"
                going_for_raw(second_page)
                break
        else:
            print(f"File type not recognized: {a.text}")


for i in res :
    links.append(i.text)
# print(links)

for link in links :
    next_page = f"{scrape}/{link}"
    final_link.append(next_page)
    loop(next_page)
# print(final_link)



driver.quit()
