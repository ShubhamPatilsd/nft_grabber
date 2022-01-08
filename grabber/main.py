from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import subprocess
import uuid

driver_path = "./chromedriver"
brave_path = "/usr/bin/brave"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--headless")

browser = webdriver.Chrome(executable_path=driver_path, options=option)

browser.get("https://opensea.io/collection/boredapeyachtclub")
time.sleep(2)

# last_position = 0
# last_nft = 1

# for i in range(5):
#     browser.execute_script(
#         f"window.scrollTo({last_position},{last_position+500})")
#     last_position += 500
#     time.sleep(5)
#     # /html/body/div[1]/div[1]/main/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div/div[SSS]/div/article/a/div[1]/div/div/div/img
#     for item in range(last_nft, last_nft+3):
#         image = browser.find_element_by_xpath(
#             f"/html/body/div[1]/div[1]/main/div/div/div[3]/div/div/div/div[3]/div[3]/div[2]/div/div/div[{item}]/div/article/a/div[1]/div/div/div/img"
#         )
#         x = image.get_attribute("src")
#         print(x)
#     last_nft += 3

# x = browser.find_elements_by_class_name("Image--image")
# for nft in x:
#     print(x.get_attribute("src"))

urls = set()
# ids = set()
extra = []

last_pos = 0
seconds = 5
images_count = 0
t_end = time.time() + seconds
while time.time() < t_end:
    browser.execute_script(
        f"window.scrollTo({last_pos},{last_pos+500})")
    time.sleep(1)
    last_pos += 500
    images = browser.find_elements(By.CLASS_NAME, "Image--image")
    for element in images:
        src = element.get_attribute("src")
        print(src, images_count)
        if(src):
            images_count += 1
        if(src and images_count >= 2):
            urls.add(src.split("=")[0])
        if(src and images_count <= 2):
            extra.append(src.split("=")[0])

# print(extra, urls)
for src in range(len(urls)):
    if(list(urls)[src] != extra[0] and list(urls)[src] != extra[1]):
        subprocess.run(["wget", list(urls)[src], "-O",
                        f"../nfts/{uuid.uuid1().hex}.png"])
