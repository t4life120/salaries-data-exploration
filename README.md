# Salaries Exploration with Pandas
In this GitHub Repository you can find Day 71 of 100 Days of Code from [Dr. Angela Yu](https://github.com/angelabauer) and [The London App Brewery](https://github.com/londonappbrewery). On this day the challenge was to explore salaries by College Majors. The data is originally from [PayScale](https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors).


## Scrape new data
Additionally, you can find a `scrape.py` file that scrapes the current College Salary Report (updated for 2021) from PayScale's website and outputs the new data in to the new `.csv` file. The new report contains more than 800 different majors, the degree type is solely "Bachelors".

As you can see, I have used selenium for scraping the new data. For now, I have left out the last column "% High Meaning". If you wish to add it to your `.csv` file to also analyze the meaning alumnis think their job has, just add it in the script.
Unfortunately, the new data does not contain a "Group" column anymore.


## Requirements
If you want to run the `scrape.py` file locally, explore the data further and maybe want to customize it, you will need to checkoff a few requirements:

* Python (Anaconda is best for data exploration)
* Git (if you want to directly clone the repo)
* VsCode (with the jupyter extension)

## Setup
If you have Python/Anaconda, Git and VsCode (including the jupyter extension) installed, we can start to...

...clone the repository and cd into it:
```bash
git clone https://github.com/t4life120/salaries-data-exploration.git
cd salaries-data-exploration
```

...open VsCode:
```bash
code .
```

Anaconda has already a lot of practical python packages installed but we will need to additionally install selenium if you want to scrape the site for yourself.

For that open the bash terminal in VsCode or open your command line and make sure that the conda env is activated:

```bash
pip install selenium
```

After that just run `python scrape.py` and as soon as the scraping is finished, you will have a new `.csv` file with the newest data.

## Use Jupyter Notebook
In the `old_salaries_exploration.ipynb` you can find useful commands and pandas methods that will help you to explore the new data. Make sure you have the Jupyter Notebook extension installed and maybe you have to change to or choose the right python kernel (python conda if you use anaconda). You can `Ctrl+Shft+P`, enter `Python: Select Interpreter` and then choose the right interpreter ('base').