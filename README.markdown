# Passphrase, a Python clone of passphra.se

### Arguments
- -n, --num\_words
  * Number of words in the passphrase.
  * Default : 4

- -w, --wordlist
  * Path to wordlist.
  * Default : passphra.se.txt
  * Note    : Wordlist must have each word separated by a newline.

- -m, --max\_length
  * Maximum length of a word.
  * Default : 8

- -p, --punctuation
  * Allow words with punctuation in them.
  * Default : False

- -l, --lowercase
  * Make the first letter of each word lowercase.
  * Default : False

- -ns, --no\_space
  * No space between words.
  * Default : False

- -np, --num\_phrases
  * Number of passphrases to generate.
  * Default : 1

- -o, --outfile
  * Path to output file.
  * Default : print to stdout
