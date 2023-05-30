import matplotlib.pyplot as plt
import seaborn as sns
import requests
from datetime import datetime

response = requests.get(
    url='https://api.energidataservice.dk/dataset/Elspotprices?limit=60000')

result = response.json()

records = result.get('records', [])

# Sort the records list by HourDK
records.sort(key=lambda x: datetime.strptime(x['HourDK'], '%Y-%m-%dT%H:%M:%S'))

# Group the records by month
records_by_month = {}
for record in records:
    month = datetime.strptime(record['HourDK'], '%Y-%m-%dT%H:%M:%S').strftime('%m')
    if month not in records_by_month:
        records_by_month[month] = []
    records_by_month[month].append(record)

# Calculate the monthly sum of the "SpotPriceDKK" values
monthly_sums = {}
for month, records in records_by_month.items():
    total_spot_price = sum([float(record['SpotPriceDKK']) for record in records])
    monthly_sums[month] = total_spot_price

# Convert the months to strings for Seaborn
months = [month for month in monthly_sums.keys()]
spot_prices = list(monthly_sums.values())

# Create a scatter plot with Seaborn
sns.set_theme(style="darkgrid")
sns.lineplot(x=months, y=spot_prices)

# Set the title and axis labels
plt.subplots_adjust(left=0.22)
plt.title('Monthly sum of spot prices')
plt.xlabel('Months')
plt.ylabel('Sum of spot prices (DKK)')

# Show the plot
plt.show()