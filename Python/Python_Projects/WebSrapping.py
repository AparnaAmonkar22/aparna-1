import requests
from bs4 import BeautifulSoup
import pandas

# URL of the website for data web scrapping
url ='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
# print(soup.prettify)

table = soup.find('table', class_='wikitable sortable')
# print(table)

column_names = table.find_all('th')
# print(column_names)

table_columns = [th_name.text.strip() for th_name in column_names]
# print(table_columns)

# Create a data frame
df = pandas.DataFrame(columns = table_columns)
# print(df)

companies_data = table.find_all('tr')
# print(companies_data)

for row in companies_data[1:]:
    row_data = row.find_all('td')
    each_row_data = [data.text.strip() for data in row_data]
    # Append each data to the data frame
    df.loc[len(df)] = each_row_data

    # print(df)

# Convert into CSV file
df.to_csv('Top_100_US_Companies.csv', index=False)

