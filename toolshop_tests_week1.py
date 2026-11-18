import re
from playwright.sync_api import expect, sync_playwright

BASE_URL = "https://practicesoftwaretesting.com"
TOOLS_CATEGORY = "Power Tools"

# Assignment1: Test1 - Browse Category
def test_browse_category(page):
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=60000)
    expect(page).to_have_title(re.compile("Practice Software Testing"))
    page.click("text=Categories")
    #page.click("text=Hand Tools")
    page.click(f"text={TOOLS_CATEGORY}")

    # Verify that the page title contains the correct category name 
    #expect(page.locator("[data-test='page-title']")).to_contain_text("Category: Hand Tools")
    expect(page.locator("[data-test='page-title']")).to_contain_text(f"Category: {TOOLS_CATEGORY}")
    print("Success: Page title contains the correct category name")

    # Verify that at least one product exists
    expect(page.locator(".container .card").first).to_be_visible()
    print("Success: At least one product is visible")

    # Verify that each product card has a name
    for each in page.locator(".container .card").all():
        expect(each.locator(".card-title")).to_be_visible()
        assert each.locator(".card-title").inner_text().strip() != ""
        print("Success: Product card has a name")

# Assignment1: Test2 - Product Details
def test_product_details(page):
    # Click on the first product card
    first_product_name = page.locator(".container .card").first.locator(".card-title").text_content()
    print("First Product Name: ", first_product_name)
    page.locator(".container .card").first.click()

    # Verify that the product detail page contains the correct product name
    expect(page.locator("[data-test='product-name']")).to_contain_text(first_product_name)
    print("Success: Product detail page contains the correct product name")

    # Verify price is shown
    expect(page.locator("[data-test='unit-price']")).to_be_visible()
    print("Success: Product price is visible")

    # Verify that the "Add to Cart" button is visible
    expect(page.locator("text=Add to Cart")).to_be_visible()
    print("Success: Add to Cart button is visible")



def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Test 1
        print("Test 1: Browse Category")
        test_browse_category(page)
        # Test 2 
        print("Test 2: First Hand-Tool Detail Page")
        test_product_details(page)
        # Test 3
        print("Test 3: Add to Cart")
        test_add_to_cart(page)
        input("Test passed. Press Enter in this terminal to close the browser...")
        browser.close()


if __name__ == "__main__":
    main()