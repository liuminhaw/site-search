# -*- coding:UTF-8 -*-


# Standard library imports
# import standard libraries here
import json


class Config:
    
    def __init__(self, config_file):
        """
        Params:
            config_file - json configuration file (default conf.json)
        Errors:
            configError - configuration error
        """
        self.config_file = config_file
        with open(self.config_file, 'r') as json_file:
            configs = json.load(json_file)
            self.searches = self._key_error(configs, 'searches')
            self.google_sheet = self._key_error(configs, 'Google-Sheet')
            self.google_sheet_cred = self._key_error(self.google_sheet, 'cred')
            self.google_sheet_id = self._key_error(self.google_sheet, 'id')
            self.google_sheet_start_row = self._key_error(self.google_sheet, 'start-row')

    def search_content(self, search_conf):
        """
        Params:
            search_conf - dict of single search information
        Errors:
            configError - configuration error
        """
        self.sheetname = self._key_error(search_conf, 'sheetname')
        self.src_col = self._key_error(search_conf, 'content-col')
        self.res_col = self._key_error(search_conf, 'result-col')
        self.src_link = self._key_error(search_conf, 'source-link')

    def _key_error(self, configs, key):
        """
        Params:
            configs - json data block
            key - parsing key value
            msg - output message if KeyError raised
        Return:
            parsed data value
        """
        try:
            config_value = configs[key]
        except KeyError:
            msg = '{} - {} not found in config file'.format(configs, key)
            raise configError(msg)
        else:
            return config_value

# Exceptions
class configError(Exception):
    """
    Base class of config exception
    """
    pass
