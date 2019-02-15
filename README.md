# Denver Crime Data
Exploring denver crime data from the denvergov opendata platform

## Table of Contents
1. [Dataset](#dataset-crime)
2. [Initial Exploration](#initial-exploration)
    * [Is crime?](#is-crime)
    * [Length of crimes](#length-of-time-between-first-and-last-occurrence)
    * [Missing locations and sexual assault](#-missing-locations-and-sexual-assault)
3. [EDA](#exploratory-data-analysis)
    * [Most frequent crimes](#most-frequent-crimes)
    * [Crimes by district](#crimes-by-district)
    * [Crime over time](#crime-over-time)
4. [Changes Over Years](#changes-over-years)
5. [Extras](#extras)
    * [Future Explorations](#future-explorations)
    * [Data artifacts](#data-artifacts)


## Dataset: Crime
Last updated 2/11/2019, [updated dataset](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime)

### Description
This dataset includes criminal offenses in the City and County of Denver for the previous five calendar years plus the current year to date. The data is based on the National Incident Based Reporting System (NIBRS) which includes all victims of person crimes and all crimes within an incident. The data is dynamic, which allows for additions, deletions and/or modifications at any time, resulting in more accurate information in the database. Due to continuous data entry, the number of records in subsequent extractions are subject to change. Crime data is updated Monday through Friday.

### Disclaimer
The information provided here regarding public safety in Denver are offered as a courtesy by the City and County of Denver. By downloading this data, you acknowledge that you have read and understand the Disclaimer below and agree to be bound by it. Certain information is omitted, in accordance with legal requirements and as described more fully in this Disclaimer.

All materials contained on this site are distributed and transmitted "as is," without any representation as to completeness or accuracy and without warranty or guarantee of any kind. The City and County of Denver is not responsible for any error or omission on this site or for the use or interpretation of the results of any research conducted here.

### About Crime Data
The Denver Police Department strives to make crime data as accurate as possible, but there is no avoiding the introduction of errors into this process, which relies on data furnished by many people and that cannot always be verified. Data on this site are updated Monday through Friday, adding new incidents and updating existing data with information gathered through the investigative process.

Not surprisingly, crime data become more accurate over time, as new incidents are reported and more information comes to light during investigations.

Crimes that occurred at least 30 days ago tend to be the most accurate, although records are returned for incidents that happened yesterday. This dynamic nature of crime data means that content provided here today will probably differ from content provided a week from now. Likewise, content provided on this site will probably differ somewhat from crime statistics published elsewhere by the City and County of Denver, even though they draw from the same database.

### Withheld Data
In accordance with legal restrictions against identifying sexual assault and child abuse victims and juvenile perpetrators, victims, and witnesses of certain crimes, this site includes the following precautionary measures: (a) Addresses of sexual assaults are not included. (b) Child abuse cases, and other crimes which by their nature involve juveniles, or which the reports indicate involve juveniles as victims, suspects, or witnesses, are not reported at all.

Crimes that are initially reported, but that are later determined not to have occurred, are called "unfounded" offenses. These incidents are excluded once they have been designated as unfounded.

### About Crime Locations
Crime locations reflect the approximate locations of crimes but are not mapped to actual property parcels. Certain crimes may not appear on maps if there is insufficient detail to establish a specific, mappable location.



## Initial Exploration
There are 19 columns. Last occurrence date has the most null values (314268) possibly due to incomplete reporting or cases waiting to be updated or that the incident only happened once (we'll explore this a little further). Incident address has 45223 null values, of which some amount are sexual assaults since locations for these are not reported, and some may just not have a parcel address. There are 3739 null-valued GIS (GEO_X, GEO_Y, GEO_LON, GEO_LAT) entries which, again, should be inclusive of sexual assaults as their locations are not reported. All other coulmns are non-null for all entries. Great! There is little data cleaning needed for this dataset.

### Is crime?
The column IS_CRIME is a categorical whether or not the incident is a crime. There are 119,666 incidents that are categorized as not crimes. From the code book these codes are traffic accidents including hit-and-run, and general traffic accidents. Removing these entries we a are left with 340193 crimes to explore.

### Length of time between first and last occurrence
Looking at the time between first and last occurrence shows that most of the incidents cover short time periods. About half of the incidents do not have a last occurrence date which could be interpreted as being singular events, however, more clarification with Denver police on reporting procedures is suggested. The other half of the entries that do have a last occurrence date have a rather large spread with 25th percentile being 22 minutes long, 50th percentile lasting 6 hours, and 75th percentile lasting 15.5 hours. There are a 39 entries that likely have incorrect dates recorded as the last occurrence date is before the first occurrence date. The longest lasting incident reported was a sexual assault that continued over a four year period.

|Percentile|         TIME DELTA    |
|     ----:|:---                   |
|min       |      -1 days +04.00.00|
|25%       |        0 days 00.22.00|
|50%       |        0 days 06.00.00|
|75%       |        0 days 15.30.00|
|max       |     1609 days 23.00.00|


### Missing locations and sexual assault
There are 3,739 entries that do not have locations included, all of which are sexual assault crimes. Not all sexual crime codes were contained within the null-valued location offenses but all sexual assault codes were. No sexual assaults have locations included. However, locations for sexual harassment and sex offenders failing to register are present in the database.



## Exploratory Data Analysis
### Most frequent crimes
There are 195 different types of offense represented in the dataset that are part of 14 different categories. The most prevalent category over all the years is a miscellaneous category called _all-other-crimes_ which is in turn dominated by _criminal tresspassing_ and _other traffic_ violations that are criminal. _Public disorder_ and _larceny_ are the next most prevalent followed by _theft from motor vehicle_.

![Crime by category][crime cate]

### Crimes by district
We can break down the amount of crime in each category by district. There are seven police districts in Denver. District 6 is downtown where we see the drug and alcohol, larceny, and public disorder crimes being committed. District 3 covers the southern part of I-25 down to the Tech Center and including Cherry Creek. Here we see high public disorder, larceny, burglary, motor vehicle theft, and in general lots of stealing going on here.

![Police district map][distric map]

District 7 is barely registering in crime counts compared to the other districts and this makes sense due to its location around the airport and how much open space it encompasses. One interesting category that District 7 does come closer to the other districts is white collar crime.

![Crimes by district][district crime]


The offense type table (tuncated) highlights some of the offense types represented in the _all-other-crimes_ category.

|OFFENSE TYPE ID                 |   Count|
|                            ---:|:---|
|accessory-conspiracy-to-crime   |    136|
|agg-aslt-police-weapon          |    293|
|animal-cruelty-to               |    125|
|criminal-trespassing            |  13989|
|...                             |  ...|
|disarming-a-peace-officer       |     27|
|public-fighting                 |    852|
|public-order-crimes-other       |   7489|
|...                             |  ...|
|reckless-endangerment           |    149|
|traf-habitual-offender          |   3581|
|traf-other                      |  30968|
|...                             |   ...|
|vehicular-eluding-no-chase      |   3409|
|violation-of-court-order        |   2513|
|violation-of-restraining-order  |   2780|
|weapon-by-prev-offender-powpo   |   1379|


### Crime over time
Plotting daily incident counts for all the years up through 2018 a fairly regular cyclical pattern emerges. Incidents start lower, rise through the spring, peak in the summer, and decline in the fall and winter. It would be interesting to compare temperature changes to crime rates as this cyclical trend suggests similar timescale as seasonal weather changes. An exponential weighted average helps to visualize the trends through the noisy peaks and valleys in the data.

![Crime over Time][daily alltime]

It would be interesting to also insert markers of any major events, holidays, etc. Further analysis of the dates of the spikes and dips would be interesting as well. Likely that the correlate to specific events. Generally, there looks to be a subtle trend of increasing crime.

## Changes Over Years
This dataset had 5 years of data plus data from the current year up to the date it was downloaded (2/11 in this case). Lets look at incidents by month, separating out the years. There is a clear cyclical pattern in the data. Incidents decrease to their low count in February and gradually increase over the year peaking in August. From there they decrease again as the year closes out. From the figure (_Crimes per Month_) The years look fairly similar, however, 2014 does look a bit lower than the rest.

![Crime over years][crime years]

Using a two-tailed hypothesis test with an overall significance level of 0.05, the average crimes per month for each year is compared. From the monthly comparisons table we see, indeed there is evidence that 2014 is significantly different than the rest of the years. Also, all the other years likely, do not differ significantly. This suggest that total crime increased from 2014 to 2015 but has stayed the same since 2015.

**Monthly Comparison**

|test  |       t   |      p   |  Reject Null  |
|  ---:|:  ---    :|:  ---   :|: ---          |
|2014-2015| -4.15     | 0.001    |        True |
|2014-2016| -3.83     | 0.002    |        True |
|2014-2017| -6.52     | 0.000    |        True |
|2014-2018| -5.41     | 0.000    |        True |
|2015-2016| -1.45     | 0.173    |       False |
|2015-2017| -3.23     | 0.007    |       False |
|2015-2018| -3.25     | 0.007    |       False |
|2016-2017| -1.33     | 0.210    |       False |
|2016-2018| -1.44     | 0.175    |       False |
|2017-2018| -0.00     | 0.997    |       False |


Average daily crimes per year are also compared. Again we see evidence that 2014 is significantly different from the other years. Interestingly, there is also evidence that average daily crime is significantly lower in 2015 vs 2017 and 2018. This suggests that the total daily crime increased in between 2015 and 2017. These comparisons do not take into account population which if there was a population increase could account for an increase in crime.

**Daily Comparison**

|test   |        t  |       p    | Reject Null |
|      ---:|:  ---    :|:  ---     :|: ---     |
|2014-2015 | -6.50     | 2.51e-10   |      True|
|2014-2016 | -7.99     | 1.78e-14   |      True|
|2014-2017 |-11.92     | 6.63e-28   |      True|
|2014-2018 |-11.49     | 2.74e-26   |      True|
|2015-2016 | -2.21     | 2.76e-02   |     False|
|2015-2017 | -4.94     | 1.17e-06   |      True|
|2015-2018 | -4.71     | 3.37e-06   |      True|
|2016-2017 | -2.36     | 1.85e-02   |     False|
|2016-2018 | -2.22     | 2.63e-02   |     False|
|2017-2018 | -0.00     | 9.97e-01   |     False|




## Extras
### Future Explorations
Looking at the normalized hourly sum of crime categories reveals some interesting trends. White collar crime spikes at 8:00 and 12:00, public disorder spikes between 15:00 and 17:00. Most other crimes reach their highest peaks late in the night. Further investigation into the time-dependence of different crimes would be very interesting.

![hour norm][cate hour norm]

Analyzing day of the week  is one are that hasn't been looked at in this analysis and should warrant an investigation. I would expect white collar crimes to be more prevalent during the work week while drug and alcohol crimes more prevalent at the end of the week and on weekends. Adding other datasets to this one could produce more insights and better comparisons such as population, income, demographics, and land area statistics to compare crime rates per capita against other socioeconomic conditions and potentially gain further insight into what statistics relate to eachother.




### Data artifacts
Initial exploration of of incident counts bout time revealed artifacts in the data possibly related to how the data gets recorded and rounded by some but not all entries. The cyclical nature of this results suggests a regular pattern due to how the data is recorded as it is unlikely that this pattern would represent how incidents are actually taking place.

![time artifact][time artifacts]



[crime cate]: images/tot_crime_categ.jpg
[district map]: images/*
[bad district crime]: images/dist_crime_by_type.jpg
[district crime]: images/crime_categ_dist.jpg
[crime years]: images/crime_year.jpg
[month prop]: images/crime_month_prop.jpg
[daily alltime]: images/crime_daily_alltime.jpg
[crime time]: images/crime_time_day.jpg
[cate hour]: images/crime_cate_hour.jpg
[cate hour norm]: images/crime_cate_hour_norm.jpg
[time artifacts]: images/time_artifacts.png
