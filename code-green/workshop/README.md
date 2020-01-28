### HAC201
# Code Green:<br>Hacking on Amazon Sustainability Data Initiative datasets

## Workshop

### Duration: 2 hours

This workshop is one of two tracks offered by **Code Green: Hacking on Amazon Sustainability Data Initiative datasets** at re:Invent 2019. If you'd prefer to compete, [check out the hackathon](https://github.com/awslabs/amazon-asdi/tree/master/code-green/hackathon), which will be held concurrently in the same event space.

### The Scenario

The year is 2030, and MLD—Major League DeepRacer—is now the most popular sporting event in America. A series of identical stadiums have been built in different parts of the country to host races. Sustainability is an important consideration in where championship races are held.

Today we’re going to create an app for DeepRacer officials to use when choosing race locations. The competition committee has decided to look for sites where the average daily temperature is closest to 23.0 degrees Celsius, to save on heating and cooling costs. The app queries an ASDI dataset ([GHNC-D](https://registry.opendata.aws/noaa-ghcn/)) and then calculate daily averge temperatures in potential race locations.

### Requirements

- Your own laptop, capable of running a command line and a text editor.
-	Basic familarity with the AWS Console and configuring AWS services.
-	Some knowledge of SQL.

### High-level workflow

In this workshop you will:

1. Create a new AWS S3 bucket that will act as the query repository and hold the city location data.
1. Create Amazon Athena tables to query the data set.
1. Create an Amazon Lambda function to call the Athena query.
1. Create an AWS API Gateway endpoint which will call the Lambda.
1. Build a static S3 Website, with a basic web page that calls the API Gateway.

#### Setup

→ **[Start here: download files and set up your workshop account](setup.md)**

#### Sections

Once you have your files and account set up, follow the directions in each section below. Go in order, as they build on each other.

1. [Create an S3 bucket and subdirectories](sections/section-1-s3.md)
1. [Connecting Athena to the NOAA data repository](sections/section-2-athena.md)
1. [Creating the endpoint and querying Athena](sections/section-3-apigw-lambda.md)
1. [Create an S3 bucket and subdirectories as a webserver](sections/section-4-s3-web.md)
1. [Next steps: Customize the Code Green Workshop](sections/section-5-next-steps.md)

#### Code

These code samples are referenced in the workshop, and listed here for your convenience:

- [iam.json](code/iam.json)
- [lambda-code.py](code/lambda-code.py)
- [sql-statements.sql](code/sql-statements.sql)
- [test-event-lambda.json](code/test-event-lambda.json)
- [index.html](code/index.html)
- [stadiums_with_stations_global.csv](code/stadiums_with_stations_global.csv)

#### Do it for me mode

<details>
	<summary>Follow these steps to automatically create a finished version of this workshop.</summary>
  <br />
  The repo includes a CloudFormation script (<a href="https://github.com/awslabs/amazon-asdi/blob/master/code-green/workshop/code/completed-workshop.cfn.json">here</a>), which will automatically set up all the infrastructure that you would otherwise manually create in this workshop. To run the script follow these steps:


  * Click to [launch CloudFormation stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3.amazonaws.com/code-green-asdi/templates/completed-workshop.cfn.json). This will automatically load the script from this repo into CloudFormation and ask you for the info necessary to run it.
  * Enter "CodeGreenWorkshop" as the stack name (or any other descriptive name)
  * Check "I acknowledge that AWS CloudFormation might create IAM resources" near bottom of page
  * Click "Create Stack" button at bottom of page
  * Wait for stack to show "Create Complete" on left side of screen.  This may take a few minutes. There is a refresh button next to "Stacks"
  * Click on the "Resources" table to explore the resources that CloudFormation created for you
  * Click on the "Outputs" tab.  The "Website URL" output has a clickable link you can use to run the query against the infrastructure you just created.

</details>

#### Architecture

When you're done, this is what you'll have created:

<img src="images/architecture.png" alt="Workshop architecture diagram"
	title="Workshop architecture diagram" style="width:90%" />
<br><br>

### Contact

If you have questions, corrections, suggestions, or reflections, please contact [sustainability-data-initiative@amazon.com](mailto:sustainability-data-initiative@amazon.com).

