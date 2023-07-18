from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://allegro.pl/oferta/rust-pelna-wersja-steam-13857559260?reco_id=cd6da594-258f-11ee-8851-4e991bb352df&sid=7d57f5ef092032639969aa24b7a6e07a65c247015427a0fba01293aeed154791'

def getContent(url):
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()
    driver.get(url)

    # Find the <div> element with the specified class name
    div_element = driver.find_element(By.CLASS_NAME, '_7030e_qVLm-')

    if div_element:
        # Get the content of the <div> element
        div_content = div_element.text

        # Convert the content from string to float
        price = float(div_content.replace(" zł", "").replace(",", "."))

        # Print the result
        print(price)
    else:
        print('No <div> element with the specified class name found.')

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    getContent(url)
