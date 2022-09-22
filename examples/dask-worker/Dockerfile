FROM public.ecr.aws/docker/library/python:3.10-slim-buster

ENV PYTHONUNBUFFERED=TRUE
ENV DEBIAN_FRONTEND noninteractive
ENV CONDA_DIR="/opt/conda"
ENV PATH="${CONDA_DIR}/bin:${PATH}"

RUN apt-get update \
  && apt-get install -y bzip2 gcc wget \
  && rm -rf /var/lib/apt/lists/*

RUN arch=$(uname -m) && \
    if [ "${arch}" = "x86_64" ]; then \
        arch="64"; \
    fi && \
    wget -qO- https://anaconda.org/conda-forge/micromamba/0.19.1/download/linux-${arch}/micromamba-0.19.1-0.tar.bz2 | tar -xvj bin/micromamba --strip-components=1

RUN mkdir -p "${CONDA_DIR}" && \
    mv micromamba /bin/micromamba


RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

RUN micromamba install --root-prefix="${CONDA_DIR}" --prefix="${CONDA_DIR}" \
    -y -c conda-forge \
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
