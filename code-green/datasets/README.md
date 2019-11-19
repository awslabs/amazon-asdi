# Code Green Recommended Datasets

Below is summary information on climate and weather datasets that are good candidates for Code Green projects. You can view the full set of sustainability datasets elibible for use [here](https://registry.opendata.aws/tag/sustainability/).

* [Extreme Weather](#extreme-weather)
    * [NOAA Global Historical Climatology Network Daily (GHCN-D)](#noaa-global-historical-climatology-network-daily-ghcn-d)
    * [NOAA Global Forecast System (GFS)](#noaa-global-forecast-system-gfs)
    * [ECMWF ERA5 Reanalysis](#ecmwf-era5-reanalysis)
* [Air Quality](#air-quality)
    * [OpenAQ](#openaq)
    * [SILAM Air Quality Forecasts](#silam-air-quality-forecasts)
* [Future climate](#future-climate)
    * [Community Earth System Model Large Ensemble (CESM LENS)](#community-earth-system-model-large-ensemble-cesm-lens)

## Extreme Weather

Extreme weather events significantly impact communities and business every year. *Weather observations are the fundamental data used for monitoring weather and assess potential risks emerging from extreme weather conditions to issue weather warnings. *In addition, weather forecast data is valuable to improve the predictive capabilities of emergency managers and planners.

### NOAA Global Historical Climatology Network Daily (GHCN-D)
[https://registry.opendata.aws/noaa-ghcn/](https://registry.opendata.aws/noaa-ghcn/)

The Global Historical Climatology Network Daily database, or GHCN-D, is a composite of climate records from numerous sources that were merged together and subjected to a common suite of quality assurance reviews. It contains meteorological measurements from over 90,000 stations across the globe. About two thirds of the observations are for precipitation measurement only.

**Main variables**<br/>
- Precipitation
- Temperature (at time of observation, and daily min/max)
- Snowfall and snow depth

**Spatial Resolution**<br/>
Station-based

**Spatial Coverage**<br/>
Global

**Temporal Resolution**<br/>
Daily

**Temporal Coverage**<br/>
1763 to present (varies by station)

**Data format**<br/>
CSV

**Access this data on AWS**<br/>

Via [CLI](https://aws.amazon.com/cli/):

    aws s3 cp s3://noaa-ghcn-pds/csv.gz/1788.csv.gz localdir_path  
    aws s3 cp s3://noaa-ghcn-pds/csv/1788.csv localdir_path

Via HTTP:

    https://noaa-ghcn-pds.s3.amazonaws.com/csv.gz/1788.csv.gzhttps://noaa-ghcn-pds.s3.amazonaws.com/csv/1788.csv  

**Additonal Resources**<br/>
- [Documentation](https://docs.opendata.aws/noaa-ghcn-pds/readme.html)
- Blog post: [Visualize over 200 years of global climate data using Amazon Athena and Amazon QuickSight](https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/)  


### NOAA Global Forecast System (GFS)
[https://registry.opendata.aws/noaa-gfs-bdp-pds/](https://registry.opendata.aws/noaa-gfs-bdp-pds/)

NOAA Global Forecast System is the operational global forecast model run by the U.S. National Weather Service. The GFS forecasts numerous variables with x-y-pressure coordinates.  

**Main variables**<br/>
- Precipitation
- Temperature
- Winds

**Spatial Resolution**<br/>
0.125 degree

**Spatial Coverage**<br/>
Global

**Temporal Resolution**<br/>
1-hourly

**Temporal Coverage**<br/>
Rolling 4-week archive

**Data format**<br/>
[GRIB2](https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/)

**Access this data on AWS**<br/>

Via [CLI](https://aws.amazon.com/cli/):

    aws s3 cp s3://noaa-gfs-bdp-pds/gfs.20191111/00/gfs.t00z.pgrb2full.0p50.f000 localdir_path  

Via HTTP

    https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.20191111/00/gfs.t00z.pgrb2full.0p50.f000  

**Additonal Resources**<br/>
  
Notebook: [NOAA GFS on AWS Jupyter Notebook](https://github.com/creare-com/podpac-examples/blob/master/notebooks/demos/gfs.ipynb)  

### ECMWF ERA5 Reanalysis
[https://registry.opendata.aws/ecmwf-era5/](https://registry.opendata.aws/ecmwf-era5/)

ERA5 is the fifth generation of ECMWF atmospheric reanalyses of the global climate, and the first reanalysis produced as an operational service. It utilizes the best available observation data from satellites and in-situ stations, which are assimilated and processed using ECMWF's Integrated Forecast System (IFS) Cycle 41r2.

**Main variables**<br/>
- Precipitation
- Temperature
- Winds

**Spatial Resolution**<br/>
31 km

**Spatial Coverage**<br/>
Global

**Temporal Resolution**<br/>
1-hourly

**Temporal Coverage**<br/>
2008-2018

**Data format**<br/>
[NetCDF](https://www.unidata.ucar.edu/software/netcdf/)

**Access this data on AWS**

Via [CLI](https://aws.amazon.com/cli/):

    aws s3 cp s3://era5-pds/2018/01/data/air_temperature_at_2_metres.nc localdir_path  

Via HTTP

    https://era5-pds.s3.amazonaws.com/2018/01/data/air_temperature_at_2_metres.nc  

**Additonal Resources**<br/>
Notebook: [Accessing ERA5 Data on S3 Jupyter Notebook](https://github.com/planet-os/notebooks/blob/master/aws/era5-s3-via-boto.ipynb)  


## Air Quality

Air quality [has a major impact on human health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4996129/), and is heavily influenced by the weather, as wild fires generate hazardous smoke which can impact large population centers for days or weeks at a time.

### OpenAQ
[https://registry.opendata.aws/openaq/](https://registry.opendata.aws/openaq/)

Global, aggregated physical air quality data from public data sources provided by government, research-grade and other sources.

**Main variables:**<br/>
- PM2.5
- PM10

**Spatial Resolution**<br/>
Station-based

**Spatial Coverage**<br/>
Global

**Temporal Resolution**<br/>
Minutes

**Temporal Coverage**<br/>
2013 to present (varies by station)

**Data format**<br/>
JSON

**Access this data on AWS**<br/>
Via CLI
    aws s3 cp s3://openaq-fetches/realtime/2019-11-11/1573430464.ndjson localdir_path  

Via HTTP
    https://openaq-fetches.s3.amazonaws.com/realtime/2019-11-11/1573430464.ndjson .

**Additonal Resources**<br/>
Blog post: [Using Athena to access the whole archive](https://medium.com/@openaq/how-in-the-world-do-you-access-air-quality-data-older-than-90-days-on-the-openaq-platform-8562df519ecd)  
Blog post: [Access OpenAQ data via a filterable SNS topic](https://medium.com/@openaq/get-faster-access-to-real-time-air-quality-data-from-around-the-world-c6f9793d5242)  

### SILAM Air Quality Forecasts

[https://registry.opendata.aws/silam/](https://registry.opendata.aws/silam/)

SILAM atmospheric composition and air quality forecast performed on a daily basis for > 100 species and covering the troposphere and the stratosphere.

**Main variables**<br/>
- CO
- NO2

**Spatial Resolution** 20 km

**Spatial Coverage** Global

**Temporal Resolution** 1-day

**Temporal Coverage** Rolling 10-day archive

**Data format** netcdf or zarr

**Access this data on AWS**  

Via AWS Command Line Interface (example):
         
    aws s3 cp s3://fmi-opendata-silam-surface-netcdf/global/20191021/silam_glob_v5_6_20191021_CO_d0.nc localdir_path  

Via HTTP (example):  

    https://fmi-opendata-silam-surface-netcdf.s3.amazonaws.com/global/20191021/silam_glob_v5_6_20191021_CO_d0.nc  

**Additonal Resources**
Notebook: [Simple ZARR Example Jupyter Notebook](https://github.com/fmidev/opendata-resources/blob/master/examples/python/Simple%20Zarr%20Example.ipynb)  


## Future Climate

The effects of climate change on communities and business are visible today, expected to increase over time, and will have disproportionate impacts on some more vulnerable communities. These impacts are already happening: from more intense hurricanes, to droughts and heat waves, climate change is creating new risks to physical assets, populations and business operations.

### Community Earth System Model Large Ensemble (CESM LENS) 

[https://registry.opendata.aws/ncar-cesm-lens/](https://registry.opendata.aws/ncar-cesm-lens/)

The Community Earth System Model (CESM) Large Ensemble Numerical Simulation (LENS) dataset includes a 40-member ensemble of climate simulations using historical data (1920-2005) or assuming the RCP8.5 greenhouse gas concentration scenario (2006-2100), as well as longer control runs based on pre-industrial conditions. The data comprise both surface (2D) and volumetric (3D) variables in the atmosphere, ocean, land, and ice domains.

**Main variables**<br/>
- Temperature
- Precipitation

**Spatial Resolution**br/>
1 degree

**Spatial Coverage**br/>
Global

**Temporal Resolution**br/>
6-hourly

**Temporal Coverage**br/>
Historical 1920-2005, Future 2006-2100

**Data format**br/>
[Zarr](https://zarr.readthedocs.io/en/stable/)

**Additonal Resources**br/>
[Example Jupyter Notebook](https://github.com/NCAR/cesm-lens-aws/blob/master/notebooks/kay-et-al-2015.v3.ipynb)  

