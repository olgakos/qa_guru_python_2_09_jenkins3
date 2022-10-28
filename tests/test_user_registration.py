import allure

from demoqa_tests.model.pages import registration_form
from tests.test_data.users import student

@allure.title("Successful fill form")
def test_submit_student_registration_form(setup_browser):
    browser = setup_browser
    registration_form.given_opened(browser)
    browser.driver.set_window_size(1920, 1500) #размер окна важен, если есть всплывающая реклама

    # WHEN
    with allure.step("Fill form"):
        registration_form.set_field('#firstName', student.name, browser)
        registration_form.set_field('#lastName', student.last_name, browser)
        registration_form.set_field('#userEmail', student.email, browser)
        registration_form.set_gender(student.gender.value, browser)       
        registration_form.set_field('#userNumber', student.user_number, browser)
        registration_form.scroll_to_bottom(browser)
        registration_form.set_birth_date(student.birth_month, student.birth_year, student.birth_day, browser)
        # OR
        #browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('01 Jan 2000').press_enter()
        registration_form.add_subjects(student.subjects, browser)
        registration_form.set_hobbies(student.hobbies, browser)
        registration_form.scroll_to_bottom(browser)
        registration_form.send_file(student.picture_file, browser)
        registration_form.set_field('#currentAddress', student.current_address, browser)
        registration_form.set_state(student.state, browser)
        registration_form.set_city(student.city, browser)
    with allure.step("Press Submit button"):
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
                ('Subjects', 'History'), #Это ожидаемое значение
                ('Hobbies', 'Reading'),  #Это ожидаемое значение
                ('Picture', student.picture_file),
                ('Address', student.current_address),
                ('State and City', f'{student.state} {student.city}'),
            ], browser
        )
