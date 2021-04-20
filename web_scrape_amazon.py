import bs4
#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

URL = ["https://www.amazon.com.au/Curash-Soothing-Oatmeal-Baby-400ML/dp/B07845LWSW/ref=pd_sbs_194_7?_encoding=UTF8&pd_rd_i=B07845LWSW&pd_rd_r=ba37dd7b-72b2-4868-a48a-82c682c1ac65&pd_rd_w=qzklN&pd_rd_wg=KO3Iz&pf_rd_p=6f60518d-a8b6-4e66-b5e9-a219cbe12564&pf_rd_r=DN74Q4Y3TN249EES4BNW&psc=1&refRID=DN74Q4Y3TN249EES4BNW",
"https://www.amazon.com.au/Curash-Soap-Free-Baby-400mL/dp/B00AR6PGOM/ref=pd_sbs_121_1/356-3780240-6265467?_encoding=UTF8&pd_rd_i=B00AR6PGOM&pd_rd_r=6975f1cb-26bc-4996-9da6-efa1d1a3e629&pd_rd_w=gEXr4&pd_rd_wg=K95k5&pf_rd_p=6f60518d-a8b6-4e66-b5e9-a219cbe12564&pf_rd_r=10HNYSQBYPRRZ3B4S0FM&psc=1&refRID=10HNYSQBYPRRZ3B4S0FM",
"https://www.amazon.com.au/HUGGIES-Baby-Wipes-Fragrance-Refill/dp/B07NPM94XB/ref=zg_bs_baby-products_2?_encoding=UTF8&psc=1&refRID=71V6BYM9Z41W02RHT80W",
#"https://www.amazon.com.au/TOMMEE-TIPPEE-Baby-Care-Black/dp/B0774GXCPT/ref=zg_bs_baby-products_18?_encoding=UTF8&psc=1&refRID=71V6BYM9Z41W02RHT80W",
"https://www.amazon.com.au/Johnsons-Cotton-100-Pure-Natural-Canister/dp/B009RCPQ42/ref=zg_bs_baby-products_23?_encoding=UTF8&psc=1&refRID=71V6BYM9Z41W02RHT80W",
"https://www.amazon.com.au/Johnsons-Baby-Bedtime-Bath-500ml/dp/B0793TDGF3/ref=sr_1_1?dchild=1&keywords=Johnson+Baby+Bedtime+Bath+500mL&qid=1600324834&s=baby-products&sr=1-1",
"https://www.amazon.com.au/ICD-Online-Nappy-Orignal-Disposal/dp/B07TGLVKH5/ref=sr_1_1?dchild=1&keywords=ICD+Nappy+Sacks+The+Orignal+Nappy+Disposal+400+Bags%2C+400+count&qid=1600341025&sr=8-1","https://www.amazon.com.au/ASAKUKI-Aromatherapy-Eucalyptus-Lemongrass-Water-soluble/dp/B07RL71N7W/ref=zg_bs_beauty_home_1?_encoding=UTF8&psc=1&refRID=Y9XTR1TP2V6XAWR1XH38"]

filename = "Find_Min.csv"
f = open(filename, "w")
heading = "Brand_Name, P_Name, P_Price, M_Quantity, URL\n"
f.write(heading)

i=0
noUrl = len(URL)
for noUrl in URL:
    hello = str(URL[i])
    uClient =  Request(hello,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'})
    page_html = urlopen(uClient).read()
    page_soup = soup(page_html, "lxml")

    product_name = page_soup.find("span",{"id":"productTitle"}).text.strip()
    product_price = page_soup.find("span",{"id":"priceblock_ourprice"}).text.strip()
    brand_name = page_soup.find("a",{"id":"bylineInfo"}).text.replace("Visit the", "").replace("Brand:","")
    min_quantity =  page_soup.find("select",{"name":"quantity"}).option.text.strip()

    print("Product Name: " + product_name)
    print("Product Price: " + product_price)
    #print("The Link : " + hello)
    print("The Brand Name :" + brand_name)
    print("Minimum quantity : " + min_quantity)
    print("\n")
    
    f.write(brand_name + "," + product_name.replace(",","") + "," + product_price + "," + min_quantity +"," + hello + "\n")
    i=i+1
f.close()

print("I GUESS IT IS DONE !!!")
