from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os
import re
import mysql.connector
import datetime
from csv import writer
#import pandas as pd

# Setting the env secrets for more security
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
email = os.getenv("email")

# Setting headers you can access your headers from --> https://myhttpheader.com
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

# Defining the price threshold, currency and the item details (name, link) from Amazon
currency = "EGP"
threshold_price = 60000
item_name = "IPhone 16 pro max"
item_url = "https://www.amazon.eg/-/en/Apple-iPhone-Pro-Max-256/dp/B0DGJKQ3KW/ref=sr_1_5?crid=1VUCLJ2UY734G&dib=eyJ2IjoiMSJ9.7664QGFdYzMd1EclJ1MGt_Z2OtycCawNBf2OQxmrbofZjFLPN8zJFTIiLT5HbybtFw86nD_lZXZUWAhOy0qfvt8YDq4DJAi2WPMHatwSG02b1HeZWH389l_ynvxZPQryLJ8Purrb0z_ZSNRMV5oEnvEpAWPTpa2_-9NG9ByIyPDtBVmNl54X_-0wtJ93_8ZlxvKJiPJFmi6pf-iXEsrZMKXJqbsfMPQeZscCFx3vhnGRwZMxAAgSx2gKMt9CBDqA7YBbtcWQvD4eImoJlRh7rOx7phTfJ-9bpKaW06tN2_8.YENOGcJKjnsrIjxao2i6ignWxTlGwYexZjkKHINLN5g&dib_tag=se&keywords=iphone+16+pro+max&qid=1729768125&sprefix=iphone+%2Caps%2C231&sr=8-5"

# Establish a connection with the Amazon server and scraping its data
response = requests.get(item_url, headers=header)
soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())

# Getting the desired data from the website
price_whole = (soup.find("span",class_="a-price-whole")).getText()
price_whole = (re.sub(r',','',price_whole)).split(".")[0]
price_decimal = soup.find("span",class_="a-price-decimal")
price_fraction = soup.find("span",class_="a-price-fraction")
whole_price = float(price_whole+price_decimal.getText()+price_fraction.getText())

# Establish a connection with mysql workbench for accessing/storing the database
mydb = mysql.connector.connect(
    user=os.getenv("workbench_username"),
    password=os.getenv("workbench_password"),
    host='127.0.0.1',
    database='price_database'
)
mycursor = mydb.cursor()

### Create the price_tracking schema for the first time
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS price_tracking (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     item_name VARCHAR(255),
#     price FLOAT,
#     currency VARCHAR(5),
#     date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)
### Creating the CSV file for th first time *don't forget to uncomment the import pandas statement above*
# df = pd.DataFrame(columns=['item_name', 'price', 'currency', 'date'])
# print(df)
# df.to_csv(csv_file,index=False)


# inserting the rows in the schema for storing the price for each day
insert_query = "INSERT INTO price_tracking (item_name, price, currency) VALUES (%s, %s, %s)"
mycursor.execute(insert_query, (item_name, whole_price, currency))

# Closing the connection after storing the price for the current day
mydb.commit()
mycursor.close()
mydb.close()


# Appending the new data in a csv file if needed for further analysis
csv_file = "amazon_prices.csv"
data = [f'{item_name}', f'{whole_price}', f'{currency}', f'{datetime.datetime.now()}']
with open("amazon_prices.csv",'a',newline='')as file:
    writer_object = writer(file)
    writer_object.writerow(data)

# Establish an SMTP connection for sending a mail for notifying if the price went down
if whole_price < threshold_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=PASSWORD)
        connection.sendmail(from_addr=email,
                            to_addrs=f"{email}",
                            msg=f"Subject:{item_name} price dropped !\n\nYour desired item's price has dropped below {threshold_price} with a price of {whole_price}{currency}.\nAccess the purchase link on Amazon from here: \n{item_url}")
