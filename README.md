# arxiv-scraping README.md


* before running min.py install the application dependencies by running:
```> pip install -r requirements.txt``` 

* It is also necessary to insert the following keys into a .env-file
OPENAI_API_KEY=
SERPAPI_API_KEY=
PINECONE_API_KEY=
PINECONE_ENVIRONMENT=


* This code will scrape article information from arxiv.org into a JSON file:
  title, pdf_url, entry_id, date published and a summary of the full article

* The arxiv category can be set on the command line
  default 'physics-hist-ph' 

* the maximum number of articles scraped can also be set on the command line
  default is 10

* for each article a file is written in './data/category/title.txt



* to run:
workspace> python main.py
