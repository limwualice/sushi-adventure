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

## Deployment to Google Cloud Platform (GCP)

To deploy your Los Angeles Sushi Adventure project to Google Cloud Platform, follow the steps below:

Prerequisites

    You should have a GCP account with the necessary permissions to create and configure resources.
    Ensure that you have the Google Cloud SDK (gcloud) command-line tool installed and configured with your GCP project credentials. You can install the SDK by following the instructions here: Installing Google Cloud SDK.

Building the Docker Image

    Make sure you have Docker installed on your local machine.
    Open a terminal or command prompt and navigate to the root directory of your project.
    Build your Docker image using the following command:

    docker build -t gcr.io/[PROJECT_ID]/sushi-adventure-app:[TAG] .

    Replace [PROJECT_ID] with your GCP project ID and [TAG] with a version or tag name for your image.

Pushing the Docker Image to Container Registry

    After the Docker image is built successfully, authenticate Docker to use your GCP project's Container Registry. Run the following command:

gcloud auth configure-docker

Tag the Docker image with the GCR registry path:


docker tag gcr.io/[PROJECT_ID]/sushi-adventure-app:[TAG]

Push the Docker image to Container Registry:

    docker push gcr.io/[PROJECT_ID]/sushi-adventure-app:[TAG]

    The image will be uploaded to your GCP project's Container Registry.

Deploying to Google Cloud Run

    Open a terminal or command prompt.

    Deploy your containerized application to Google Cloud Run using the following command:

    diff

    gcloud run deploy sushi-adventure \
    --image gcr.io/[PROJECT_ID]/sushi-adventure-app:[TAG] \
    --platform managed \
    --port=5001

    Replace [PROJECT_ID] with your GCP project ID and [TAG] with the version or tag of your Docker image.

    Follow the prompts to select your preferred region and confirm the deployment.

    Once the deployment is complete, you will receive a URL where your application is accessible.

Accessing Your Deployed Application

    After the deployment is successful, you can access your deployed application using the URL provided by Google Cloud Run.

Congratulations! Your Los Angeles Sushi Adventure project is now deployed on Google Cloud Platform.

## License

This project is licensed under the MIT License.
