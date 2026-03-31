import os
import time

from faker.generator import random

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, UploadAndDownloadPage

class TestElements:
    """ class TestTextBox:


        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            output_data = text_box_page.check_filled_form()

            assert input_data == output_data           
            
            

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()

            assert input_checkbox == output_checkbox, 'Checkboxes do not match'

    
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            #radio_button_page.click_on_the_radio_button('no')
            #output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', 'YES radio button is not selected'
            assert output_impressive == 'Impressive', 'IMPRESSIVE radio button is not selected'
            #assert output_no == '', 'NO radio button should not be selected'

            print(f"YES: {output_yes}, IMPRESSIVE: {output_impressive}")


    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            person_list = web_table_page.check_added_person()
            print(f"\nAdded person: {new_person}")
            print(f"Person list: {person_list}")
            assert new_person in person_list, 'Added person is not in the table'


        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'Search result does not contain the key'
            

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            search_key = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(search_key)
            updated_field, updated_value = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert updated_value in row, f'{updated_field} was not updated correctly'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            search_key = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(search_key)
            web_table_page.delete_person()
            row = web_table_page.check_search_person()
            assert row == '', 'Person was not deleted successfully'
        
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            expected_counts = [10, 20, 30, 40, 50]
            assert count == expected_counts, f'Expected row counts {expected_counts}, but got {count}'
    
    class TestButtonsPage:
        def test_different_on_the_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double_click_result = buttons_page.double_click_on_the_button()
            right_click_result = buttons_page.right_click_on_the_button()
            click_result = buttons_page.click_on_the_button()

            assert double_click_result == 'You have done a double click', 'Double click result is incorrect'
            assert right_click_result == 'You have done a right click', 'Right click result is incorrect'
            assert click_result == 'You have done a dynamic click', 'Click result is incorrect'

    class TestLinksPage:
        def test_check_links(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'The link did not open in a new tab or the URL is incorrect'
            
        def test_broken_list(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            broken_link_status = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert broken_link_status == '400', f'Broken link with status code: {broken_link_status}' """
            
    class TestUploadAndDownload:
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, uploaded_file_path = upload_download_page.upload_file()
            assert file_name == uploaded_file_path, 'Uploaded file name does not match the expected file name'

        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()

            file_path, file_name, file_size = upload_download_page.download_file()
            print(f"Downloaded file path: {file_path}")
            print(f"Downloaded file name: {file_name}")
            print(f"Downloaded file size: {file_size}")


            try:
                assert os.path.exists(file_path), 'Downloaded file does not exist'
                assert file_size > 0, 'Downloaded file is empty'
                assert file_name.endswith(".jpeg"), 'Downloaded file does not have the expected .jpeg extension'
            finally:
                upload_download_page.delete_downloaded_file(file_path)

