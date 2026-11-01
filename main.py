from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import ctypes
import undetected_chromedriver as uc 

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
subs=open("result.txt","a+")
inp=input("accounts file (.txt) : ")
accounts = open(inp,"r")
def worker(line):
    driver = webdriver.Chrome(options=chrome_options)
    ac=line.split(":")
    mail = ac[0]
    pw = ac[1]
    val_usr = ac[2]
    val_pw = ac[3]
    driver.set_window_size(1024, 768)
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=3600&openid.return_to=https%3A%2F%2Fgaming.amazon.com%2Fprime%2Fusamazonlogin%2Fxd%3Fconfirm%3DALWAYS%26returnUri%3Dhttps%253A%252F%252Famazon.com%252Fap%252Fsignin%253Fopenid.pape.max_auth_age%253D3600%2526openid.return_to%253Dhttps%25253A%25252F%25252Fgaming.amazon.com%25252Floot%25252Fleagueoflegends%25253FsignedIn%25253Dtrue%2526openid.identity%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.assoc_handle%253Damzn_respawn_desktop_us%2526openid.mode%253Dcheckid_setup%2526openid.claimed_id%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0%25252Fidentifier_select%2526openid.ns%253Dhttp%25253A%25252F%25252Fspecs.openid.net%25252Fauth%25252F2.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_respawn_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gaming_prime&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.ahzf8VWMq50eybIidHLgWWYdhNwTEBEkKDZ46Gs6A3P7nOlNOc3n3w.PKYZa3viah3J9I1w._Dv9DmV2-65BVVFN-LN5n5J19jX2LD1eKezLN_GYe--hB095isUcCSPqrYJ7Jkkzu_A5jxS44qcwnu83fdJSoOlJEF5BFASrtAjPibdK9y0OzWhkzSCqDdvGj3U4qhkPBJCuavpSNj8VBgb08pRej5bll9qBi9BGHHTjzfD26wx5wKm6KTLI4QCey4psjaN23jOCbRcyaQ4.JJk6AiHSEodi6lHfi5P0Ng")
    m = driver.find_element(By.CSS_SELECTOR, '[type="email"],[maxlength="128"]')
    m.send_keys(mail)
    sleep(1)
    p = driver.find_element(By.CSS_SELECTOR, '[type="password"],[maxlength="1024"]')
    p.send_keys(pw)
    sleep(1)
    si = driver.find_element(By.CSS_SELECTOR, '[id="signInSubmit"]')
    si.submit()
    sleep(8)
    if "https://www.amazon.com/" == driver.current_url:
        subs.write(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} Twitch prime expired \n')
        print(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} Twitch prime expired \n')
        driver.close()
        return
    try:
        driver.find_element(By.ID, 'auth-captcha-guess')
        subs.write(f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Captcha \n')
        print(f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw}: Captcha')
        ctypes.windll.user32.MessageBoxW(0, " Error , Captcha problem", "Error")
        driver.close()
        input("Press Enter to exit")
        #exit()
        return
    except :
        pass
    try :
        driver.find_element(By.CSS_SELECTOR, '[class="a-box-inner a-alert-container"]')
        subs.write(
        f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Incorrect amazon account details \n')
        print(f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Incorrect amazon account details')
        driver.close()
        return
    except :
        pass
    cw = driver.current_url
    if "https://www.amazon.com/ap/cvf/transactionapproval?" == cw[:50]:
        subs.write(
            f' you need to verify and pass to the next account')
        print(
            f' you need to verify and pass to the next account')
        driver.close()
        return
    print(f'amazon : {mail} | logged in')
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'[class="tw-interactive tw-button tw-button--amazon"]')))
        driver.find_element(By.CSS_SELECTOR ,'[class="tw-interactive tw-button tw-button--amazon"]').click()
    except:
        pass
    #check if receive content is clickable
    try:WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="tw-interactive tw-button tw-button--full-width"]')))
    except:
        subs.write(f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Already linked and claimed reward \n')
        print(f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Already linked and claimed reward ')
        driver.close()
        return
    banner = driver.find_element(By.CSS_SELECTOR,'[class="tw-interactive tw-button tw-button--full-width"]')
    sleep(1)
    banner.click()
    sleep(4)
    '''
    try:
        driver.find_element(By.CSS_SELECTOR ,'[class="sign-up-button tw-pd-x-10 tw-pd-y-1"]')
        subs.write(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} Twitch prime expired \n')
        print(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} Twitch prime expired \n')
        driver.close()
        return
    except:
        pass
    '''
    sleep(1)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[class="tw-interactive tw-button"]')))
    except:
        subs.write(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Unable to proceed to sign-in page \n')
        print(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Unable to proceed to sign-in page')
        driver.close()
        return   
    driver.find_element(By.CSS_SELECTOR,
                        '[class="tw-interactive tw-button"]').click()
    print(f"logging on riot account : {val_usr} ")
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,'username')))
    except:
        subs.write(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Unable to proceed to sign-in page \n')
        print(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Unable to proceed to sign-in page')
        driver.close()
        return      
    driver.find_element(By.NAME,"username").send_keys(val_usr)
    sleep(1)
    driver.find_element(By.NAME,"password").send_keys(val_pw)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'[data-testid="btn-signin-submit"][type="submit"]').click()
    sleep(10)
    try :
        driver.find_element(By.CSS_SELECTOR,'[data-testid="btn-signin-submit"][type="submit"]')
        subs.write(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Incorrect riot account details or expired riot account \n')
        print(
            f'riot account : {val_usr}:{val_pw} with amazon account : {mail}:{pw} : Incorrect riot account details or expired riot account')
        driver.close()
        return
    except :
        pass
    print(f'successfully logged in to riot : {val_usr}')
    try :
        driver.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
    except :
        pass
    sleep(5)
    print(f"{val_usr} : account linked successfully\n")
    sleep(5)
    driver.close()
threads = input("threads number : ")

with ThreadPoolExecutor(max_workers=int(threads)) as pool:
    for line in accounts.read().strip().splitlines():
        pool.submit(worker,line)
input("Press Enter to exit")


