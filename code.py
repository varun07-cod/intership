from bs4 import BeautifulSoup
import requests
import csv


# Function to scrape Canoo's industry information
def scrape_canoo_industry_info():
    url = 'https://www.canoo.com/'  # Replace 'example.com' with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape industry information
    industry = soup.find('div', class_='description').text.strip()
    size = soup.find('div id', class_= "tabcontent block-card mb-4 summary").text.strip()
    growth_rate = soup.find('tr', class_= "rou").text.strip()
    trends = soup.find('div', class_ = "row sqs-row").text.strip()

    return industry, size, growth_rate, trends


# Function to scrape Canoo's competitors information
def scrape_competitors_info():
    url = 'https://www.cbinsights.com/company/evelozcity/alternatives-competitors'  # Replace 'example.com' with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape competitors information
    competitors_data = []
    competitors = soup.find_all('div', class_ ="CompetitorCard_container__e_eHa")
    for competitor in competitors:
        market_share = competitor.find('div', class_ ="container").text.strip()
        products_services = competitor.find('div', id ='slideshow').text.strip()
        marketing_efforts = competitor.find('div', class_='qmod-quotehead').text.strip()
        competitors_data.append({
            'Market Share': market_share,
            'Products or Services': products_services,
            'Marketing Efforts': marketing_efforts
        })

    return competitors_data


# Function to scrape market trends
def scrape_market_trends():
    url = 'https://stockanalysis.com/stocks/goev/market-cap/'  # Replace 'example.com' with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape market trends
    trends = soup.find('div', class_="rounded border border-gray-300 bg-white p-2.5 dark:border-dark-600 dark:bg-dark-700 xs:p-3").text.strip()

    return trends


# Function to scrape Canoo's financial performance
def scrape_financial_performance():
    url = 'https://investors.canoo.com/news-presentations/press-releases/detail/117/canoo-inc-announces-third-quarter-2023-results'  # Replace 'example.com' with the actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Scrape financial performance
    revenue = soup.find('ul', class_='disc').text.strip()
    profit_margin = soup.find('ul', class_='disc').text.strip() # Assuming this is the profit margin
    expense_structure = soup.find('ul', class_='disc').text.strip() # Assuming this is expense structure

    return revenue, profit_margin, expense_structure


# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Data has been written to {filename}")


if __name__ == '__main__':
    # Scrape data
    canoo_industry_info = scrape_canoo_industry_info()
    competitors_info = scrape_competitors_info()
    market_trends = scrape_market_trends()
    financial_performance = scrape_financial_performance()

    # Write data to CSV files
    write_to_csv([{
        'Industry': canoo_industry_info[0],
        'Size': canoo_industry_info[1],
        'Growth Rate': canoo_industry_info[2],
        'Trends': canoo_industry_info[3],
        'Key Players': canoo_industry_info[4]
    }], 'canoo_industry_info.csv')

    write_to_csv(competitors_info, 'competitors_info.csv')

    write_to_csv([{'Market Trends': market_trends}], 'market_trends.csv')

    write_to_csv([{
        'Revenue': financial_performance[0],
        'Profit Margin': financial_performance[1],
        'Expense Structure': financial_performance[3]
    }], 'financial_performance.csv')
