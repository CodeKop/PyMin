from argparse import ArgumentParser
from sites_loader import SitesLoader

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
                "type": ["string", "object"]
            }
        }
    },
    "required": [
        "baseUrl",
        "acceptsHttps",
        "pages"
    ]
}


def main():
    loader = SitesLoader()


if __name__ == "__main__":
    main()
