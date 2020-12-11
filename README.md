# Climate Analysis
The goal of this project was to use Python and SQLAlchemy to do basic climate analysis and data exploration of a dataset. The data was contained in a SQLite database.  All of analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
## Tools Used
* Python - Pandas, Numpy, Matplotlib, SQLAlchemy, Datetime, Flask, Scipy
## Tasks
### Reflect sqlite tables into SQLAlchemy
1.  Connected to sqlite database using SQLAlchemy create_engine.
2.  Used SQLAlchemy automap_base() to reflect tables into classes and saved a reference to those classes called Station and Measurement.
### Precipitation analysis
1.  Designed a query to retrieve last 12 months of precipitation data.
2.  Calculated date one year from last date in data set.
3.  Designed a query to retrieve data and precipitation results
4.  Loaded the query results into a Pandas DataFrame and set the index to the date column.  
5.  Sorted dataframe values by date.
6.  Plotted results using the .plot method.
7.  Use Pandas to print the summary statistics for the precipitation data.
### Station analysis
1.  Designed a query to calculate total number of stations.
2.  Designed a query to find most active stations.
3.  Listed stations and observation counts in descending order.
3.  Determined which station had the highest number of observations.
### Temperature analysis
1.  Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
2.  Filtered by the station with the highest number of observations, then loaded data into datafram
3.  Plotted results as a histogram with `bins=12`.
### Additional temperature analysis
1.  Queried all June and December temperature observations.
2.  Created separate Pandas dataframes from each dataset.
3.  Performed an independent t-test on June and December datasets.
4.  Analyzed t-statistic and p-value.
### Daily average rainfall analysis
1.  Calculated rainfall per weather station using the previous year's matching dates.
2.  Calculated daily normals.
3.  Created a list of dates for your trip.
4.  Use daily_normals function to calculate the normals for each date string and append results to a list.
5.  Loaded list of daily normals into a dataframe and set index to the date.
6.  Plotted daily normals as an area plot.
### Climate app with multiple routes
1.  Designed a Flask API based on the queries developed.
2.  Used Flask to create routes.
### Routes
1.  `/` 
  * Home page
  * List of all routes available.
2.  `/api/v1.0/precipitation`
  * Converted query results to a dictionary using `date` as the key and `prcp` as the value.
  * Returned JSON representation of your dictionary.
3.  `/api/v1.0/stations`
  * Returned JSON list of stations from the dataset.
4.  `/api/v1.0/tobs`
  * Queried dates and temperature observations of the most active station for the last year of data.  
  * Returned a JSON list of temperature observations (TOBS) for the previous year.
5.  `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, calculated `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


### Additional temperature analysis
* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

### Daily rainfall average

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

