# Salaries Exploration with Pandas
In this GitHub Repository you can find Day 71 of 100 Days of Code from [Dr. Angela Yu](https://github.com/angelabauer) and [The London App Brewery](https://github.com/londonappbrewery). On this day the challenge was to explore salaries by College Majors. The data is originally from [PayScale](https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors).


## Scrape new data
Additionally you can find a scrape.py file that scrapes the current College Salary Report (updated for 2021) from PayScale's website and outputs the new data in to the new .csv file. The new report contains more than 800 different majors, the degree type is solely "Bachelors".
As you can see, I have used selenium for scraping the new data. For now, I have left out the last column "% High Meaning". If you wish to add it to your .csv file to also analyze the meaning alumnis think their job has, just add it in the script.
Unfortunately, the new data does not contain a "Group" column anymore.


## Requirements

