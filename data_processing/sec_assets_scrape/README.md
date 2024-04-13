Description:
1. Creates dataframe of stocks of US companies in the NASDAQ
2. Data so far: Ticker, Company Name, Industry, Sector, and Total Assets dataframe for each company
    **Sources**:
    * Ticker: NASDAQ CSV (data/nasdaq)
    * Company Name: SEC Data (utils/secAPI-main)
    * Industry, Sector: yfinance 
    * Total Assets: SEC Data (utils/secAPI-main)
3. Filter the data so that all companies in dataframe have Industry, Sector, and Total Assets data

Next Steps:
1. Merge with Lobbying Data
2. Merge with Stock Data