# python-challenge
<!-- Python script to analyze data and provide financial analysis -->
<h>_**SUMMARY**_</h></br>
Completed two python scripts for analyzing specific data. _**File one**_ was comprised of financial data for an un-named company. _**File two**_ was comprised of polling data for an un-named county election.

<h>_**DETAIL**_</h></br>
_PyBank_</br>
In this script I imported my .csv file and read the data into multiple lists: Dates and Profit Loss. After getting the data into lists I started to create my analysis summary. </br>

Analysis included:
- Total number of months being analyzed.
- Total net amount of profit/loss. Achieved this value by using the sum function and applying it to the values in the profit loss columns.
- Average change of profit/loss across the whole duration.
This was achieved by looping through my data and subtracting the value in the profit loss from the same value in the row below it. 
- Greatest _**increase**_ in profits. Achieved this by storing the above values into a new list and using the max function to find the highest value in the list.
- Greatest _**decrease**_ in profits. Achieved this by storing the above values into a new list and using the min function to find the lowest value in the list.

The script finishes by writing my analysis to a new csv file.

_PyPoll_</br>
In this script I imported my .csv file and read the data into multiple lists: Voter ID, County, & Candidate. After getting the data into lists I created multiple variables to assist with my analysis. </br>
Variables were: </br>
- **Votes:** provides the total number of votes.
- **Unique:** after importing '_numpy_' I was able to create a variable to give me a list of the unique values in my "Candidate" list.</br>

After establishing those two values I was then able to create variables for each unique candidate vote count and it's percentage of total vote count. 


Analysis included:
- Total number of votes cast.
- Summary table showing each unique candidate, their percent of total votes and corresponding vote count received.
- Winner was chosen by looking at a dictionary I created and using the max function to find the highest vote count and corresponding candidate.

The script finishes by writing my analysis to a new csv file.