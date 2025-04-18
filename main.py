import os
from playwright.sync_api import sync_playwright
import time
import datetime

def is_time_in_range(start_hour, end_hour):
    now = datetime.datetime.now().time()
    return now >= datetime.time(start_hour) or now <= datetime.time(end_hour)

def run_bot():
    if not is_time_in_range(22, 6):  # من 10 مساءً إلى 6 صباحًا
        print("ليس الوقت المناسب لتشغيل البوت.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://kick.com/login')
        page.fill('input[name="username"]', os.environ['KICK_USERNAME'])
        page.fill('input[name="password"]', os.environ['KICK_PASSWORD'])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        page.goto('https://kick.com/nourgamer')
        print("البوت يشاهد البث الآن...")
        while is_time_in_range(22, 6):
            time.sleep(300)
        print("انتهى وقت البث.")
        browser.close()

run_bot()
