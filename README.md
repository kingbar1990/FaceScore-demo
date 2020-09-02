# FaceScore-demo

## Problems

DeepFace cannot analyze a lot of photos in one time.

## Installing guide

First, install python version 3.8.5 for your OS version.

### Install packages

sudo apt-get update

sudo apt-get install python3-pip
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python3 python3-dev python3-pip

#### Or in one string

sudo apt-get install python3-pip build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev python3-dev python3-pip

### Create virtual environment into your project root folder.

virtualenv --python=python3.8 venv

### Install dlib to virtualenv.

pip install dlib

### Install reqiurements

pip install -r requirements.txt