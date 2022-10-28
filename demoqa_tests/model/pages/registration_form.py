from typing import Tuple

import allure
from selene import have, command
from selene.support.shared.jquery_style import ss

from demoqa_tests.model.controls import dropdown, date
from demoqa_tests.utils import path
from tests.test_data.users import Subject

def given_opened(browser):
    browser.open('http://demoqa.com/automation-practice-form')
'''
    #рекламные блоки(!)
    #1
    ads = ss('[id^=google_ads][id$=container__]')
        if ads.with_(timeout=15).wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
'''
    #2     
    ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.wait.until(have.size_less_than_or_equal(4)):
            ads.perform(command.js.remove)            
  

#@allure.step('Add subjects {values}')
def add_subjects(values: Tuple[Subject], browser):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()

#@allure.step('Change state {value}')
def set_state(value: str, browser):
    dropdown.select(browser.element('#state'), value, browser)

def set_state_with_typing(value: str, browser):
    dropdown.select_with_typing(browser.element('#reac@allure.step("Change state {values}")t-select-3-input'), value)

#@allure.step('Change city {value}')
def set_city(value: str, browser):
    dropdown.select(browser.element('#city'), value, browser)

def set_city_with_typing(value: str, browser):
    dropdown.select_with_typing(browser.element('#react-select-4-input'), value)


#@allure.step('Scroll to bottom')
def scroll_to_bottom(browser):
    browser.element('#state').perform(command.js.scroll_into_view)

def should_have_submitted(data, browser):
    rows = browser.element('.modal-content').all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))


def set_field(selector, text, browser):
    browser.element(selector).type(text)


def set_gender(gender, browser):
    browser.all('[for^=gender-radio]').by(have.exact_text(gender)).first.click()


def set_birth_date(month, year, day, browser):
    date.date_picker(month, year, day, browser)


def send_file(file, browser):
    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(file)
    )


def set_hobbies(hobbies, browser):
    for hobby in hobbies:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element('..').click()


def submit(browser):
    browser.element('#submit').perform(command.js.click)
