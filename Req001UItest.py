from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

elereq = []
elexp = []
eletag = []
respcode = []
n = 0
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service_obj = Service("C:/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get('https://reqres.in/')
tot_req = driver.find_elements(By.XPATH, '//*[@data-key="endpoint"]')
tot_tag = driver.find_elements(By.TAG_NAME, 'a')
print(tot_req)
print(tot_tag)


# To Be implemented in detailed manner as a part of Framework Design
def verificationTest(actual, expected):
    assert actual == expected, "TestCase : Failed"
    print("TestCase : Passed")


ii: WebElement
for ii in tot_tag:
    idntxt = " " + ii.text.capitalize().format() + ' '
    eletag.append(idntxt)

print(eletag)
eletag = eletag[5:21]

resultX = ['ab'] * len(eletag)
print(eletag)
for k in eletag:
    k = "'" + k + "'"
    resultX[n] = " ".join(["//a[text() = ", k, "]"])
    n = n + 1
print(resultX)

for ele in resultX:
    try:
        element = driver.find_element(By.XPATH, ele)
        element.click()
        reqcap = driver.find_element(By.CLASS_NAME, "url")
        rescod = driver.find_element(By.CLASS_NAME, "response-code")
        print(reqcap.text)
        # verificationTest(reqcap.text, "")
        print(rescod.text)
        # verificationTest(rescod.text, "")

    except NoSuchElementException:
        track = resultX.index(ele)
        print("Exception Handled : Issue With APP Element: FAIL", track)
    else:
        continue

butSupport = driver.find_element(By.XPATH, "//a[text() = 'Support ReqRes']")
# Here we can give one assertion for Button Check at multiple levels
butSupport.click()

oneTime = driver.find_element(By.NAME, "support")
payment1 = oneTime.get_dom_attribute("value")
print("Pay1", payment1)
verificationTest(payment1, "supportOneTime")
