

# Lobbying Data Analysis for Stock Movement

## Introduction

This project aims to explore the relationship between lobbying activities of companies and their stocks' price movements. We utilize data from the Lobbying Disclosure Act API to gather lobbying expenditure information, publicly available SEC data for company total assets, and Yahoo Finance for historical stock prices.

## Data Sources

1. **Lobbying Disclosure Act API**: This API provides data on lobbying expenditures by various organizations in the United States. We use it to gather information on lobbying expenses incurred by specific companies. The data was originally extracted by [Rahul Krishna](https://github.com/rmkrishn). [Source](https://lda.senate.gov/system/public/)

2. **SEC Filings**: We extract data on a company's total assets from publicly available filings with the U.S. Securities and Exchange Commission (SEC). This information gives us insights into the financial health and scale of the company. [Source](https://www.sec.gov/edgar/search/)

3. **Yahoo Finance**: We utilize the Yahoo Finance API to retrieve historical stock price data for the companies under analysis. This data is crucial for understanding the movement of stock prices over time.[Source](https://github.com/ranaroussi/yfinance)

4. **OpenSecrets Lobbying Data**: We webscraped the OpenSecrets lobbying data to obtain an alternative lobbying dataset to cross-check with the raw data obtained from the Lobbying Disclosure Act API. [Source](https://www.opensecrets.org/federal-lobbying/)

## Methodology

1. **Data Collection**: We gather lobbying expenditure data, company total assets, and historical stock prices for the selected companies using the respective APIs and publicly available sources.

2. **Data Cleaning and Preparation**: The collected data undergoes cleaning and preprocessing to handle missing values, format inconsistencies, and ensure compatibility for analysis.

3. **Correlation Analysis**: We perform statistical analysis to explore any potential correlations between lobbying expenditure, company total assets, and stock price movements. We mainly focus on the *Lobbying Ratio* and the *Relative Market Performance*, as defined in Slide #3 of the main presentation file.

4. **Modelling**: We performed linear regression on the *Lobbying Ratio* and the *Relative Market Performance*. We also built classification models to determine whether or not the *Lobbying Ratio* can be used to infer if a company's stock price movement exceeds that of the S&P 500.

See `presentation.pdf` for more details.

## Usage

1. **Data Collection**: Run scripts to collect data from the Lobbying Disclosure Act API, SEC filings, and Yahoo Finance API.

2. **Data Processing**: Execute analysis scripts to clean, preprocess, and analyze the collected data.

3. **Data Modeling**: Utilize visualization scripts to create charts and graphs to visualize the relationships between lobbying expenditure, company assets, and stock prices.

## Description of Directories

- `data`: Unprocessed and completely processed versions of the data
- `data_processing`: Contains notebooks and intermediate stages of the data 
- `data_modeling`: Contains correlation analysis and modelling attempts
- `notes`: Contains reports and meeting notes
- `junk`: Contains files that may be useful but do not contribute to the main results in the repo
- `utils`: Contains useful modules or files  

**NOTE:** To run the files in the `data/LDA_data` and `data_processing/lobbying_eda` directories, move these directories to the main repo directory. Otherwise, the notebooks inside those directories must be modified to account for the fact that they are not in the main directory.

## Main Dependencies

- Python 3
- Requests library (for API requests)
- Pandas library (for data manipulation)
- Matplotlib and Seaborn (for data visualization)
- yfinance (for stock data)

## Contributors

- [Edward Ramirez](https://github.com/edwarddramirez)
- [Nicolas Jaramillo Torres](https://github.com/nicoj13)
- [Yong Cui](https://github.com/Itamik)
- [Cara D'Alesio](https://github.com/cara-dalesio)

## Acknowledgments

- Special thanks to OpenSecrets for providing access to the OpenSecrets API.
- Special thanks to [Adam Getbags](https://github.com/AdamGetbags) for providing code for extracting the SEC Assets Data. 
- Thanks to Yahoo Finance for providing historical stock price data.
- We acknowledge the US Office of the Senate for making Lobbying Disclosure reports publicly available.
- We acknowledge the SEC for making company filings publicly available. 