from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
from pandas import DataFrame


exec_path = "C:/Users/tpoll/OneDrive/Desktop/coding/helpers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=exec_path)

payscale_url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
driver.get(payscale_url)

# Click Accept Cookies
sleep(5)
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/div/div[2]/div/button[2]').click()

# # For testing purposes: click right to the end, otherwise takes very long to go through
# driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/article/div[3]/a[6]').click()

# Set up list to append the data to
table_data = []
while True:
    driver.implicitly_wait(10)
    rows = driver.find_elements(By.CLASS_NAME, 'data-table__row')


    for i, row in enumerate(rows, 1):
        ranking = row.find_element(By.CLASS_NAME, 'data-table__cell.csr-col--rank').text
        major = row.find_element(By.CLASS_NAME, 'data-table__cell.csr-col--school-name').text
        early_career_pay = row.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/article/div[2]/table/tbody/tr[{i}]/td[4]').text
        mid_career_pay = row.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/article/div[2]/table/tbody/tr[1]/td[5]').text

        try:
            early_career_pay = float(early_career_pay.replace('$', '').replace(',', ''))
            mid_career_pay = float(mid_career_pay.replace('$', '').replace(',', ''))
        except ValueError:
            pass

        data = {
            "Undergraduate Major": major,
            "Early Career Pay": early_career_pay,
            "Mid-Career Pay": mid_career_pay
        }
        table_data.append(data)

    try:
        end_page = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn.pagination__btn--off')
    except:
        next_page = driver.find_element(By.CSS_SELECTOR, '#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn')
        next_page.click()
    else:
        break


# Convert list of prepared rows to a pandas dataframe or convert to csv
df = DataFrame(data=table_data)
print(df)

df.to_csv('2021_salaries_by_college_majors.csv', index=False)