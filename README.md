#Kartskrape

Kartskrape is an application for downloading files from Kartverket, without using their cumbersome download portal. It is a simple library focused on downloading entire datasets from.

Usage requires that you sign for an account at http://www.kartverket.no/download.

Documentation is simple as there really are just two functions.

## Usage
```
# import library
import kartskrape

# get a list of available datasets
datasets = kartskrape.get_datasets()

# download to datafolder
kartskrape.download_dataset("kartverket_user", "password", "offisielle-adresser-utm33-csv", "./data")
```




### Publish to pypi
This is the first project I've submitted to pypi (install with pip). I used twine to publish the package to pypi. Had some problems doing this on Windows with python 2.7, so I'm using python3 to actually push it to pypi.

```
python setup.py bdist_wheel
twine upload -s dist/*

```
