# pygments-dafny

## About

This repository contains a Dafny lexer for pygments. It's intention is to be used with [minted](https://github.com/gpoore/minted).

## Requirements

- Python setuptools
  - on Debian: `sudo apt-get install python3-setuptools`

- pygments
  - on Debian: `sudo apt-get install python3-pygments`
  - alternative: `sudo easy_install Pygments`


## Setup

One-Shot installation via: `sudo python3 setup.py install` (copies the files).

Development installation via: `sudo python3 setup.py develop` (links to the files). Uninstall with `sudo python3 setup.py develop --uninstall`.


## Usage with minted

- install the minted package in your latex distribution
  - on Debian: `sudo apt-get install texlive-latex-extra`

Example usage:

```LaTeX
\usepackage{minted}

\newmintinline[dafnyinline]{dafny}{escapeinside=||}

Hello \dafnyinline{b := a[1..]}!
```

shell escape must be enabled (unless you use the draft mode), e.g. via `pdflatex -shell-escape`.
