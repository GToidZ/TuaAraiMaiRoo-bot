import json
import re
import logging

class Configuration:
    
    def __init__(self, path: str):
        self.__config_location = path
        self.__read_config(path)
        
    def __read_config(self, path: str):
        try:
            with open(path, "r+") as f:
                self.config = {k.strip(): v for
                               k, v in
                               json.load(f).items()
                               if not k.startswith("__")}
        except IOError:
            logging.exception("Cannot load config file!")

    def reload_config(self):
        """Reloads config file."""
        self.__read_config(self.__config_location)

    def query_key_by_regex(self, pattern: str):
        """Searches for key in current config by regex-pattern and
        makes a generator for all queries (k,v)."""
        pat = re.compile(pattern)
        queries = [key for key in self.config if pat.match(key)]
        for query in queries:
            yield (query, self.config[query])

    def query_key_by_keywords(self, *words: str):
        """Searches for key in current config by absolute keyword
        it returns a generator by calling the regex search function.
        This function will work indifferently from the regex
        search."""
        matching = [f"(\\b{w}\\b)" for w in words]
        return self.query_key_by_regex('|'.join(matching))
