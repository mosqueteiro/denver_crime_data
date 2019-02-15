# Denver Crime Data
Exploring denver crime data from the denvergov opendata platform

## Table of Contents
1. [Dataset](#dataset-crime)
2. [Initial Exploration](#initial-exploration)
    * [Is crime?](#is-crime)
    * [Length of crimes](#length-of-time-between-first-and-last-occurrence)
    * [Missing locations and sexual assault](#-missing-locations-and-sexual-assault)
    * [Most Frequent Crimes](#most-frequent-crimes)
3. [EDA](#exploratory-data-analysis)
    * [Most frequent crimes](#most-frequent-crimes)
    * [Crimes by district](#crimes-by-district)
4. [Changes Over Years](#changes-over-years)


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

**table here**


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


## Changes Over Years









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
