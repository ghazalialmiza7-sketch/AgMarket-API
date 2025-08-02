from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "🚜 AgMarket API is up! Use /scrape to fetch data."

@app.route("/scrape")
def scrape_popup():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://agmarknet.gov.in/")

    # Wait and interact with popup
    time.sleep(5)
    driver.switch_to.frame("cframe")
    popup_data = driver.find_element(By.ID, "PopUpText").text

    driver.quit()
    return jsonify({"popup_data": popup_data})
