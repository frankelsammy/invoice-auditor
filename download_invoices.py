import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError

import customer_id_map


load_dotenv()
WM_USER = os.getenv("WM_USER")
WM_PASSWORD = os.getenv("WM_PASSWORD")

cust_id_map = customer_id_map.make_map()

def download_invoices():
    #create a directory for invoices
    os.makedirs("invoices", exist_ok=True)

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.bring_to_front()  # Bring the browser window to the front

        # Go to login page
        page.goto(
            "https://www.wm.com/us/en/user/login?redirect=/us/en/mywm/user/my-payment/billing/overview"
        )

        # Fill email and password
        page.wait_for_selector("#EmailInput")
        page.fill("#EmailInput", os.getenv("WM_USER"))

        page.wait_for_selector("#PasswordInput")
        page.fill("#PasswordInput", os.getenv("WM_PASSWORD"))

        # Click login button
        page.click("button[data-testid='LoginWidget-login-button']")
        list_container = page.locator('div[data-testid="WindowedList"]')

        try:
            list_container.wait_for(state="visible", timeout=30_000)
            print("WindowedList container found and visible")
        except TimeoutError:
            print("WindowedList container NOT found after 30 seconds")

        def find_customer_button(customerID):
            # Scroll to top
            list_container.evaluate("(el) => el.scrollTop = 0")
            page.wait_for_timeout(1000)

            scroll_attempts = 0
            while scroll_attempts < 10:  # Allow more attempts to find the button
                button = list_container.locator("button", has_text=customerID)
                if button.count() > 0:
                    return button.first

                # Scroll down
                bbox = list_container.bounding_box()
                if bbox:
                    page.mouse.move(
                        bbox["x"] + bbox["width"] / 2, bbox["y"] + bbox["height"] / 2
                    )
                page.mouse.wheel(0, 400)
                page.wait_for_timeout(1000)
                scroll_attempts += 1

        i = 0
        for customer_id in cust_id_map.keys():
            i += 1
            current_customer = customer_id
            customer_name = cust_id_map[current_customer]
            print(f"Processing customer {i} of {len(cust_id_map)}: {customer_name}")
            customer_button = find_customer_button(current_customer)
            if customer_button is None:
                print(f"Customer button for {current_customer} not found, skipping.")
                continue
            page.click(f'button:has-text("{current_customer}")')

            # Wait for invoice link to appear and click it
            invoice_link = page.locator('button[analytics="02/16/2026"]').first
            
            if invoice_link.count() > 0:
                with page.expect_download() as download_info:
                    invoice_link.click()
                download = download_info.value
                download.save_as(f"invoices/{customer_name}.pdf")

            page.goto(
                "https://www.wm.com/us/en/user/login?redirect=/us/en/mywm/user/my-payment/billing/overview"
            )


if __name__ == "__main__":
    download_invoices()
