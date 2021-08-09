import time
import boto3
import json
import collections
import operator
import datetime
import os

# athena database name
athenaDatabase = 'ghcn'

# S3 constant
S3_QUERY='query-result'
S3_BUCKET ='YOUR_BUCKET_HERE'

# set defaults
DEFAULT_CITIES = "best" # choices are 'list' (returns all cities) or 'best' (returns city with closest temp to target temp)
DEFAULT_TARGET = 230 # Any int that is represented in tenths of celcius
DEFAULT_DATE_HISTORY = 14 # defaults to 14 days from current day in SQL query
DEFAULT_MIN_LOOKBACK = 5
# number of retries
RETRY_COUNT = 15

## override defaults with Environment variables if available
if 'GLUE_DATABASE' in os.environ:
    athenaDatabase = os.environ['GLUE_DATABASE']

if 'S3_QUERY_OUTPUT_LOCATION' in os.environ:
    S3_OUTPUT = os.environ['S3_QUERY_OUTPUT_LOCATION']
else:
    S3_OUTPUT = 's3://' + S3_BUCKET + '/' + S3_QUERY

if 'GHCN_TABLE_NAME' in os.environ:
    GHCN_TABLE_NAME = os.environ['GHCN_TABLE_NAME']
else:
    GHCN_TABLE_NAME = 'ghcntable'

if 'STADIUM_TABLE_NAME' in os.environ:
    STADIUM_TABLE_NAME = os.environ['STADIUM_TABLE_NAME']
else:
    STADIUM_TABLE_NAME = 'stadium'

def lambda_handler(event, context):
    
    try: 
        city = event['queryStringParameters']['cities']
        if ((city != "list") and (city != "best")):
            city = DEFAULT_CITIES
    except: 
        city = DEFAULT_CITIES

    try: 
        target = int(event['queryStringParameters']['target'])
    except:
        target = DEFAULT_TARGET
    
    try: 
        lookbackDays = int(event['queryStringParameters']['days'])
    except: 
        lookbackDays = DEFAULT_DATE_HISTORY
        
    
    if (lookbackDays < DEFAULT_MIN_LOOKBACK):
        lookbackDays = DEFAULT_MIN_LOOKBACK
        
    dateObj = datetime.date.today() - datetime.timedelta(days=lookbackDays)
    queryDate = int(dateObj.strftime('%Y%m%d'))

    # query has hardcoded elements for simplicity of this workshop
    query = f"""SELECT city, avg(CAST(data_value as INTEGER)) as temp FROM "{STADIUM_TABLE_NAME}" as stadium
        INNER JOIN "{GHCN_TABLE_NAME}" as ghcn  ON stadium.station_id = ghcn.id 
        WHERE ghcn.year_date >= '{queryDate}' 
        AND ghcn.element = 'TAVG' 
        GROUP BY city"""
    
    # athena client
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': athenaDatabase
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
        }
    )

    # get query execution id
    query_execution_id = response['QueryExecutionId']
    print(query_execution_id)

    # get execution status
    for i in range(1, 1 + RETRY_COUNT):

        # get query execution
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_status = query_status['QueryExecution']['Status']['State']

        if query_execution_status == 'SUCCEEDED':
            print("STATUS:" + query_execution_status)
            break

        if query_execution_status == 'FAILED':
            raise Exception("STATUS:" + query_execution_status)
        else:
            print("STATUS:" + query_execution_status)
            time.sleep(i)
    else:
        client.stop_query_execution(QueryExecutionId=query_execution_id)
        raise Exception('TIME OVER')

    # get query results
    result = client.get_query_results(QueryExecutionId=query_execution_id)
    
    # Convert the result set into something a bit easier to manage
    i=1
    stations= {}
    
    num_cities =  len(result['ResultSet']['Rows'])
    
    while i < num_cities:
        # Pull out the station city and station avg temp from the json returned from query
        station_city = result['ResultSet']['Rows'][i]['Data'][0]['VarCharValue']
        station_temp = int(float(result['ResultSet']['Rows'][i]['Data'][1]['VarCharValue']))
        
        # the delta from target shows how far (in tenths of a degree) we are from the target temp
        delta_from_target = abs(station_temp - target)
        
        # save it in a new dict. Station[<City Name>] = [ degree delta from target, avg temp of city]
        stations[station_city] = [ delta_from_target, station_temp ] 
        i = i+1
        
    sorted_stations = sorted(stations.items(), key=operator.itemgetter(1))
    stations_dict = collections.OrderedDict(sorted_stations)   
    
    best_city = list(stations_dict)[0]
    
    if (city == "list"):
        return { 
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
            'body': json.dumps(stations_dict)
        }
    elif (city == "best"):
        return_val = { }
        return_val[best_city] =  stations[best_city] 
        return { 
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
            'body': json.dumps(return_val)
        }
    else:
        return { 
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },        
            'body': json.dumps(stations_dict)
        }