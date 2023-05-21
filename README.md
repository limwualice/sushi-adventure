# Los Angeles Sushi Adventure!

Welcome to the Los Angeles Sushi Adventure project! This project allows you to scrape data from Yelp using their API, run a machine learning model to predict which sushi restaurants the user would enjoy, and then output 5 sushi restaurants!

## Getting Started

To get started with this project, follow the instructions below:

### Prerequisites

- Python 3.x installed
- Yelp API access token

### Installation

1. Clone the repository:

git clone https://github.com/limwualice/sushi-adventure.git

2. Change to the project directory:

cd sushi-adventure


3. Install the required dependencies:

pip install -r requirements.txt

4. Create the configuration file:
- Create a new file in the project directory called `config.py`.
- Open the `config.py` file in a text editor.

5. Obtain the Yelp API access token:
- Go to the Yelp Developer website (https://www.yelp.com/developers) and create an account if you haven't already.
- Follow the instructions to create a new Yelp app and obtain an API access token.

6. Define the access token in the `config.py` file:
- In the `config.py` file, define a variable named `ACCESS_TOKEN` and assign your Yelp API access token to it. For example:
  ```
  ACCESS_TOKEN = "your-access-token-here"
  ```
- Save the `config.py` file.

### Usage

Run the script:

python3 yelp_scrape.py


The script will retrieve data from Yelp using the provided access token and display the results in the console.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Deployment on Google Cloud Platform (GCP)

To deploy the Los Angeles Sushi Adventure project on Google Cloud Platform (GCP), follow these additional steps:

1. Set up a GCP account and project.
2. Build and push a Docker image for the project.
3. Deploy the Docker image on GCP using Cloud Run.
4. Update the necessary configurations and environment variables to work with the GCP deployment.

For detailed deployment instructions, please refer to the [GCP Deployment Guide](deployment-guide.md).

## License

This project is licensed under the MIT License.
