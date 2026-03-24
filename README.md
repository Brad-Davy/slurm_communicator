# Slurm Communicator

## Overview
Slurm Communicator is a tool designed to facilitate communication with the Slurm workload manager. It provides an easy-to-use interface for monitoring the use of the cluster.

## Database Integration
For simplicity, the Slurm Communicator tool uses csv files to keep track of outputs. This is done for, as already mentioned, simplicity but also to make extracting this data simple.

## Features
- Determine how many cores are currently in use.
- Determine how long jobs are running for and how much time is being requested.
- Determine the usage of each partition.


## Installation
To install Slurm Communicator, clone the repository and install the required dependencies:
```bash
git clone https://github.com/yourusername/slurm_communicator.git
cd slurm_communicator
pip3 install -r requirements.txt
```

## Usage
To use Slurm Communicator, run the main script with the appropriate commands:
```bash
python3 -m slurm_communicator.main
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact
For questions or support, please open an issue on the GitHub repository or contact the maintainer bdavy@ocf.co.uk.
