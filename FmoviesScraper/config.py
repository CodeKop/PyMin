from argparse import ArgumentError


class ConfigMeta:
    pass


class Config:
    _fields = ()

    def __init__(self):
        pass

    @staticmethod
    def parse(data, kind="data"):
        if kind == "data":
            pass
        elif kind == "file":
            pass
        else:
            raise ArgumentError()

    @staticmethod
    def load_dict(dict):
        pass
