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

def _print_message(row):
    """Print message"""
    print(f'{row.timestamp} -> {row.sender} -> {row.message}')

def _count_words(message, words):
    """Count occurences of words in message"""
    return sum(map(message.count, words))

def search(words, df):
    """Search words from messages"""
    for row in df.itertuples(index=False):
        count = _count_words(row.message, words)
        if count:
            _print_message(row)

def plot_messages(df):
    """"""
    counts = {}
    senders = []
    for row in df.itertuples(index=False):
        date = row.timestamp.date()
        if date not in counts:
            counts[date] = {}
        if row.sender not in counts[date]:
            counts[date][row.sender] = 0

        count = _count_words(row.message, ['rakas', 'kulta'])
        if count:
            logging.info(row.message)
        counts[date][row.sender] += count
        # Collect senders
        if row.sender not in senders:
            senders.append(row.sender)
    # print(counts)
    # print(senders)

    dates = list(counts.keys())
    values = [[] for sender in senders]
    for date in dates:
        for idx, sender in enumerate(senders):
            values[idx].append(counts[date].get(sender, 0))
    # print(values)

    # Plot
    fig, ax = plt.subplots()
    previous_values = None
    for idx, sender in enumerate(senders):
        bottom = values[idx-1] if idx > 0 else None
        ax.bar(dates, values[idx], bottom=bottom, label=sender)
    ax.legend()
    plt.show()
