# MIS581

## Introduction
Capstone project for MS in Data Analytics. The goal of this project is to ask a research question related to an organization and then use software to conduct statistical testing. 

## The target organization
The Electric Reliability Council of Texas, Inc. (ERCOT) is an American organization that operates Texas's electrical grid, the Texas Interconnection, which supplies power to more than 25 million Texas customers and represents 90 percent of the state's electric load. 

## The research question 
Is there a difference in forced unplanned outages between seasons (caused by weather events).

## The dataset
Request to ERCOT returned less than a years worth of historical records.

## The data pipeline
1. collect 289 Excel documents from ERCOT historical data request
2. convert Excel documents into a series of dataframes, sorted from date published
3. merged dataframes into one dataframe
4. export dataframe into a CSV file
5. import CSV file into as data frame for data analysis (or use it in other analytical software like Excel)
6. conduct data analysis and statistical tests

## Limitations
Less than a years worth of data was availabe from ERCOT on data related to unplanned outages. Thus, pseudo-random data was generated based of the given data in an inductive reasoning approach. The solutoin used in this project uses the amount of outages for each month as the mean for creating gaussian distribution with 3 standard deviations. For months that do not have an outages, like the spring seasons, the one month that has a outage is used for all other month's means. 

## Methods
Using the pseudo-random generated data does not account for variance in the distribution but we can use the orginal data as a basis for the mean. 30 samples were created for each month to create a gaussian distribuition, as per the central limit theorem. Then the amonut of outages from each season are combined. I used the Welch’s ANOVA test was used instead because the requirements of variance was relaxed but normality was still assumed. 

## Results
The results of the test show that we have p-value of 3.58e-17 which is way smaller than the alpha of 0.05. Now the null hypothesis is rejected. Using this inductive approach of using the theory that pseudo-randomly generated data can be used as a pattern for real world observations then the null hypothesis can be rejected. Thus, there is a statistical difference of outages between seasons.

## Recommendations
Data transparency and data accessibility are key elements in improving ERCOT’s data policies. By taking greater responsibility and possession of energy resource related data they can focus on making this data more accessible to the public. Creating a data warehouse for public consumption would allow researchers to better investigate ERCOT and its related energy resources. Further upstanding is needed for predicting power outages caused by weather related events.

