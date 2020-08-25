# gcp_stock_extract

Steps -
1. Create VM in GCP with public IP and service account having permission to -
  a. BigQuery Data Editor -- for table creation access
  b. BigQuery Job User -- for running jobs access
  
2. VM comes with Python3 installed. Install pip package -
   sudo apt-get update
   sudo apt-get install python3-pip
   
3. Next purpose is to create python script to extract hourly Stock data. you have several options. But I was looking for hourly data so used Alpha Vantage
https://blog.quantinsti.com/stock-market-data-analysis-python/
Above link gives all the details on how to generate free API key and sample code.

4. Extracted Data is then dumped into BigQuery-
  a. Create a Dataset
  b. Raw data will be dumped into the table
  c. Raw data will be upserted in the final table to append only new data.
