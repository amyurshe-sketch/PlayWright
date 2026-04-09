from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://zdes-vkusno.ru/")
    page.wait_for_load_state("networkidle")
    
    # Кликаем на Пицца
    page.get_by_role("link", name="Пицца").click()
    page.wait_for_load_state("networkidle")
    
    # Смотрим что там есть
    print("=== Ищем элементы для выбора селектора ===")
    print(f"Элементы с [class*='product']: {page.locator('[class*=\"product\"]').count()}")
    print(f"Элементы с .item: {page.locator('.item').count()}")
    print(f"Элементы <h3>: {page.locator('h3').count()}")
    print(f"Элементы с [class*='price']: {page.locator('[class*=\"price\"]').count()}")
    print(f"Элементы img: {page.locator('img').count()}")
    print(f"Элементы div с data-item: {page.locator('div[data-item]').count()}")
    print(f"Элементы с класс 'menu-item': {page.locator('.menu-item').count()}")
    
    browser.close()
    print("\n✓ Проверка завершена")
