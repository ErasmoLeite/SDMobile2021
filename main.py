from appium import webdriver
import pytest

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "9.0"
caps["browserName"] = ""
caps["appium:appiumVersion"] = "1.22.0"
caps["appium:deviceName"] = "Samsung Galaxy S9 FHD GoogleAPI Emulator"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:app"] = "storage:filename=Calculator_v7.8 (271241277)_apkpure.com.apk"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

#   Acionador do Script / codigo
if __name__ == '__main__':

#def teste_somar_dois_numeros():
# Conexão com o SauceLabs, apotamento para o datacenter, inserir o endereço remote em webdriver.remote  - Endereço:Disponível no saucelabs em User Settings "Copiar conteudo" Driver Creation
    driver = webdriver.Remote("Inserir Link Driver Creation", caps)

    resultado_esperado = '8'

    #Realiza a Conta
    botao_3 = driver.find_element_by_id("com.google.android.calculator:id/digit_3")
    botao_3.click()
    botao_somar = driver.find_element_by_accessibility_id("plus")
    botao_somar.click()
    botao_5 = driver.find_element_by_id("com.google.android.calculator:id/digit_5")
    botao_5.click()
    botao_igual = driver.find_element_by_accessibility_id("equals")
    botao_igual.click()
    resultado_final = driver.find_element_by_id("com.google.android.calculator:id/result_final")
    print(f'resultado final = {resultado_final.text} \n resultado esperado = {resultado_esperado}')

    assert resultado_final.text==resultado_esperado

    driver.quit()