# python-challenge
<!-- Python script to analyze data and provide financial analysis -->
<h>_**SUMMARY**_</h>

Completed two python scripts for analyzing specific data. _**File one**_ was comprised of financial data for an un-named company. _**File two**_ was comprised of polling data for an un-named county election.

<h>_**DETAIL**_</h>

_PyBank_
In this script I imported my .csv file and read the data into multiple lists: Dates, Profit Loss. After getting the data into lists I started to create my analysis summary. Analysis included:
- Total number of months being analyzed.
- Total net amount of profit/loss. Achieved this value by using the sum function and applying it to the values in the profit loss columns.
- Average change of profit/loss across the whole duration.
This was achieved by looping through my data and subtracting the value in the profit loss from the same value in the row below it. 
- Greatest Increase in profits. Achieved this by storing the above values into a new list.

_PyPoll_
