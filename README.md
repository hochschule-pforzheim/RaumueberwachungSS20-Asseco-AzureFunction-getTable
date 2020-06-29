# RaumueberwachungSS20-Asseco-AzureFunction-getTable

Azure function “getfromtable” 

This function runs whenever an HTTP request is made to its URL. 

Function then makes a GET request to the “Last2” table in Azure Storage, requesting all entities in the table (there must be always 10 entities). The response with all 10 entities is then converted into json object which is then stored in the body of the response of an HTTP request. 
