

# Lobbying Data Analysis for Stock Movement

## Introduction

This project aims to explore the relationship between lobbying activities of companies and their stocks' price movements. We utilize data from the Lobbying Disclosure Act API to gather lobbying expenditure information, publicly available SEC data for company total assets, and Yahoo Finance for historical stock prices.

## Data Sources

1. **Lobbying Disclosure Act API**: This API provides data on lobbying expenditures by various organizations in the United States. We use it to gather information on lobbying expenses incurred by specific companies. The data was originally extracted by Rahul Krishna.

2. **SEC Filings**: We extract data on a company's total assets from publicly available filings with the U.S. Securities and Exchange Commission (SEC). This information gives us insights into the financial health and scale of the company. 

3. **Yahoo Finance**: We utilize the Yahoo Finance API to retrieve historical stock price data for the companies under analysis. This data is crucial for understanding the movement of stock prices over time.

4. **OpenSecrets Lobbying Data**: We webscraped the OpenSecrets lobbying data to obtain an alternative lobbying dataset to cross-check with the raw data obtained from the Lobbying Disclosure Act API.

## Methodology

1. **Data Collection**: We gather lobbying expenditure data, company total assets, and historical stock prices for the selected companies using the respective APIs and publicly available sources.

2. **Data Cleaning and Preparation**: The collected data undergoes cleaning and preprocessing to handle missing values, format inconsistencies, and ensure compatibility for analysis.

3. **Correlation Analysis**: We perform statistical analysis to explore any potential correlations between lobbying expenditure, company total assets, and stock price movements.

4. **Modelling**: Based on the insights gained from the correlation analysis, we may develop predictive models to forecast stock price movements based on lobbying activities and other factors.

## Usage

1. **Data Collection**: Run scripts to collect data from the Lobbying Disclosure Act API, SEC filings, and Yahoo Finance API.

2. **Data Processing**: Execute analysis scripts to clean, preprocess, and analyze the collected data.

3. **Data Modeling**: Utilize visualization scripts to create charts and graphs to visualize the relationships between lobbying expenditure, company assets, and stock prices.

## Main Dependencies

- Python 3
- Requests library (for API requests)
- Pandas library (for data manipulation)
- Matplotlib and Seaborn (for data visualization)
- yfinance (for stock data)

## Contributors

- [Edward Ramirez](https://github.com/yourusername)
- [Nicolas Jaramillo Torres](https://github.com/nicoj13)
- [Yong Cui](https://github.com/Itamik)
- [Cara D'Alesio](https://github.com/cara-dalesio)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to OpenSecrets for providing access to the OpenSecrets API.
- Special thanks to [Adam Getbags](https://github.com/AdamGetbags) for providing code for extracting the SEC Assets Data. 
- Thanks to Yahoo Finance for providing historical stock price data.
- We acknowledge the US Senate for making Lobbying Disclosure reports publicly available.
- We acknowledge the SEC for making company filings publicly available. 


# To Do (for project completion)
* Complete modelling and collect results

* Complete all assignments (reports) 
    - Data gathering and defining stakeholders + KPIs (I made a bullet-point version in the `notes` directory)
    - Data analysis and visualizations 
    - Modelling proposal
    - List of success and pitfalls of modelling approach (with visualizations and metrics)

* Organize the GitHub with the following directory structure
    - `data`: Contains final versions of the data
    - `data_processing`: Contains data that is used for processing
    - `notebooks`: Contains important results (visualizations, statistics, modelling, etc.)
    - `notes`: Contains reports and meeting notes
    - `junk`: Contains old or irrelevant files (may be deleted before submission)
    - `utils`: Contains useful modules or files  

    The only file in the main page should be the slides.

* (Optional) Make a README file that summarizes the project and results well

* Make slides and make a video recording of presentation

## Remove API Key History before Making Repo Public
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
