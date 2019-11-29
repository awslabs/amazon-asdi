This repo provides two Docker containers which run Jupyter notebooks for working datasets from the Amazon Susatainability Data Initiative:

- Use the [gfs](https://github.com/awslabs/amazon-asdi/tree/master/code-green/notebooks/gfs) container to work with data from the [NOAA Global Forecast System (GFS)](https://registry.opendata.aws/noaa-gfs-bdp-pds/).
- Use the [ghcn](https://github.com/awslabs/amazon-asdi/tree/master/code-green/notebooks/ghcn) container to work with data from the [NOAA Global Historical Climatology Network Daily (GHCN-D)](https://registry.opendata.aws/noaa-ghcn/).

Some third-party notebooks that can help with ASDI data:

- [This notebook from PlanetOS](https://github.com/planet-os/notebooks/blob/master/aws/era5-s3-via-boto.ipynb) assists in working with [ERA5 data on ASDI](https://registry.opendata.aws/ecmwf-era5/).
- If you plan on using Amazon SageMaker check [this AWS-maintained managed Jupyter notebook](https://github.com/aws-samples/aws-research-workshops) containing notebooks related to data lakes, AI/ML, Batch, IoT, and Genomics.