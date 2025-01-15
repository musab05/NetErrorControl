# NetErrorControl

NetErrorControl is a Python-based project designed to implement error control mechanisms for network communications. The project aims to provide reliable data transmission by detecting and correcting errors that may occur during data transfer over networks.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Implementation of various error control techniques such as parity checks, checksums, and Hamming codes.
- Support for both error detection and error correction.
- Customizable parameters for different network scenarios.
- Comprehensive test cases to validate the correctness of the implemented algorithms.

## Technologies Used

- **Python**: Main programming language used for implementing the error control algorithms.
- **Nix**: Used for managing dependencies and environments.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/musab05/NetErrorControl.git
    ```
2. Navigate to the project directory:
    ```sh
    cd NetErrorControl
    ```
3. Set up the environment using Nix (optional but recommended):
    ```sh
    nix-shell
    ```

## Usage

1. Run the main script to execute the error control algorithms:
    ```sh
    python main.py
    ```
2. Customize the parameters in the configuration file (`config.json`) to suit your network scenario.
3. Check the output in the console or log files for the results of the error control processes.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add your feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```
5. Open a pull request.
