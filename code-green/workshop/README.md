### HAC201
# Code Green:<br>Hacking on Amazon Sustainability Data Initiative datasets

## Workshop

### Duration: 2 hours

This workshop is one of two tracks offered by **Code Green: Hacking on Amazon Sustainability Data Initiative datasets** at re:Invent 2019. If you'd prefer to compete, [check out the hackathon](https://github.com/awslabs/amazon-asdi/tree/master/code-green/hackathon), which will be held concurrently in the same event space.


If you're attendeding re:Invent 2019 and want to participate in either the hackathon or the workshop, you can [register here](https://www.portal.reinvent.awsevents.com/connect/sessionDetail.ww?SESSION_ID=99788&csrftkn=3SUA-ISXO-ZSNY-YOY0-5EJH-E7K8-ASEI-D66U).


In this workshop you will be building a API to learn about working with ASDI datasets and AWS services. The API has a single call, which queries an ASDI dataset ([GHNC-D](https://registry.opendata.aws/noaa-ghcn/)), and returns the most sustainable location for a sporting event. For the purposes of this workshop that means a location that is neither too hot nor too cold. It could be expanded with additional data sources and more sophisticated algorithms to help select the most sustainable location for any kind of event, based on multiple criteria.

This is meant to give you a starting point for exploring sustainability data. Use it to get up and running, then play with the data—what interesting things can you uncover? What other metrics can you look at when determining if a city is the best city for our fictious event? What other ways can you leverage this dataset, and what other data could you use in conjunction with it?

### The Scenario

The year is 2030, and MLD—Major League DeepRacer—has exploded, and is now the most popular sporting event in America. A series of identical stadiums have been built in different parts of the country to host races. A focus on sustainability has swept the country as well, and sustainability is an important consideration in where championship races are held.

Today we’re going to create an API for use by DeepRacer officials when choosing race locations. It queries an ASDI dataset to select a city where the race will have the least environmental impact. To save on heating and cooling the competition committee has decided to look for sites where the average daily temperature is closest to 23.0 degrees Celsius. 

### Requirements

- Your own laptop, capable of running a command line and a text editor.
- Basic knowledge of AWS services ([Amazon S3](https://aws.amazon.com/s3/), [Amazon Athena](https://aws.amazon.com/athena/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon API Gateway](https://aws.amazon.com/api-gateway/))
-	Comfort working on the AWS Console and configuring AWS services
-	Working knowledge of SQL

### Contents

#### Sections

1. [Create an S3 bucket and subdirectories](sections/Section-1-S3.pdf)
1. [Connecting Athena to the NOAA data repository](sections/Section-2-Athena.pdf)
1. [Creating the endpoint and querying Athena](sections/Section-3-APIGW-Lambda.pdf)
1. [Create an S3 bucket and subdirectories as a webserver](sections/Section-4-S3-web.pdf)
1. [Next steps: Customize the Code Green Workshop](sections/Section-5-next-steps-references.pdf)
  
#### Code

- [iam.json](code/iam.json)
- [lambda-code.py](code/lambda-code.py)
- [sql-statements.sql](code/sql-statements.sql)
- [test-event-lambda.json](code/test-event-lambda.json)
- [index.html](code/index.html)
- [stadiums-with-stations_global.csv](code/stadiums-with-stations_global.csv)
  
### Getting started

-	Begin with [Section 1](sections/Section-1-S3.pdf) and progress through the sections in order, as successful completion of each exercise is necessary to complete subsequent sections.
- As a best practice, as you create new objects in AWS, keep track of what you have created (names of things like S3 buckets, database names, etc) in a notebook or text editor. This will make it easier to refer to these objects in other sections.
-	The workshop uses Event Engine, a tool used for AWS events which will automatically create a correctly-configured temporary account for workshop participants. The account will be automatically cleaned up and deleted after the workshop is over. If you want to recreate the workshop in your own account later, [a CloudFormation template is available](completed-workshop.cfn.json) which will automatically create the completed workshop.

### High-level workflow

In this workshop, you will be using various services to create an application that will enable end-users to query an ASDI dataset and determine the city with the temperature closest to 23 degrees Celsius. The process will be following these high-level steps:

1. Create a new AWS S3 bucket that will act as the query repository and hold the city location data 
1. Create Amazon Athena tables to query the data set
1. Create an Amazon Lambda function to query Athena
1. Create an AWS API Gateway endpoint which will call the Lambda
1. Build a static S3 Website to interface with API Gateway

<img src="architecture.png" alt="Workshop architecture diagram"
	title="Workshop architecture diagram" style="width:90%" />
<br><br>
  
### [Get started!](https://github.com/awslabs/amazon-asdi/blob/master/code-green/workshop/sections/Section-1-S3.pdf)


### Contact

If you have questions, corrections, suggestions, or reflections, please contact [sustainability-data-initiative@amazon.com](mailto:sustainability-data-initiative@amazon.com)

