03/16/2024: Initial LDA Analysis

Useful Links:
	Explanation of OpenSecrets Data: https://www.opensecrets.org/federal-lobbying/methodology
	Lobbying Disclosure File Instructions: https://www.senate.gov/reference/resources/pdf/LD2_Instructions.pdf
	LDA Senate Database: https://lda.senate.gov/filings/public/filing/search/ [rahul got files from the API]
	
Results
	1. Able to extract the data easily
	2. Performed some preprocessing for ease-of-use, may need some more cleaning
	3. dt_posted is somewhat arbitrary, but may be thought of as date that traders
	may be aware of lobbying activity
	4. Possible that lobbying registrants report activity before companies; 
	comparison of "expenses / income" histograms indicate that companies scatter
	their lobbying to different companies
	5. A lot of categories and companies lobby for different things. Example: 
	pfizer put 
	
Important Features:
	1. lobbying_activities (list of dictionaries containing different pieces of lobbying)
		a. general_issue_code: code categorizing lobbying activity
		b. description: brief description of activity, may be useful for keyword search
	2. 
	
Possible To Do:
	1. Combine datasets from different quarters (since disclosures are posted after quarter)
	2. Like OpenSecrets, may need to update disclosures with amended / terminated data carefully

Finding Correlations Between Lobbying and Market Movement:

	Lobbying at Quarter vs Future Price Movement:
		Pro: 
			* Lobbying in this quarter will more directly affect the price of a stock
		Issue: 
			* How to measure "long-term" price movement as a function of lobbying?
			* Useful only if the date that the activity was posted is near enough the quarter (see issue below)
		
	Lobbying at "dt_posted" vs price around "dt_posted"
		Issue: 
			* Past lobbying (e.g., 2021 Q4) might be reported in the future (e.g., dt_posted.year = 2024)
		
	Finding Correlation Between Lobbying Activity and Price Movement:
		* I.e., did more lobbying help to increase price? 
		* Difficult to disentangle this and other factors in longer time scales
		
	Causal Impact of "Events" on Time Series Data
		https://stats.stackexchange.com/questions/590916/testing-the-impact-of-a-events-on-time-series 
		
		provides a measure of impact of event ; i wonder if it can be used to predict the effect of future such events
		
Predicting Politician Trades from Lobbying:
	Use lobbying in one quarter to predict trading activity in the next quarter
	Difficult