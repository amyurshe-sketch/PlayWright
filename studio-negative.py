from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

# ===== ТЕСТ 2: Негативный — неверный пароль =====
    print("Тест 2: Проверка неверного пароля...")
    
    page.goto("https://studio-nn.online/login")
    page.fill("input[placeholder='Введите ваше имя']", "Alex")
    page.fill("input[placeholder='Введите пароль']", "неверный_пароль")
    page.click("button[type='submit']")
    page.wait_for_timeout(2000)
    
    error = page.locator("text=Неверные учетные данные")
    assert error.is_visible(), "Сообщение об ошибке не появилось!"
    print("✓ Тест 2 пройден — ошибка отображается корректно!")
    page.screenshot(path="test2_error.png")

    # ===== ТЕСТ 1: Позитивный — успешный вход =====
    print("Тест 1: Проверка успешной авторизации...")
    
    page.goto("https://studio-nn.online")
    page.click("a[href='/login']")
    page.wait_for_url("**/login")
    page.fill("input[placeholder='Введите ваше имя']", "Alex")
    page.fill("input[placeholder='Введите пароль']", "88ffd82s")
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
    
    assert page.url != "https://studio-nn.online/login", "Логин не прошёл!"
    print("✓ Тест 1 пройден — авторизация успешна!")
    page.screenshot(path="test1_success.png")

    

    print("\n Все тесты пройдены успешно!")
    
    input("Нажми Enter чтобы закрыть...")
    browser.close()