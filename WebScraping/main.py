from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
index=1
gadget="mobiles" #input("Enter gadget name to search:")
prices=[]
descriptions=[]
ratings=[]
specifications=[]
core=[]
ram=[]   
hdd=[]
warranty=[]
display=[]
def fetch_data():
    global index
    pages=10#int(input("Enter No. of pages to scrap:"))
    for i in range(1,pages+1):
        url=f"https://www.flipkart.com/search?q={gadget}&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&as-pos=1&as-type=HISTORY&suggestionId={gadget}&requestId=4279052d-1af4-4207-aede-da43241ae41c&as-searchtext=laptops&page={i}"
        data=requests.get(url).text
        #to scrape all html file
        soup=BeautifulSoup(data,"lxml")
        #scrape every individual laptop details
        wholes=soup.find_all("div",class_="_3pLy-c row")

        for whole in wholes:
            #to find descriptions of the laptops
            desc=whole.find_all('div',class_='_4rR01T')
            description=[]
            #to discard html tags
            for i in range(len(desc)):
                description.append(desc[i].text) #filtering out only text
            descriptions.extend(description)

            rat=whole.find_all('div',class_='_3LWZlK')
            rating=[]
            for i in range(len(rat)):
                rating.append(rat[i].text)    #filtering out only text
            ratings.extend(rating)
            
            spec=whole.find_all("li",'rgWa7D')
            
            specifications=[]
            for i in range(len(spec)):
                specifications.append(spec[i].text)  #filtering out only text
            
            for i in specifications:
                if 'Core' in i:
                    core.append(i)
                elif 'RAM' in i:
                    ram.append(i)
                elif 'SSD' in i or 'HDD' in i:
                    hdd.append(i)
                elif 'Warranty' in i:
                    warranty.append(i)
                elif 'Display' in i:
                    display.append(i)
            
            #scrapes the html tags of price
            price=whole.find_all("div",class_="_30jeq3 _1_WHN1")

            for i in range(len(price)):
                prices.append(price[i].text)   #filtering out only text

    #to create text file
    ref=open(f"{gadget}_description{index}.txt","w")
    for i in range(len(ratings)):
        ref.write(f"{descriptions[i]} \n")
    ref.close()
    print('prices:',len(prices))
    print('descriptions:',len(descriptions))
    print('ratings:',len(ratings))
    print('specifications:',len(specifications))
    print('core:',len(core))
    print('ram:',len(ram))
    print('hdd:',len(hdd))
    print('warranty:',len(warranty))
    print('display:',len(display))
    if gadget=="laptops":
        le=len(warranty)-1
        df={"description":descriptions[slice(le)],"core":core[slice(le)],"ram":ram[slice(le)],"hdd":hdd[slice(le)],"display":display[slice(le)],"warranty":warranty[slice(le)],"rating":ratings[slice(le)],"price":prices[slice(le)]}

    elif gadget=="mobiles":
        le=len(ram)-1
        df={"description":descriptions[slice(le)],"ram":ram[slice(le)],"display":display[slice(le)],"rating":ratings[slice(le)],"price":prices[slice(le)]}
    dataset=pd.DataFrame(data=df)       
    dataset.to_csv(f"{gadget}{index}.csv")
    pd.read_csv(f"{gadget}{index}.csv")
    index+=1  
    

#automating scraping by using sleep method of time module
if __name__=="__main__":
    count=1  #required no.of times
    call=1
    print("Scraping the Data..!")
    while True:
        fetch_data()
        if call<count:
            call+=1
            time_wait=10    #waiting time
            print(f"Waiting {time_wait} Seconds")
            time.sleep(time_wait)
            print("Scraping the Data Again...!")    
        else:
            print("Scraping Completed..!")
            break
    '''
    str=input("Enter a mobile/laptop brand to search:")
    print(f"The following are {str} Brand Gadgets with price:")
    for i,j in zip(descriptions,prices):
            if i.startswith(str):
                print(i+"--->"+j)
    '''
        

#continuation of scraping based on user command 
'''
response=input("T/F:")
if response.upper()=="T":
    print("scraping the data again..!")
    continue
else:
    print("Scraping Completed..!")
    break
'''

           

                
            