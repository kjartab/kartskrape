#Kartskrape

Kartskrape is an application for downloading files from Kartverket, without using their cumbersome download portal.

## Usage
```
import kartskrape

kartskrape.list_datasets()

kartskrape.download_dataset("kartverket_user", "password", "offisielle-adresser-utm33-csv", "./data")
```

## Publish to pypi
Twine is used to publish to pypi. Problems doing this on Windows with python 2.7, so I'm using python3 to actually push it to pypi.

```
python setup.py bdist_wheel
twine upload -s dist/*

```
