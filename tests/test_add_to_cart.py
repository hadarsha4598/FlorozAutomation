from pages.home_page import HomePage


def test_floroz_add_to_cart(driver):
    home_page = HomePage(driver)

    # כניסה לאתר
    driver.get("www.floroz.co.il")

    # חיפוש והוספה לסל
    home_page.search_for_product("זר פרחים")
    home_page.add_first_product_to_cart()

    # אימות שהסל התעדכן (לפחות מוצר 1)
    count = home_page.get_cart_count()
    assert int(count) > 0, "הסל ריק למרות שהוספנו מוצר!"
    print(f"הבדיקה הצליחה! בסל יש {count} מוצרים.")
