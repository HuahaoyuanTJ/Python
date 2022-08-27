import time
import winsound
from selenium import webdriver
import datetime

driver = webdriver.Chrome()
driver.get("https://uogapply.mycampus.gla.ac.uk/psc/campus/EMPLOYEE/SA/c/CY2_AD_MENU.CY2_AD_NUR_FL.GBL&cmd=start?CAMPUS_URL=https%3a%2f%2fuogapply.mycampus.gla.ac.uk%3a443%2fpsp%2fcampus%2fEMPLOYEE%2fSA%2fs%2fWEBLIB_SCC_NUR.SCC_SS_GATEKEEPER.FieldFormula.IScript_SCC_GateKeeper%3fSCC_APPL_CONTXT_ID%3dSCC_NURCTXT_20171218163641")
time.sleep(80)
winsound.Beep(400, 2000)
#-----------------------------------------------------------------------------------------
while 1:
    cas_Numb = driver.find_element("id","win0divSAD_PB_CAS_NUMBER$0").text
    if cas_Numb == " ":
        print("Value is null----" + str(datetime.datetime.now()))
        print(cas_Numb)
        driver.refresh()
        time.sleep(40)
    else:
        print("CAS has updated!!!----" + str(datetime.datetime.now()))
        print(cas_Numb)
        winsound.Beep(400, 100000)
        break

#-----------------------------------------------------------------------------------------
