# wahap-csv-to-sql
ETL from CSVs to SQL

# Background
Wahapedia provides CSV extracts of the data used to produce their content. This tool is intended to extract the content from the CSV files provided by Wahapedia and transform it into SQL for subsequent loading.

# Road Map
The initial goal is to create a command line tool that starts from pre-downloaded files and produces a sqlite loading script with a direct port of the schema.

Follow on versions may:
 * perform data retrieval
 * transform HTML to Markdown
 * target other data storage tools
 * explore a richer schema
 
Initial Target will be SQLite3.
