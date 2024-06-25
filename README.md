# Information Retrieval: Spell Correction and Wildcard Queries

## Overview
This project focuses on building an Information Retrieval (IR) system capable of processing, indexing, and querying text data. It includes various components for preprocessing data, creating indexes, and handling queries to retrieve relevant information efficiently.

## Features
- **Data Preprocessing**: Tools to clean and prepare text data for indexing.
- **Indexing**: Efficient indexing mechanisms to support quick retrieval of information.
- **Query Handling**: Support for various query types to retrieve the most relevant documents.
- **Notebooks**: Jupyter notebooks for experimenting and reporting.

## Installation
To get started with the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Amir-Entezari/IR-wildcards-and-spell-correction.git
    ```
2. Navigate to the project directory:
    ```sh
    cd IR-wildcards-and-spell-correction
    ```
3. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Description
The Information Retrieval Project is designed to demonstrate the core functionalities of an IR system. It includes modules for preprocessing text data, indexing documents, and processing queries to retrieve relevant results. The project is organized as follows:

- **src/**: Contains the source code for preprocessing, indexing, querying, and utility functions.
    - `preprocessing.py`: Functions to clean and prepare text data.
    - `indexing.py`: Functions to create and manage indexes.
    - `querying.py`: Functions to handle and process search queries.
    - `utils.py`: Utility functions for various common tasks.
- **notebooks/**: Contains Jupyter notebooks for experiments and reporting.
    - `experiments.ipynb`: Notebook for running experiments on the IR system.
    - `report.ipynb`: Notebook for generating reports on the IR system's performance.


## Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss any changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
