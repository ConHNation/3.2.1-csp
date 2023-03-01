# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plotm
import pandas as csvm

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
temp_data = csvm.read_csv("temperature_data.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
plotm.plot(temp_data['Year'], temp_data['Anomaly'], color='gray')

# TODO #3: Plot LOWESS in a line graph

# Line 17 borrowed from nerdsfornerds.com, because idk how to add multiple graphs into one
plotm.plot(temp_data['Year'], temp_data['LOWESS'], color='blue')
plotm.ylabel('Temp Anomalies (Celcius)')
plotm.xlabel('Years')
plotm.title('Change in Temp')
plotm.show()

# TODO #4: Use matplotlib to make a bar chart
plotm.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plotm.ylabel('Temperature Anomalies in Celsius')
plotm.xlabel('Years')
plotm.title('Change in Temperatures')
plotm.show()

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0
for i in range(len(temp_data['Anomaly'])):
    if (temp_data['Anomaly'][i] < min_anomaly):
        min_anomaly = temp_data['Anomaly'][i]
        min_year = temp_data['Year'][i]
    elif (temp_data['Anomaly'][i] > max_anomaly):
        max_anomaly = temp_data['Anomaly'][i]
        max_year = temp_data['Year'][i]
    sum_anomaly += temp_data['Anomaly'][i]
    avg_anomaly = sum_anomaly/len(temp_data['Anomaly'])
print("The maximum anomaly is:", max_anomaly, "which occured in", max_year)
print("The minimum anomaly is:", min_anomaly, "which occured in", min_year)
print(f"The average anomaly is: {round(avg_anomaly,4)}")