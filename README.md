# Zillow-Rental-Search
Python app that scraps the Zillow website and generates a spreadsheet with a list of potential rentals.

We are looking at renting a home in San Francisco with a price lower than 3k/month and with at least one bedroom.

Using Beautiful Soup we are going to scrape all of the relevant content of the website (Zillow) at the URL found in the beginning of the "main.py" file.
We want the price, the address and the URL the card of the listing will link.

After that, we have to parse correctly the prices (removing an "/" or "+") as well as incomplete links (those missing the 'https://www.zillow.com' in front of them)

After the scrapping we are going to use Selenium on a Google Form, to autofill it with the price, address and link of each listing.
One formis filled per listing and once all the responses from the forms are compiled, we will convert them into a spreadsheet.

The spreadsheet resulting from this project can be seen here : https://docs.google.com/spreadsheets/d/1MO2BF_4zJed3gaqfqli4VoG3To7yOmFvM_FJj3MqeFE/edit?resourcekey#gid=1571900326

Two things from this project where I struggled a bit were the use of headers so that my GET request for the Zillow website goes through and the string manipulations for the links,
where at one point I was trying to transform my list into a set then again to list, which had the averse effect of changing the entire order of my list of links, while my list of prices and addresses were fine.



