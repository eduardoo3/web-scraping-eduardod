# X (Twitter) Web Scraping with Python

## Project Description

This project was developed as part of a course activity to perform **data collection (Web Scraping)** from posts on X (Twitter) using Python.

The script automatically accesses a user profile, collects information from the posts, and saves the data into a **structured CSV file**, which can be opened in Excel or used for data analysis.

Profile used for data collection:
https://x.com/TechDrop_News

## Technologies Used

* Python
* Playwright (browser automation)
* Pandas (data organization and export)
* Asyncio (asynchronous execution)

## Collected Information

The script extracts the following information from each post:

* Post author
* Post text (description)
* Post date
* Post URL
* Number of likes
* Number of reposts
* Number of replies
* Number of views
* Media type (image, video, or none)

These data are stored and then exported to a `.csv` file.

## How the Script Works

The program:

1. Automatically opens a browser using Playwright
2. Accesses the profile defined in the code
3. Scrolls the page to load more posts
4. Locates the HTML elements of the posts
5. Extracts the information from each post
6. Stores the collected data in a list
7. Converts the data into a Pandas DataFrame
8. Saves the data into a CSV file

Before saving, the script also removes **duplicate posts**.

## Generated File

After running the script, a folder called:

`saidas_scrapings`

is created.

Inside this folder the file is generated:

`relatorio_techdrop_limpo.csv`

## Note

The number of collected posts can be changed by modifying the variable:

`QUANTIDADE_SCROLLS`

## Author
# X (Twitter) Web Scraping with Python

## Project Description

This project was developed as part of a course activity to perform **data collection (Web Scraping)** from posts on X (Twitter) using Python.

The script automatically accesses a user profile, collects information from the posts, and saves the data into a **structured CSV file**, which can be opened in Excel or used for data analysis.

Profile used for data collection:
https://x.com/TechDrop_News

## Technologies Used

* Python
* Playwright (browser automation)
* Pandas (data organization and export)
* Asyncio (asynchronous execution)

## Collected Information

The script extracts the following information from each post:

* Post author
* Post text (description)
* Post date
* Post URL
* Number of likes
* Number of reposts
* Number of replies
* Number of views
* Media type (image, video, or none)

These data are stored and then exported to a `.csv` file.

## How the Script Works

The program:

1. Automatically opens a browser using Playwright
2. Accesses the profile defined in the code
3. Scrolls the page to load more posts
4. Locates the HTML elements of the posts
5. Extracts the information from each post
6. Stores the collected data in a list
7. Converts the data into a Pandas DataFrame
8. Saves the data into a CSV file

Before saving, the script also removes **duplicate posts**.

## Generated File

After running the script, a folder called:

`saidas_scrapings`

is created.

Inside this folder the file is generated:

`relatorio_techdrop_limpo.csv`

## Note

The number of collected posts can be changed by modifying the variable:

`QUANTIDADE_SCROLLS`

## Author

Project developed by a **Computer Science student** as a practical activity on web scrping using python.
