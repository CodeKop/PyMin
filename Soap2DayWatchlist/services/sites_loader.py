import json
import os
import requests


class SiteData:
    def __init__():
        pass

class SitesLoader:
    def __init__(self, sites_enable=[], sites_disable=[]):
        # Load sites data from sites folder
        # TODO: Make this an argument so it can be dynamic.
        self.sites_dir = './sites'
        site_files = self.load_sites()

        self.site_metas = []
        if sites_enable:
            self.site_metas = (x for x in sites_enable if x in site_files)
        elif sites_disable:
            self.site_metas = (x for x in site_files if x not in sites_disable)
        else:
            self.site_metas = site_files

        self.validate_enabled()

    def load_sites(self):
        """ Method to load sites from the sites folder. """
        sites = []
        if os.path.isdir(self.sites_dir):
            sites = os.listdir(self.sites_dir)

        return sites

    def validate_enabled(self):
        for site in self.site_metas:
            meta = json.load(open("./sites/" + site, "r"))

            uri = ""
            if ("acceptsHttps" in meta) and meta["acceptsHttps"]:
                uri += "https"
            else:
                uri += "http"
            uri += "://" + meta["baseUrl"]
            uri = ("https" if meta["acceptsHttps"]
                   else "http") + "://" + meta["baseUrl"]
            is_valid = is_site_valid(uri)
            print(is_valid)

    @staticmethod
    def retrieve_sites(sites_enable=[], sites_disable=[]):
        loader = SitesLoader(sites_enable=[], sites_disable=[])
        loader


def is_site_valid(uri: str) -> bool:
    with requests.get(uri, stream=True) as resp:
        try:
            resp.raise_for_status()
            return True
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.ConnectionError:
            return False
