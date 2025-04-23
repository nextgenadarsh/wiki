pip
---

## User Guide

### Common tasks

- `pip` is the reference Python package manager
- Used to install and update packages.
- Upgrade pip to latest version `python3 -m pip install --upgrade pip`
- Identify the pip version `python3 -m pip --version`
- Install python package `python3 -m pip install requests`
- Install specific python package version:
    - `python3 -m pip install 'requests==2.18.4' `
    - `python3 -m pip install 'requests>=2.0.0,<3.0.0' `
- Install python package extra `python3 -m pip install 'requests[security]' `
- Upgrade python package `python3 -m pip install --upgrade requests`

### Using requirement file to store the python package versions

- You can declare the dependencies in a file so that you can install it again on other machine when required
- Example requirement file:
    ```
    requests==2.18.4
    google-auth==1.1.0
    ```
- Install all packages using file `python3 -m pip install -r requirements.txt`
- Export the list list of packages installed to file `python3 -m pip freeze`
