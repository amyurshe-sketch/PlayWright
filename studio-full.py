from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Открываем сайт
    page.goto("https://studio-nn.online")
    
    # Нажимаем кнопку ВОЙТИ
    page.click("a[href='/login']")
    
    # Ждём загрузки страницы логина
    page.wait_for_url("**/login")
    
    # Заполняем поля
    page.fill("input[placeholder='Введите ваше имя']", "Alex")
    page.fill("input[placeholder='Введите пароль']", "88ffd82s")
    
    # Нажимаем кнопку Войти
    page.click("button[type='submit']")
    
    # Ждём результата
    page.wait_for_load_state("networkidle")
    
    # Ждём результата
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)  # подождать 2 секунды
    
    # Проверить что вошли успешно (например по URL или элементу на странице)
    assert page.url != "https://studio-nn.online/login", "Логин не прошёл!"
    print("Авторизация успешна!")

    # ===== ПРОВЕРКА ЗАГРУЗКИ НОВОСТЕЙ =====
    print("Проверка загрузки RSS новостей...")

    # Ждём появления новостей
    page.wait_for_selector(".news-content-item", timeout=5000)

    # Считаем количество новостей
    news_count = page.locator(".news-content-item").count()
    assert news_count > 0, "Новости не загрузились!"
    print(f"✓ Новости загружены — найдено {news_count} статей!")
    page.screenshot(path="test_news.png")
    
    # Ждём результата
    page.wait_for_timeout(2000)  # подождать 2 секунды
    
    # Переключаемся на английский
    page.click("button[title='Switch to English']")
    page.wait_for_timeout(1000)
    print("✓ Язык переключён на English!")
    page.screenshot(path="test_lang.png") 

    # Считаем количество новостей
    news_count = page.locator(".news-content-item").count()
    assert news_count > 0, "Новости не загрузились!"
    print(f"✓ Новости загружены — найдено {news_count} статей!")
    page.screenshot(path="test_news.png")  

    # Нажать на кнопку Users
    page.click("a[href='/users']")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)
    print("✓ Перешли на страницу Users!")
    
    # Нажать кнопку "написать" у пользователя Lazy
    page.locator("li:has-text('Lazy') button:has-text('написать')").click()
    page.wait_for_timeout(1000)
    print("✓ Нажали написать у Lazy!")

    # Заполняем сообщение
    page.fill("textarea[placeholder='Write your message…']", "Check")
    print("✓ Написал сообщение Send")

    # Отправляем сообщение
    page.click("button:has-text('Send')")

    # Выходим из аккаунта
    page.click("button.logout-desktop")
    print('Выход из аккаунта!')
    ##########################

    # Входим в аккаунт Lazy
    # Нажимаем кнопку ВОЙТИ
    page.click("a[href='/login']")
    
    # Ждём загрузки страницы логина
    page.wait_for_url("**/login")
    
    # Заполняем поля
    page.fill("input[placeholder='Enter your name']", "Lazy")
    page.fill("input[placeholder='Enter your password']", "ff88ds")
    print('Вход в Lazy!')

    # Вход
    page.click("button:has-text('Log in')")

    # Открытие окна сообщений
    page.click("button[title='New messages']")
    print('Проверка сообщений от Alex!')

    # Скриншот
    page.screenshot(path="result.png")
    
    input("Нажми Enter чтобы закрыть...")
    browser.close()
