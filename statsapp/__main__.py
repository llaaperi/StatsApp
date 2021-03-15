#!/usr/bin/env python

"""StatsApp"""

import argparse

from . import parser as chat_parser

def main():
    """Main"""
    parser = argparse.ArgumentParser(prog='StatsApp')
    parser.add_argument('chat', help='Chat file')
    args = parser.parse_args()
    chat_file = args.chat

    # Load pandas dataframe
    df = chat_parser.load_file(chat_file)
    # print(df)
    chat_parser.plot_messages(df)

if __name__=='__main__':
    sys.exit(main(sys.argv))
