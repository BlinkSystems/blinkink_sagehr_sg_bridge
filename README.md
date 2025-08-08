# sagehr_sg_bridge

Bridge between SageHR and SG

## Description

This application retrieves leave requests from SageHR and processes them. It runs periodically to fetch the latest leave requests and logs the details.

## Requirements

- Python 3.11
- pip

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd sagehr_sg_bridge
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Environment Variables

The following environment variables need to be set for the application to run correctly:

- `LOG_LEVEL`: The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) of the bridge.
- `SAGEHR_API_URL`: The base URL for the SageHR API.
- `SAGEHR_API_KEY`: The API key for the SageHR API.
- `SAGE_LEAVE_REQUEST_SYNC_INTERVAL`: The interval in seconds at which the bridge should sync leave requests.
- `SG_SITE_URL`: The base URL for the Shotgun site.
- `SG_SCRIPT_NAME`: The script name for the Shotgun API.
- `SG_SCRIPT_KEY`: The API key for the Shotgun script.

You can set these variables in your environment or create a `.env` file in the root of your project with the following content:

```env
LOG_LEVEL=INFO
SAGEHR_API_URL=https://api.sage.hr
SAGEHR_API_KEY=your_api_key
SAGE_LEAVE_REQUEST_SYNC_INTERVAL=60
SG_SITE_URL=https://your_shotgun_site_url
SG_SCRIPT_NAME=your_script_name
SG_SCRIPT_KEY=your_script_key
```

## Usage

To run the bridge, execute the following command:

```sh
python startup_dev.py
```

## Docker

### To deploy the application using Docker:
Build the Docker image:  
```sh 
docker build -t sagehr_sg_bridge .
```

Run the Docker container:  
```sh
docker run -e LOG_LEVEL=INFO -e SAGEHR_API_URL=https://api.sage.hr -e SAGEHR_API_KEY=your_api_key -e SAGE_LEAVE_REQUEST_SYNC_INTERVAL=60 -e SG_SITE_URL=https://your_shotgun_site_url -e SG_SCRIPT_NAME=your_script_name -e SG_SCRIPT_KEY=your_script_key sagehr_sg_bridge
```
