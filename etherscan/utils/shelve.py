import shelve


class Shelve:
    SHELVE_FILE = r'data/etherscan_shelve'

    @staticmethod
    def shelve_store(key, data):
        # store result in cache
        d = shelve.open(Shelve.SHELVE_FILE)
        d[key] = data
        d.close()

    @staticmethod
    def shelve_load(key):
        d = shelve.open(Shelve.SHELVE_FILE)
        try:
            data = d[key]
            return data
        except KeyError as err:
            return None
        finally:
            d.close()

