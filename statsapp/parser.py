#!/usr/bin/env python

"""parser.py: Parse whatsapp exported chat to pandas DataFrame"""

import re
import sys
import time
import pandas
import logging
from datetime import date, datetime
from collections import defaultdict
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)

ENTRY_REGEX = r'(?P<timestamp>\d{1,2}\/\d{1,2}\/\d{1,2}, \d{1,2}:\d{1,2} [AP]M)\s-\s(?P<sender>.+?):\s(?P<message>.+)'
ENTRY_PATTERN = re.compile(ENTRY_REGEX)

def load_file(filename, max_lines=None):
    """Load whatsapp export to pandas dataframe"""
    logging.info(f'Loading chat from file <{filename}>')
    data = {
        'timestamp': [],
        'sender': [],
        'message': []
    }
    with open(filename) as file:
        for idx, line in enumerate(file):
            if idx == max_lines:
                logging.info(f'Terminating loading at line {idx}')
                break
            # Parse line to timestamp and message
            match = ENTRY_PATTERN.match(line)
            if not match:# If parrent fails, current line is extension to previous line message part
                data['message'][-1] += f'\n{line}'
                continue
            # Parse timestamp
            try:
                timestamp = datetime.strptime(match.group("timestamp"), '%m/%d/%y, %I:%M %p')
            except ValueError as error:
                logging.debug(error)
                continue
            sender = match.group("sender")
            message = match.group("message")
            logging.debug(f'{timestamp} -> {sender} -> {message}')
            # Add to data
            data['timestamp'].append(timestamp)
            data['sender'].append(sender)
            data['message'].append(message)
    # Return data frame
    return pandas.DataFrame(data)
