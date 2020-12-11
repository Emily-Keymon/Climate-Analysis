# Climate Analysis
The goal of this project was to use Python and SQLAlchemy to do basic climate analysis and data exploration of a dataset. The data was contained in a SQLite database.  All of analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
## Tools Used
* Python - Pandas, Numpy, Matplotlib, SQLAlchemy
## Tasks
### Climate analysis
1.  Connected to sqlite database using SQLAlchemy create_engine.
2.  Used SQLAlchemy automap_base() to reflect tables into classes and saved a reference to those classes called Station and Measurement.
### Precipitation analysis
1.  Designed a query to retrieve the last 12 months of precipitation data.
2.  Queried the date and prcp values.
3.  Loaded the query results into a Pandas DataFrame and set the index to the date column.  
4.  Sorted dataframe values by date.
5.  Plotted results using the .plot method.
6.  Use Pandas to print the summary statistics for the precipitation data.
### Station Analysis
1.  Designed a query to calculate the total number of stations.
2.  Designed a query to find the most active stations.
3.  Listed stations and observation counts in descending order.
3.  Determined which station had the highest number of observations.
### Temperature Analysis
1.  Designed a query to retrieve the last 12 months of temperature observation data (TOBS).
2.  Filtered by the station with the highest number of observations.
3.  Plotted the results as a histogram with `bins=12`.
### Climate App
1.  Designed a Flask API based on the queries developed.
2.  Used Flask to create routes.
### 

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Hints

* You will need to join the station and measurement tables for some of the queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

- - -

## Bonus: Other Recommended Analyses

* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).

### Daily Rainfall Average

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.

