FROM quay.io/condaforge/miniforge3

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN conda install --yes \
    -c conda-forge \
    python==3.7.9 \
    python-blosc==1.8.1 \
    cytoolz \
    dask==2.19.0 \
    lz4==3.0.2 \
    nomkl \
    msgpack-python==0.6.2 \
    netcdf4==1.5.3 \
    numpy==1.17.3 \
    pandas==1.0.5 \
    xarray==0.16.2 \
    bokeh==2.1.1 \
    s3fs==0.5.2 \
    fsspec==0.8.5 \
    h5netcdf==0.8.0 \
    distributed==2.19.0 \
    tornado==6.0.4 \ 
    cloudpickle==1.4.1 \
    h5py==2.10.0 \
    zarr==2.3.2 \
    rechunker==0.3.2 \
    && conda clean -tipsy \
    && find /opt/conda/ -type f,l -name '*.a' -delete \
    && find /opt/conda/ -type f,l -name '*.pyc' -delete \
    && find /opt/conda/ -type f,l -name '*.js.map' -delete \
    && find /opt/conda/lib/python*/site-packages/bokeh/server/static -type f,l -name '*.js' -not -name '*.min.js' -delete \
    && rm -rf /opt/conda/pkgs

COPY prepare.sh /usr/bin/prepare.sh
RUN chmod +x /usr/bin/prepare.sh

RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/bin/prepare.sh"]