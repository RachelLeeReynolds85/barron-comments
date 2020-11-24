# Dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

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

def get_search_results():
    with open ("html_dump.html", "r", encoding="utf-8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "lxml")
            # print(soup.prettify())

    search_results = soup.find_all("a", class_="videomodal")

    search_results_html = str(search_results)

    with open("search_results.html", "w+", encoding="utf-8") as f:
        f.write(search_results_html)
    
    return search_results_html


url = 'https://factba.se/search#barron%2Bpositive'
html = get_html(url, wait=5)


with open('html_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html)








# soup = BeautifulSoup(html_string, "html.parser")

# print(soup.prettify())

# print(soup.head.prettify())

# print(soup.head.title.text.strip())

# print(soup.title.text)

# print(soup.p.text)

# p_tags = soup.find_all("p")

# for p_tag in p_tags:
#     print(p_tag.text)

# print(type(soup.head))

# print([p.text.strip() for p in soup.find(id="div-3").find_all("p")])

# print([p.text.strip() for p in soup.find(class_="class-1").find_all("p")])