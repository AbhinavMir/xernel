import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime
from google.oauth2 import service_account

# Set up your Google Fit API credentials
credentials = service_account.Credentials.from_service_account_file(
    '~/.abc.json', scopes=['https://www.googleapis.com/auth/fitness.activity.read']
)

# Define the API endpoint to retrieve walking steps data
endpoint = 'https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:estimated_steps/datasets/00000000000000000000000000000000-{}'.format(
    int((datetime.datetime.now() - datetime.timedelta(days=3650)).timestamp()) * 1000000
)

# Make an authenticated API request to fetch the data
response = requests.get(endpoint, headers={'Authorization': f'Bearer {credentials.token}'})
data = response.json()

# Process the data
steps_data = data['point']

# Create a DataFrame
df = pd.DataFrame(steps_data, columns=['startTimeNanos', 'endTimeNanos', 'value'])
df['startTimeNanos'] = pd.to_datetime(df['startTimeNanos'], unit='ns')
df['endTimeNanos'] = pd.to_datetime(df['endTimeNanos'], unit='ns')
df['value'] = df['value'].astype(int)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df['startTimeNanos'], df['value'], label='Walking Steps')
plt.xlabel('Date')
plt.ylabel('Steps')
plt.title('Walking Steps Over the Last Decade')
plt.legend()
plt.grid()
plt.show()
