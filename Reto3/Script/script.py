from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time

# Opciones de navegación
options = Options()
options.add_argument("start-maximized")
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Inicializamos el navegador
driver.get('http://www.pbclibrary.org/raton/mousercise.htm?')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='¡Vamos a Empezar los Ejercicios del Ratón!']"))).click() #index
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'1')]"))).click() #1
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'2')]"))).click() #2
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'3')]"))).click() #3
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'4')]"))).click() #4
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'5')]"))).click() #5
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'6')]"))).click() #6
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'7')]"))).click() #7
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'8')]"))).click() #8
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'9')]"))).click() #9
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'10')]"))).click() #10
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'11')]"))).click() #11
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'12')]"))).click() #12
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'13')]"))).click() #13
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Proxima')]"))).click() #14
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'¿Dónde está el ratón?')]"))).click() #15
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='clicker']"))).click() #16
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continua']"))).click() #17
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@value='¡Oye esto esta buenísimo!']"))).click() #18
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']"))).click() #19
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='llaves']"))).click() #20
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Kokopelli']"))).click() #21

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b1']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b2']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b3']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b4']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b5']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b6']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b7']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b8']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b9']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b10']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='b11']"))).click()  #22
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #22

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Púlseme']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Yo también']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='boton de inicio']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='alien']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='metal']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@onclick='setCheck(4)']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Próxima']"))).click()  #23
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #23

ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f1']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f2']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f3']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f4']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f5']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f6']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f7']")))).perform() #24
ActionChains(driver).double_click(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='f8']")))).perform() #24
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #24

ActionChains(driver).click_and_hold(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='red-slider']")))).perform() #25
ActionChains(driver).click_and_hold(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='blue-slider']")))).perform() #25
ActionChains(driver).click_and_hold(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='green-slider']")))).perform() #25
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continua')]"))).click()  #25

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Próxima')]"))).click()  #26
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Próxima')]"))).click()  #27
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Próxima')]"))).click()  #28
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Próxima')]"))).click()  #29
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Próxima')]"))).click()  #30

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Pulse para mostrar la caja de aviso')]"))).click()  #31
Alert(driver).accept() #31

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continua')]"))).click()  #32

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[2]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[3]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[4]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[5]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[6]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[7]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[8]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[9]"))).click()  #33
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #33

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[7]"))).click() #34

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[2]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[3]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[4]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[5]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[6]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[7]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[8]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[9]"))).click()  #35
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #35

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continua']"))).click()  #36

select = Select(driver.find_element(By.XPATH, "//select[@name='theChoices']")) #37
select.select_by_visible_text('Cinco') #37
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #37

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continua']"))).click()  #38

select = Select(driver.find_element(By.XPATH, "//select[@name='theChoices']")) #39
select.select_by_visible_text('Seis') #39
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@name='advance']"))).click()  #39

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continua']"))).click()  #40

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continua']"))).click()  #41
time.sleep(5)