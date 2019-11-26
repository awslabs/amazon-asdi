### HAC201
## Code Green: Hacking on Amazon Sustainability Data Initiative datasets

### Workshop Duration: 2 hours

Welcome to Code Green! This workshop was created as a supplement to the Hacking on Amazon Sustainability Data Initiative datasets hackathon at re:Invent 2019.

You will be building a API to learn about working with ASDI datasets and AWS services. The API has a single call, which queries one ASDI dataset ([GHNC-D](https://registry.opendata.aws/noaa-ghcn/)), and returns the most sustainable location for a sporting event. For the purposes of this workshop that just means a location that is neither too hot nor too cold. It could be expanded with additional data sources and more sophisticated algorithms to help select the most sustainable location for any kind of event, based on multiple criteria.

The workshop is meant to give you a starting point for exploring sustainability data. Use it to get up and running, then play with the data—what interesting things can you uncover? What other metrics can you look at when determining if a city is the best city for our fictious event? What other ways can you leverage this dataset, and what other data could you use in conjunction with it?

### The Scenario

The year is 2030, and MLD—Major League DeepRacer—has exploded, and is now the most popular sporting event in America. A series of identical stadiums have been built in different parts of the country to host races. A focus on sustainability has swept the country as well, and sustainability is an important consideration in where championship races are held.

Today we’re going to create an API for use by DeepRacer officials when choosing race locations. It queries an ASDI dataset to select a city where the race will have the least environmental impact. The competition committee has decided to look for sites where the average daily temperature is closest to 23.0 degrees Celsius. 

### Requirements

- Your own laptop, capable of running a command line and a text editor.
- Basic knowledge of AWS services ([Amazon S3](https://aws.amazon.com/s3/), [Amazon Athena](https://aws.amazon.com/athena/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon API Gateway](https://aws.amazon.com/api-gateway/))
-	Comfort working on the AWS Console and configuring AWS services
-	Working knowledge of SQL

### Contents

-	Sections:
  -	/sections/1-s3.pdf
  - /sections/2-athena.pdf
  - /sections/3-agigw-lambda.pdf
  - /sections/4-s3-web.pdf
  - /sections/5-useful-links.pdf
  
-	Code:
  - code/iam.json
  - code/lambda-code.py
  - code/sql-statements.sql
  - code/test-event-lambda.json
  - code/index.html
  - code/stadiums-with-stations_global.csv
  
### Getting started

-	Begin with Section 1 and progress through the sections in order, as successful completion of each exercise is necessary to complete subsequent sections.
- As a best practice, as you create new objects in AWS, keep track of what you have created (names of things like S3 buckets, database names, etc) in a notebook or text editor. This will make it easier to refer to these objects in other sections.
-	The workshop uses Event Engine, a tool used for AWS events which will automatically create a correctly-configured temporary account for workshop participants. The account will be automatically cleaned up and deleted after the workshop is over. If you want to recreate the workshop in your own account later, a CloudFormation template is available.

### High-level workflow

In this workshop, you will be using various services to create an application that will enable end-users to query an ASDI dataset and determine the city with the temperature closest to 23 degrees Celsius. The process will be following these high-level steps:

1. Create a new AWS S3 bucket that will act as the query repository and hold the city location data 
1. Create Amazon Athena tables to query the data set
1. Create an Amazon Lambda function to query Athena
1. Create an AWS API Gateway endpoint which will call the Lambda
1. Build a static S3 Website to interface with API Gateway

<img src="architecture.png" alt="Workshop architecture diagram"
	title="Workshop architecture diagram" style="width:90%" />

### Contact

If you have questions, corrections, suggestions, or reflections, please contact [sustainability-data-initiative@amazon.com](mailto:sustainability-data-initiative@amazon.com)

