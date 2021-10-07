FROM quay.io/condaforge/miniforge3

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN conda install --yes \
    -c conda-forge \
    python==3.7.10 \
    python-blosc==1.10.2 \
    dask==2021.8.1 \
    lz4==3.1.3 \
    nomkl==1.0 \
    msgpack-python==1.0.2 \
    netcdf4==1.5.7 \
    numpy==1.21.2 \
    pandas==1.3.2 \
    xarray==0.19.0 \
    bokeh==2.2.3 \
    s3fs==2021.8.1 \
    fsspec==2021.8.1 \
    h5netcdf==0.11.0 \
    distributed==2021.8.1 \
    tornado==6.1 \ 
    cloudpickle==1.6.0 \
    h5py==3.4.0 \
    zarr==2.9.5 \
    rechunker==0.4.2 \
    intake-esm==2021.8.17 \
    intake==0.6.3 \
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
