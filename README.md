# tex_template

A LaTeX template for mathematical writing, based on `amsart`.

## Build

Build the document with `latexmk`:

```sh
latexmk -pdf main.tex
```

The bibliography uses `biblatex` with `biber`, so a complete TeX installation
should include both `latexmk` and `biber`.

## Structure

- `main.tex` is the root document.
- `sections/` contains section files included from `main.tex`.
- `figures/` is the recommended location for figures and other image assets.
- `My Library.bib` contains the BibTeX/BibLaTeX bibliography entries.
- `preamble/symbols.sty` defines common mathematical symbols.
- `preamble/environments.sty` defines theorem-like environments.
- `preamble/boxes.sty` defines reusable `tcolorbox` wrappers.
- `preamble/todos.sty` defines margin-note commands for drafting.
- `.vscode/latex.code-snippets` contains project snippets for VS Code.
- `conventions.md` records writing and typesetting conventions.

## Formatting

Format the LaTeX sources with:

```sh
tex-fmt --recursive
```

The formatter configuration lives in `tex-fmt.toml`.

## Python Helpers

The scripts `pytex_zip.py` and `pytex_unzip.py` depend on `pytex-merge`.
Install the Python dependency with:

```sh
python3 -m pip install -r requirements.txt
```

Then create a merged single-file version with:

```sh
python3 pytex_zip.py
```

Extract a merged file back into separate files with:

```sh
python3 pytex_unzip.py
```
