# Binary-Ninja-Marimo-Analysis-Notebook
Binary Ninja Marimo Analysis Notebook

Marimo notebook for Binary Ninja to analyse headless the extracted artefacts from Binary Ninja scripting.

## Clone the repo
git clone https://github.com/meerkatone/Binary-Ninja-Marimo-Analysis-Notebook.git

## Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

## Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

## Setup venv and Marimo
uv venv venv_marimo --python 3.12

source /venv_marimo/headless/bin/activate

cd Binary-Ninja-Marimo-Analysis-Notebook

uv pip install marimo

## Launch the notebook
marimo edit ./binary_ninja_analysis.py

The notebook will ask you to install the required dependencies via uv.
