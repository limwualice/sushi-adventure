# Beverly Grove Sushi Adventure

Welcome to the Beverly Grove Sushi Adventure project! This project allows you to scrape data from Yelp using their API.

## Getting Started

To get started with this project, follow the instructions below:

### Prerequisites

- Python 3.x installed
- Yelp API access token

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/limwualice/data-engineering.git
   ```

2. Change to the project directory:

   ```shell
   cd data-engineering
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Create the configuration file:

   - Create a new file in the project directory called `config.py`.
   - Open the `config.py` file in a text editor.

5. Obtain the Yelp API access token:

   - Go to the Yelp Developer website (https://www.yelp.com/developers) and create an account if you haven't already.
   - Follow the instructions to create a new Yelp app and obtain an API access token.

6. Define the access token in the `config.py` file:

   - In the `config.py` file, define a variable named `ACCESS_TOKEN` and assign your Yelp API access token to it. For example:

     ```python
     ACCESS_TOKEN = "your-access-token-here"
     ```

7. Save the `config.py` file.

### Usage

1. Run the script:

   ```shell
   python yelp_scrape.py
   ```

2. The script will retrieve data from Yelp using the provided access token and display the results in the console.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
