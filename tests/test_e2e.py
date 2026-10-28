from playwright.sync_api import sync_playwright
import threading
import uvicorn
from main import app
import time

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def test_e2e_browser():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000")
        
        assert "FastAPI Calculator" in page.title()
        heading = page.locator("h1").inner_text()
        assert heading == "FastAPI Calculator App"
        
        browser.close()