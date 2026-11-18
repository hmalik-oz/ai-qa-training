# AI QA Training

Hands-on test automation training exercises using Python and [Playwright](https://playwright.dev/python/).

The tests target the [Toolshop demo application](https://practicesoftwaretesting.com) (Practice Software Testing) and cover common e-commerce user flows.

## Contents

- `toolshop_tests_week1.py` — Week 1 assignment with three UI tests:
  1. **Browse Category** — navigate to a product category and verify the page title and product listings.
  2. **Product Details** — open the first product and verify its name, price, and "Add to Cart" button.
  3. **Add to Cart** — add a product to the cart and verify the cart count, product name, quantity, and price.

## Running the tests

```bash
pip install playwright
playwright install chromium
python toolshop_tests_week1.py
```

The script launches a visible Chromium browser, runs the three tests in sequence, and waits for Enter before closing.
