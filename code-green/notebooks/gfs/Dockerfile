FROM jupyter/scipy-notebook:latest

RUN pip install --upgrade pip
RUN pip install PyAthena
RUN conda install -c anaconda basemap proj4 cfgrib

ENV PROJ_LIB $CONDA_DIR/share/proj/

RUN fix-permissions /home/$NB_USER
