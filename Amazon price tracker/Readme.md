# Amazon Price Tracker

A Python-based project to monitor Amazon product prices, store historical price data, and notify users via email when prices drop below a specified threshold. This tool is ideal for users wanting to automate price tracking for items they wish to purchase at a discount.

## Used Tools
- **Python**: Core programming language for implementing functionality.
- **BeautifulSoup**: Web scraping to retrieve product price data from Amazon.
- **MySQL**: Database storage to maintain historical price records.
- **SMTP**: Email notifications to alert users when a price drop is detected.
- **dotenv**: Environment variable management for secure storage of sensitive credentials.

## Description
The Amazon Price Tracker uses web scraping to monitor the price of an Amazon item daily. It automatically records the price, stores it in a MySQL database for historical tracking, and sends an email alert to the user when the price drops below a predefined threshold.

## Key Features
- **Daily Price Monitoring**: Scrapes Amazon product prices regularly and stores them for historical analysis.
- **Email Alerts**: Sends automatic email notifications to users when prices fall below a target value.
- **Historical Data Logging**: Logs each price update in both a MySQL database and a CSV file for future analysis.
- **Environment Security**: Utilizes environment variables to securely handle sensitive information, such as email credentials and database login details.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/amazon-price-tracker.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your `.env` file to securely store sensitive information:
    ```plaintext
    PASSWORD=your_email_password
    EMAIL=your_email@example.com
    WORKBENCH_USERNAME=your_mysql_username
    WORKBENCH_PASSWORD=your_mysql_password
    ```

## Usage

1. Update the `item_url`, `item_name`, and `threshold_price` variables in the script with the product URL, name, and price threshold.
2. Run the script:
    ```bash
    python amazon_price_tracker.py
    ```
3. The script will:
   - Scrape the current product price from Amazon.
   - Store the price in the MySQL database and CSV file.
   - Send an email notification if the price falls below the threshold.

## Schema Setup
To create the MySQL table for storing prices, you can use the following SQL command:
```sql
CREATE TABLE IF NOT EXISTS price_tracking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255),
    price FLOAT,
    currency VARCHAR(5),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
