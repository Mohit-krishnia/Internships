import pandas as pd

# Read data from 'rawdata.xlsx' file
raw_data = pd.read_excel('rawdata.xlsx')

# Combine 'date' and 'time' columns into a single datetime column
raw_data['datetime'] = pd.to_datetime(raw_data['date']) + pd.to_timedelta(raw_data['time'].astype(str))

# Extract date and hour from 'datetime' column
raw_data['date'] = raw_data['datetime'].dt.date
raw_data['hour'] = raw_data['datetime'].dt.hour

# Calculate datewise total duration for each inside and outside
df_duration = raw_data.groupby(['date', 'location'])['hour'].sum().reset_index()
df_duration.columns = ['date', 'location', 'duration']  # Rename 'hour' to 'duration'

# Calculate datewise number of picking and placing activity done
df_activity = raw_data.groupby(['date', 'activity']).size().reset_index(name='count')

# Pivot the activity dataframe to get separate columns for 'picking' and 'placing'
df_activity_pivoted = df_activity.pivot(index='date', columns='activity', values='count').reset_index()
df_activity_pivoted.columns = ['date', 'placing_count', 'picking_count']

# Merge duration and activity dataframes
result = pd.merge(df_duration, df_activity_pivoted, on='date', how='left')

# Fill NaN values with 0 for cases where there is no picking or placing activity on a particular date
result.fillna(0, inplace=True)

# Save result to an Excel file
result.to_excel('output_result.xlsx', index=False)

# Display success message
print("File 'output_result.xlsx' successfully created.")
