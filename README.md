# pygments-dafny

## About

This repository contains a [Dafny](https://github.com/dafny-lang/dafny) lexer for [Pygments](https://github.com/pygments/pygments). It's motivation is to be used with [minted](https://github.com/gpoore/minted) for simple programs.

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

## Status

Developed on Debian 11 with Pygments 2.7.1 and Dafny 3.3.0.

Coverage of the Dafny language is still incomplete.

This repository will not be actively maintained. Small contibutions / PRs are welcome, larger contibutions / PRs might justify a fork with a note here to archive this repo.
