#!/usr/bin/env python

"""StatsApp"""

import argparse

from . import parser as chat_parser
from . import analyser as chat_analyser

def main():
    """Main"""
    parser = argparse.ArgumentParser(prog='StatsApp')
    parser.add_argument('chat', help='Chat file')
    parser.add_argument('-w', '--words', nargs='+', help='Search words')
    args = parser.parse_args()
    chat_file = args.chat
    words = args.words
    # Load pandas dataframe
    df = chat_parser.load_file(chat_file)
    # print(df)

    # chat_analyser.plot_messages(df)
    chat_analyser.search(words, df)

if __name__=='__main__':
    sys.exit(main(sys.argv))
