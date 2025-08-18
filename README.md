# readylist

A state graph editor.

## Installation

```bash
pip install .
```

Also need sudo apt-get install graphviz libgraphviz-dev 

## Usage
source ./venv/bin/activate
readylist-cli --greet Alice
readylist-cli --version

## Development
source ./venv/bin/activate

Run tests with 
pip install -e . This builds a wheel using the pyproject.toml file)
pytest

