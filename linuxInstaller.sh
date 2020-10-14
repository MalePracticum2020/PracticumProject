#!/bin/bash

PACKAGEPROGRAMS="python3-pip python3-venv git python3-pyqt5.qtwebengine"

if [ -x "/usr/bin/apt-get" ]; then
    sudo apt-get update
    sudo apt-get -y install $PACKAGEPROGRAMS
elif [ -x "/usr/bin/yum" ]; then
    sudo yum install -y $PACKAGEPROGRAMS
else
    echo "$OUTPUT_ERROR_PREFIX Distribution not supported"
    exit 1
fi

pip install pip --upgrade

pip install PyQT5 plotly dash Flask pandas plotly-express cachetools

sudo python3 -m pip install ipywidgets
