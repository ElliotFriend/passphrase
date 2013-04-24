#!/usr/bin/env python
# encoding: utf-8

""" Generate a passphrase.
    A Python implementation of passphra.se
    Default wordlist is the same as passphra.se
"""

import argparse
import random
import sys


def get_args(): #{{{
    """ Get arguments from the command line. """

    parser = argparse.ArgumentParser(
            description="Generate a passphrase.",
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-n", "--num_words",
            type=int, default=4,
            help="Number of words in the passphrase.\n" +
                 "Default : 4")

    parser.add_argument("-w", "--wordlist",
            type=str, default="passphra.se.txt",
            help="Path to wordlist.\n" +
                 "Default : passphra.se.txt\n" +
                 "Note    : Wordlist must have each word " +
                 "separated by a newline.")

    parser.add_argument("-m", "--max_length",
            type=int, default="8",
            help="Maximum length of a word.\n" +
                 "Default : 8")

    parser.add_argument("-p", "--punctuation",
            action="store_true",
            help="Allow words with punctuation in them.\n" +
                 "Default : False")

    args = parser.parse_args()
    return args #}}}


def get_word(wordlist, args): #{{{
    """ Choose a random word from the wordlist that meets our requirements.
        Only allow 500 iterations, as more than that probably means we have
        a bad (malformed?) wordlist.
    """
    iters = 0
    while iters < 500:
        word = random.choice(wordlist).strip().lower()

        if args.punctuation == False:
            if len(word) < args.max_length and word.isalpha() == True:
                return word
                iters += 1
        elif args.punctuation == True:
            if len(word) < args.max_length:
                return word
                iters += 1 #}}}


def main(args): #{{{
    """ Generate a passphrase. """

    try:
        wordlist = open(args.wordlist).readlines()
    except IOError:
        print 'Bad wordlist path or permissions: {path}'.format(
                path=args.wordlist)
        sys.exit(1)

    # Generate n words, each with a length less than args.max_length.
    words = [get_word(wordlist, args) for _ in range(args.num_words)]

    return ''.join(words) #}}}


if __name__ == '__main__':
    try:
        print main(get_args())
    except KeyboardInterrupt:
        sys.exit()
