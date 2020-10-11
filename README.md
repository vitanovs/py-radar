# py-radar

This repository contains the source code of the `py-radar` project. The project aims to
provide the opportunity to quickly analyze if an email is falsely interpreted as spam or not.

## Requirements

* [Python](https://www.python.org/downloads/release/python-380/) - v3.8 at least
* [GNU make](https://www.gnu.org/software/make/) - v3.81 at least

## Installation

Follow the next items to correctly configure and install the application

* Create virtual environment (optional)

    ```sh
    python -m venv venv
    source ./venv/bin/activate
    ```

* Install all requirements

    ```sh
    pip install -r ./requirements.txt
    ```

## Usage

The following items define the general usage of the application.

* Initialization

    ```sh
    make init
    ```

* Run

    ```sh
    make run PATH=/path/to/your/dataset
    ```

* Lint

    ```sh
    make lint
    ```
