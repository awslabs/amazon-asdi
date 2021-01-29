FROM quay.io/condaforge/miniforge3

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN conda install --yes \
    -c conda-forge \
    python==3.7.9 \
    python-blosc==1.10.2 \
    cytoolz==0.11.0 \
    dask==2021.1.1 \
    lz4==3.1.3 \
    nomkl==1.0 \
    msgpack-python==0.6.2 \
    netcdf4==1.5.5.1 \
    numpy==1.19.5 \
    pandas==1.2.1 \
    xarray==0.14.1 \
    bokeh==2.2.3 \
    s3fs==0.5.2 \
    fsspec==0.8.5 \
    h5netcdf==0.8.1 \
    distributed==2021.1.1 \
    tornado==6.1 \ 
    cloudpickle==1.6.0 \
    h5py==3.1.0 \
    && conda clean -tipsy \
    && find /opt/conda/ -type f,l -name '*.a' -delete \
    && find /opt/conda/ -type f,l -name '*.pyc' -delete \
    && find /opt/conda/ -type f,l -name '*.js.map' -delete \
    && find /opt/conda/lib/python*/site-packages/bokeh/server/static -type f,l -name '*.js' -not -name '*.min.js' -delete \
    && rm -rf /opt/conda/pkgs

#    zarr==2.3.2 \
 #   rechunker==0.3.2 \

COPY prepare.sh /usr/bin/prepare.sh
RUN chmod +x /usr/bin/prepare.sh

RUN mkdir /opt/app /etc/dask
COPY dask.yaml /etc/dask/

ENTRYPOINT ["/usr/local/bin/dumb-init", "/usr/bin/prepare.sh"]
