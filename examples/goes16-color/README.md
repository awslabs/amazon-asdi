NOAA GOES16 True Color Jupyter Notebook Example
===============================================

This notebook demonstrates how to use `conda` to install `micromamba`, and then install necessary python packages using that. From there the notebook shows how to access [GOES-16](https://registry.opendata.aws/noaa-goes/) data using `fsspec` and `xarray` for streaming the data directly from Amazon S3. Finally the notebook shows how to plot multispectral imagery from GOES-16 by loading 3 channels at once for plotting with matplotlib.


