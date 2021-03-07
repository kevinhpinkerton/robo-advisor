# robo-advisor

## Prerequisites

  + Anaconda 3.8+
  + Python 3.8+
  + Pip

## Installation

Fork this [remote repository](https://github.com/kevinhpinkerton/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.8 #first time only
conda activate stocks-env
```

From inside your virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

Go [here](https://www.alphavantage.co/) to get your free Alpha Vantage API key. 

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file with the following:

    ALPHAVANTAGE_API_KEY = "[Your Key Here]"
 
 ## Usage

Run the script:

```py
python app/robo_advisor.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment