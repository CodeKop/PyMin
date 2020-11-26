import json
import os

import requests

site_meta_schema = {
  "$schema": "https://json-schema.org/schema#",
  "type": "object",
  "properties": {
    "baseUrl": {
      "type": "string"
    },
    "acceptsHttps": {
      "type": "boolean"
    },
    "pages": {
      "type": "object",
      "properties": {
      	"type": ["string","object"]
      }
    }
  },
  "required": [
    "baseUrl",
    "acceptsHttps",
    "pages"
  ]
}

def main(args):
    print("1")
    Application(sites_enable=["soap2day.to"])
    print(2)
    Application(sites_disable=["soap2day.to"])
    print(3)
    Application()


class Application:
    def __init__(self, sites_enable=[], sites_disable=[]):
        # Load sites data from sites folder
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
        sites = []
        if os.path.isdir("./sites"):
            sites = os.listdir("./sites")

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
            uri = ("https" if meta["acceptsHttps"] else "http") + "://" + meta["baseUrl"]
            is_valid = is_site_valid(uri)
            print(is_valid)


def is_site_valid(uri: str) -> bool:
    with requests.get(uri, stream=True) as resp:
        try:
            resp.raise_for_status()
            return True
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.ConnectionError:
            return False
