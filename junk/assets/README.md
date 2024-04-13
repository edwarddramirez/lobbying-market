# Progress
1. Created dataframe of stocks of US companies in the NASDAQ
2. Data so far: Ticker, Company Name, Industry, Sector, and Total Assets dataframe for each company
    * Ticker: NASDAQ CSV (utils/nasdaq)
    * Company Name: SEC Data (utils/secAPI-main)
    * Industry, Sector: yfinance
    * Total Assets: SEC Data (utils/secAPI-main)
3. Filtered the data so that all companies in dataframe have Industry, Sector, and Total Assets data

# To Finalize this Dataset
1. Need to collect financial data from yfinance for each stock
2. Calculate percent change of price of a stock relative to the S&P500
    (Save dataframe of S&P500 using yfinance)