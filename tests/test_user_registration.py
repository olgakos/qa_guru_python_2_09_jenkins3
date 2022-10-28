import allure

from demoqa_tests.model.pages import registration_form
from tests.test_data.users import student

@allure.title("Successful fill form")
def test_submit_student_registration_form(setup_browser):
    browser = setup_browser
    registration_form.given_opened(browser)
    browser.driver.set_window_size(1920, 1080) #важно при рекламе!

    # WHEN

    with allure.step("Fill form"):
        registration_form.set_field('#firstName', student.name, browser)
        registration_form.set_field('#lastName', student.last_name, browser)
        registration_form.set_field('#userEmail', student.email, browser)
        registration_form.set_gender(student.gender.value, browser)
        '''
        # OR
        gender_male = browser.element('[for=gender-radio-1]')
        gender_male.click()
        # OR
        gender_male = browser.element('[for=gender-radio-1]')
        gender_male.click()
        # OR
        browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
        browser.element('[id^=gender-radio][value=Male]').element(
            './following-sibling::*'
        ).click()
        # OR better:
        browser.element('[id^=gender-radio][value=Male]').element('..').click()
        # OR
        browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
        browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
        '''
        registration_form.set_field('#userNumber', student.user_number, browser)
        registration_form.scroll_to_bottom(browser)
        registration_form.set_birth_date(student.birth_month, student.birth_year, student.birth_day, browser)
        '''
        # OR something like
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('01 Jan 2000').press_enter()
        '''
        registration_form.add_subjects(student.subjects, browser)
        registration_form.set_hobbies(student.hobbies, browser)
        registration_form.scroll_to_bottom(browser)
        registration_form.send_file(student.picture_file, browser)
        registration_form.set_field('#currentAddress', student.current_address, browser)

        registration_form.set_state(student.state, browser)
        registration_form.set_city(student.city, browser)

        registration_form.submit(browser)

    # THEN
    with allure.step("Check form results"):
        registration_form.should_have_submitted(
            [
                ('Student Name', f'{student.name} {student.last_name}'),
                ('Student Email', student.email),
                ('Gender', student.gender.value),
                ('Mobile', student.user_number),
                ('Date of Birth', f'{student.birth_day} {student.birth_month},{student.birth_year}'),
                ('Subjects', 'History'),
                ('Hobbies', 'Sports'),
                ('Picture', student.picture_file),
                ('Address', student.current_address),
                ('State and City', f'{student.state} {student.city}'),
            ], browser
        )
