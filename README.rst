Kartskrape is an application for downloading files from Kartverket, without using their cumbersome download portal.

Usage:
import kartskrape

kartskrape.list_datasets()

kartskrape.download_dataset("kartverket_user", "password", "offisielle-adresser-utm33-csv", "./data")
