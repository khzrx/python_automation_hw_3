from selene import be, have


def test_yandex_search_with_result(browser_object, yandex):
    browser_object.element('input[name="text"]').should(be.blank).type('qa guru').press_enter()
    browser_object.element('a[href^="https://qa.guru/"]').should(be.present)

def test_yandex_search_no_result(browser_object, yandex):
    text = 'alksdjklajsdlkjalsjdlajsd'
    browser_object.element('input[name="text"]').should(be.blank).type(f'{text}').press_enter()
    browser_object.element('[class="EmptySearchResults-Title"]').should(have.text("Ничего не нашли"))

