# -*- coding:UTF-8 -*-


# Standard library imports
import os, sys
import argparse

# Local application imports
from src import env
from src import google_cred as cred

from mod import logging_class as logcl
from mod import json_conf
from mod import sheet

logger = logcl.PersonalLog('site-search', env.LOG_DIR)


def main():
    # Check for config file existence
    try:
        config = json_conf.Config(env.CONFIG_FILE)
    except FileNotFoundError as err:
        logger.warning('Config file {} not found: {}'.format(env.CONFIG_FILE, err))
        sys.exit(11)
    except json_conf.configError as err:
        logger.warning('Wrong configuration: {}'.format(err))
        sys.exit(12)

    credential = cred.google_credential(config.google_sheet_cred)
    gs = sheet.Sheet(credential, config.google_sheet_id)

    # TODO: Check searches validation

    for search in config.searches:
        config.search_content(search)
        last_row = gs.get_last_row(f"'{config.sheetname}'!{config.src_col}:{config.src_col}")        
        contents = gs.read_range(f"'{config.sheetname}'!{config.src_col}{config.google_sheet_start_row}:{config.src_col}{last_row}")


        print(contents)


if __name__ == '__main__':
    main()