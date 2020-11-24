from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Use selenium to grab html on site (after waiting for site to fully load)
def get_html(url, wait):
    print("\nStarting headless Firefox driver!")
    print(f"Navigating to {url}")
    print(f"Waiting {wait} seconds...\n")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()
    return html

url = 'https://factba.se/search#barron%2Bpositive'
html = get_html(url, wait=5)

print(html)

with open('html_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html)