# Logs analysis Report
This is a simple reporting tool done by Python that prints out reports for a newspaper to its analysis articles and authors.


### Installation  ###

1. Clone this repo

```
git clone https://github.com/onemoreahmad/logs-analysis
cd logs-analysis
```

2. Download the database file:

- https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip


3. Import the database after you unzipped it:

```
psql -d news -f newsdata.sql
```

4. Install psycopg2-binary library using pip3 by typing this command:

```
pip3 install psycopg2-binary
```

## Run the script

Run the script by using this command:
```
python3 app.py
```

You should get output similar to the following results:

```
 1- What are the most popular three articles of all time?
 -  Candidate is jerk, alleges rival  -  338647  views
 -  Bears love berries, alleges bear  -  253801  views
 -  Bad things gone, say good people  -  170098  views

2- Who are the most popular article authors of all time?
 -  Ursula La Multa  —  507594  views
 -  Rudolf von Treppenwitz  —  423457  views
 -  Anonymous Contributor  —  170098  views
 -  Markoff Chaney  —  84557  views

3. On which days did more than 1% of requests lead to errors?
 -  2016-07-17  —  2.25  views
```


### Done
That was it!

Please let me know if you get any issue or find any security bugs.

### Author

- Ahmad Alahmadi
- Github: @onemoreahmad
