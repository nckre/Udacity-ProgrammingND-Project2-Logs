# Project 1: Logs Analysis 
### Udacity Full Stack Web Development ND
_______________________
## Installation
This project makes use of a Linux-based virtual machine (VM), a PostgreSQL database and Python.
In order to run the python script, follow these steps: 
1. Download and extract the .zip file 
2. Bring the virtual machine online (with vagrant up). Then log into it with vagrant ssh.
3. Download the `newsdata.sql` database from this [Link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put the file into your vagrant directory. 
4. Use your shell to `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql` to connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data
5. Run the python file `newsdata.py` to execute the SQL queries 
_______________________
## SQL Queries
The news database includes 3 tables:
1. A table called articles that lists information on articles (e.g. title, teaser) and identifies the author
2. A table called authirs that lists additional information on the authors (e.g. names)
3. A table called log that lists all HTTP queries made to the articles

When the script is run via `python newsdata.py` (or `python3 newsdata.py`), the script makes three SQL queries via the imported `psycopg2` database adapter, w:
* Listing all articles and their respective view counts. This is done by joining the articles and log table on the log path / article slug.
* Listing all authors and the aggregated view counts of all their articles. This is done by joining all three tables and using the author id to sum individual article counts.
* Listing all days in which the percent of 404 requests was larger than 1 percent. This is done by grouping the requests per day and calculating the percentage of 404 of the total requests.
_______________________
## Licence
This project is released under the [MIT Licence](https://spdx.org/licenses/MIT.html)

Copyright (c) 2019 Niklas Restle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.