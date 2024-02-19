from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.page_load_strategy = 'eager'

#输入：日期（例：2021-12-05）、货币类型（中文形式）
def get_data(date,currency_class):
    driver = webdriver.Chrome(options=options) 
    driver.get("https://www.boc.cn/sourcedb/whpj/") 
    date_from = driver.find_element(By.ID, 'erectDate')
    date_from.send_keys(date)
    
    date_to = driver.find_element(By.ID, 'nothing')
    date_to.send_keys(date)
    
    dropdown = Select(driver.find_element(By.ID,"pjname")) 
    dropdown.select_by_visible_text(currency_class) 
    
    search_button = driver.find_element(By.XPATH,"//*[@id='historysearchform']/div/table/tbody/tr/td[7]/input")
    search_button.click()
    table = driver.find_element(By.XPATH,"/html/body/div/div[4]/table/tbody").find_elements(By.XPATH,"./*")
    
    if len(table) == 3 and table[1].find_elements(By.XPATH,"./*")[0].text == "对不起，没有检索结果，请换其他检索词重试！":
        #没有该货币在此天的信息
        get_data_success = False
        output = "没有检索结果"
    else:
        get_data_success = True
        output = "No Data"    #该货币无现汇卖出价信息
        for i in range(1,len(table)-1):
    
            if len(table[i].find_elements(By.XPATH,"./*")[3].text) !=0:
                output = table[i].find_elements(By.XPATH,"./*")[3].text
                break
    return get_data_success,output
code_trans_dic = {
    "GBP":"英镑",
    "HKD":"港币",
    "USD":"美元",
    "CHF":"瑞士法郎",
    "SGD":"新加坡元",
    "SEK":"瑞典克朗",
    "DKK":"丹麦克朗",
    "NOK":"挪威克朗",
    "JPY":"日元",
    "CAD":"加拿大元",
    "AUD":"澳大利亚元",
    "EUR":"欧元",
    "MOP":"澳门元",
    "PHP":"菲律宾比索",
    "THP":"泰国铢",
    "NZD":"新西兰元",
    "KPW":"韩元",
    "SUR":"卢布",
    "MYR":"林吉特",
    "TWD":"新台币",
    "ESP":"西班牙比塞塔",
    "ITL":"意大利里拉",
    "NLG":"荷兰盾",
    "BEF":"比利时法郎",
    "FIM":"芬兰马克",
    "IDR":"印尼卢比",
    "BRC":"巴西里亚尔",
    "AED":"阿联酋迪拉姆",
    "INR":"印度卢比",
    "ZAR":"南非兰特",
    "SAR":"沙特里亚尔",
    "TRL":"土耳其里拉",
    }

key = input()

key = key.split(" ")
    
if len(key) == 2:
    date = key[0]
    currency_code = key[1]
    if len(date) == 8:
        formatted_date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
        has_currency = True
        try:
            currency = code_trans_dic[currency_code]
        except:
            has_currency = False
        if has_currency == True:    
            a,data = get_data(formatted_date, currency)
            result = data
        else:
                #网站内不存在该货币的数据
            result = '无此货币数据'
    else:
        result = "日期格式错误"
else:
    result = "输入格式错误"
with open("result.txt", "w") as file:
    # 将结果写入文件
    file.write(result)
