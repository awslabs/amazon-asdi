![aws](images/aws_logo_100.png "AWS logo")

----

### Section 5

# Customize the Code Green Workshop

You’ve created a recommendation API to tell Deep Racer facilitators which city is closest to their target room temperature! This reduces heating and cooling of the Deep Racer stadium and is a step toward a more sustainable event. There are several ways improve this API and customize it for other events:

## Add your own cities to the list of potential cities

Think of cities where you’d like to host events. Download NOAA’s list of all stations in the GHCN-D, available here: [http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt](http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt). Manually or programmatically search this file to find stations near the cities you are interested in. Use your Athena table created in the workshop to check out data on these stations, and ensure its recent. If it is, add the station name to the stadiums-with-stations\_global.csv file and upload this to S3. Update your Glue table, using Lab-guide-Section-2-Athena as a reference, or use a [Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to update it automatically. The API should now include your custom cities.

## Add additional GHCN-D data to the recommendation API

How could precipitation or snowfall affect the sustainability of your event? Could we avoid holding events in cities that are currently experiencing a drought? Refer to the [NOAA GHCN details](https://docs.opendata.aws/noaa-ghcn-pds/readme.html) to understand which measurements are included in the GHCN-D. Edit the exiting Lambda function, lambda-code.py, or create a separate function to add additional criteria to your recommendation API.

## Replace the GHCH-D with forecast data

In this workshop, we’ve used historical temperature measurements to estimate future temperatures. A better way to estimate future temperature is to use a forecast model. NOAA provides one such model which estimates climate data up to 16 days in the future. Review the [Unidata NOAA Global Forecast System (GFS) Model](https://registry.opendata.aws/noaa-gfs-pds/) and replace the GHCN-D temperatures with this. Explore the difference in results. Is the same city suggested? Ask a facilitator for resource tips on working with GRIB formatted data.

## Customize the recommendation API with new inputs

Several factors beyond climate may impact what makes a city a sustainable choice for hosting your event. Is there efficient public transportation for attendees to commute? Are there solar or wind farms available that could power your event? What do solar radiance measurements look like for your cities? Do you have your own criteria, such as existing office locations or a preferred venue type for the event?

Participate in the hack by expanding the workshop concept with new inputs. Refer to the [Registry of Open Data on AWS](https://registry.opendata.aws/) for ideas and data.

## Explore the GHCN-D data visually

Use Amazon Athena and [Amazon QuickSight](https://aws.amazon.com/quicksight/) to map your cities and visualize them based on efficiency rating. Or use Quicksight to explore other parameters of the GHCN-D data. The blog [_Visualize over 200 years of global climate data using Amazon Athena and Amazon QuickSight_](https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/) includes step by step instructions.

## Improve the recommendation API wait time

We’ve queried the NOAA CSV data directly in this workshop which leads to ~15 second wait time. Use Amazon Glue or Athena to pre-process the ASDI data into your own S3 bucket in an alternate format such as Parquet. Edit the workshop code to use this table, and see how much you can reduce the query time for returning average temperature. The blog [_Visualize over 200 years of global climate data using Amazon Athena and Amazon QuickSight_](https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/) includes an example under the section titled _’Use CTAS to speed up queries’._

Other techniques to improve response time include exporting a smaller subset of the data into a different S3 bucket, or exporting the data to be queried into a more performant data store such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

# Useful links and background information

Blog:_Visualize over 200 years of global climate data using Amazon Athena and Amazon QuickSight_ ([https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/](https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/))

_NOAA Global Historical Climatology Network Daily (GHCN-D) dataset_: ([https://registry.opendata.aws/noaa-ghcn/](https://registry.opendata.aws/noaa-ghcn/))

_GHCN-D Climate data schema details_: ([https://docs.opendata.aws/noaa-ghcn-pds/readme.html](https://docs.opendata.aws/noaa-ghcn-pds/readme.html))

ASDI Sustainability Data: [https://registry.opendata.aws/tag/sustainability/](https://registry.opendata.aws/tag/sustainability/)
