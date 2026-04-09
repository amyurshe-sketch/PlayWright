import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)  # 2000ms = 2 секунды
    #browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    print("📍 Загрузка главной страницы...")
    page.goto("https://zdes-vkusno.ru/")
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не загружено!"
    print("✓ Главная страница загружена и меню видимо")
    
    print("📍 Переход на Пицца...")
    page.get_by_role("link", name="Пицца").click()
    page.wait_for_load_state("networkidle")
    # Проверяем что загрузились изображения товаров
    img_count = page.locator("img").count()
    assert img_count > 2, f"Пицца: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Пицца загружена - найдено {img_count} изображений товаров")
    
    print("📍 Клик Еще...")
    page.get_by_role("link", name="Еще").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)  # Дополнительное ожидание на случай асинхронной загрузки
    img_count = page.locator("img").count()
    # Проверяем что есть хотя бы какой-то контент (товары загружены)
    assert page.locator("button").count() > 0 or img_count > 0, "Еще: контент не загружен!"
    print(f"✓ Еще загружено")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Роллы...")
    page.get_by_role("link", name="Роллы").click()
    page.wait_for_load_state("networkidle")
    img_count = page.locator("img").count()
    assert img_count > 2, f"Роллы: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Роллы загружены - найдено {img_count} изображений товаров")
    
    print("📍 Клик Еще...")
    page.get_by_role("link", name="Еще").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(1000)  # Дополнительное ожидание на случай асинхронной загрузки
    img_count = page.locator("img").count()
    # Проверяем что есть хотя бы какой-то контент (товары загружены)
    assert page.locator("button").count() > 0 or img_count > 0, "Еще: контент не загружен!"
    print(f"✓ Еще загружено")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Сеты...")
    page.get_by_role("link", name="Сеты").click()
    page.wait_for_load_state("networkidle")
    img_count = page.locator("img").count()
    assert img_count > 2, f"Сеты: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Сеты загружены - найдено {img_count} изображений товаров")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Снеки...")
    page.get_by_role("link", name="Снеки").click()
    page.wait_for_load_state("networkidle")
    img_count = page.locator("img").count()
    assert img_count > 2, f"Снеки: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Снеки загружены - найдено {img_count} изображений товаров")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Десерты...")
    page.get_by_role("link", name="Десерты").click()
    page.wait_for_load_state("networkidle")
    img_count = page.locator("img").count()
    assert img_count > 0, f"Десерты: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Десерты загружены - найдено {img_count} изображений товаров")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Напитки...")
    page.get_by_role("link", name="Напитки").click()
    page.wait_for_load_state("networkidle")
    img_count = page.locator("img").count()
    assert img_count > 0, f"Напитки: недостаточно изображений ({img_count}), товары не загружены!"
    print(f"✓ Напитки загружены - найдено {img_count} изображений товаров")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")
    
    print("📍 Переход на Отзывы...")
    page.get_by_role("link", name="Отзывы").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=★").count() > 0 or page.locator("role=article").count() > 0, "Отзывы: контент не загружен!"
    print(f"✓ Отзывы загружены")
    
    print("📍 Клик Назад...")
    page.get_by_role("link", name="Назад").click()
    page.wait_for_load_state("networkidle")
    assert page.locator("text=Пицца").is_visible(), "Меню не отобразилось!"
    print("✓ Вернулись на главную")

    print("\n✅ Все тесты пройдены успешно!")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

