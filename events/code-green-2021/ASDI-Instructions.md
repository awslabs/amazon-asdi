##
# <br> Instructions and Guidance for using Amazon Sustainability Data Initiative Datasets

### Getting Started 

These are three suggested datasets to get started, however there are many more datasets, in addition to these, listed at the [AWS Registry of Open Data](https://registry.opendata.aws/). These datasets are stored in [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/). If you have not worked with S3 previously, we recommend the following resources to get familiar:

- [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/index.html)
- [Amazon S3 API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

There are a number of ways to access objects stored in S3:

* In code using a 3rd party or AWS SDK such as the [AWS SDK for Python (Boto 3)](https://aws.amazon.com/sdk-for-python/)
* Via [the command line](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html) using the [AWS Command Line Interface](https://aws.amazon.com/cli/)
* Using a 3rd party graphical client such as [Cyberduck](https://cyberduck.io/)


Datasets listed at the AWS Registry of Open Data can be quite large. We recommend using these data in-place rather than copying data to another location, and using processing strategies that consume the data incrementally. Each dataset will be different, and will include documentation specific to the particular dataset. In addition, many datasets have tutorials and other usage examples to help you get started.

### NOAA GOES-16 & 17: [Location and documentation](https://registry.opendata.aws/noaa-goes/)

Ideas to get started

1. Visualize climatologies of land surface temperature, long wave radiation, or lightning
    - Where should you build solar farms based on the most clear skies?
    - Where is the most rain occurring now, and which reservoirs are capturing it?
2. Develop innovative alerts for real time weather events
    - Can real time alerts for wildfires help us protect the world’s ecosystem faster?

### GLEIF: [Location and documentation](https://registry.opendata.aws/lei/)

**Ideas to get started:**
1. Map entities showing international relationships for climate risk
2. Network analysis of major GHG, waste producing industries
3. Supply chain explorer for industry verticals

### CMIP6: [Location and documentation](https://registry.opendata.aws/cmip6/)

Ideas to get started

1. Using the ScenarioMIP runs explore how rainfall (and thus water availability) will change at your location over the next 100 years
2. Explore the future emission scenarios in ScenarioMIP to understand the full impact of reducing carbon emissions. How can this be extended to understand the impact of corporations committing to reduce carbon usage?



### Other Data: [Location](https://registry.opendata.aws/collab/asdi/)

### Next: [ADX Guide](ADX-Instructions.md) 
