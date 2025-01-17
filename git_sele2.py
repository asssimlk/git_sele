from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time



driver = webdriver.Chrome()

wait = WebDriverWait(driver, 30000)
url1 = 'https://www.etsy.com/uk/promotions'
driver.get(url1)
driver.maximize_window()
time.sleep(3)


def test_numbers(start, end):
    results = {
        'working': [],
        'failed': []
    }

    for number in range(start, end + 1):
        print(f'Testing number: {number}')

        # Find the input field and button
        input_field = driver.find_element(By.ID, 'input-promotion-code')  # Update with the actual ID
        button = driver.find_element(By.ID, 'button-redeem')  # Update with the actual ID

        # Clear the input field and enter the number
        input_field.clear()
        input_field.send_keys(str(number))
        time.sleep(0.3)
        button.click()

        # Wait for a moment to allow the page to process the input
        time.sleep(1)  # Adjust the sleep time as necessary

        # Check for the error message using XPath
        try:
            error_message = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/form/div[2]/span')
            if "Please enter a valid promotion code" in error_message.text:
                print(f' {number} failed: {error_message.text}')
                results['failed'].append(number)
                # Refresh the page to continue testing
                time.sleep(0.3)  # Wait for the page to reload
                continue  # Skip to the next number
            else:
                # If the error message is not found, treat it as success
                print(f' {number} treated as success (no error message found)')
                results['working'].append(number)
                time.sleep(5)  # Wait for 5 seconds before going back to the page
                driver.get('url1')  # Navigate back to the target page
                continue  # Continue to the next number
        except:
            print(f' {number} treated as success (no error message found)')
            results['working'].append(number)
            time.sleep(5)  # Wait for 5 seconds before going back to the page
            driver.get(url1)  # Navigate back to the target page
            continue  # Continue to the next number



    print('=== Testing Complete ===')
    print('Working numbers:', results['working'])
    print('Total working numbers:', len(results['working']))
    print('Total tested numbers:', len(results['working']) + len(results['failed']))


# Run the test
test_numbers(2236, 2240)  # Adjust the range as needed

# Close the driver after testing
driver.quit()
