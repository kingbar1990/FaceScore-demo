# FaceScore-demo

## Problems
DeepFace cannot analyze a lot of photos in one time.

## Installing guide
First, install python version 3.8 (any subversion) for your OS version.

#### Install packages
```
sudo apt-get update
sudo apt-get install python3-pip build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev python3-dev python3-pip
```

#### Install virtual environment package
`sudo apt install virtualenv`

#### Create virtual environment into your project root folder.
`virtualenv --python=python3.8 venv`

#### Run virtual environment
`. venv/bin/activate`

#### Install dlib and then other libraries.
```
pip install dlib
pip install -r requirements.txt
```

### Run project
1. Start the virtual environment (if you haven't already).
2. `python main.py`

## Notes
> You can change input data in **input/** directory.
> Result of working program saving at **output/** directory.
>
> If the program ends with the message "killed", then you don't have enough RAM for that many photos. In this case, delete unnecessary photos in the **input/** directory.