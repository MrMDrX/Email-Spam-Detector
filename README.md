# Email Spam Detector

Welcome to the Email Spam Detector project repository! This project focuses on building a spam detection system using natural language processing techniques. The detector analyzes text data to classify emails as either spam or legitimate (ham).

## Project Structure

- **data**: Contains the dataset used for training and testing (`spam.csv`).
- **email-spam-detector.ipynb**: Jupyter Notebook containing the main code and documentation.
- **main.py**: Python script for running the spam detection model.
- **models**: Directory to store trained model files (`model.pkl` and `vectorizer.pkl`).
- **README.md**: You are here! Provides an overview of the project.
- **requirements.txt**: Lists project dependencies for easy environment setup.
- **screenshots**: Contains screenshots for illustration (`ham.png` and `spam.png`).
- **static**: Static files for the web application.
  - **img**: Images used in the web application (`logo-64x64.png`).
- **templates**: HTML templates for the web application.
  - **index.html**: Main page template.

## Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MrMDrX/Email-Spam-Detector.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Email-Spam-Detector
   ```

3. **Create and Activate a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the spam detector:**

   ```bash
   python main.py
   ```

## Web Application

The project includes a simple web application for testing the spam detector. The web application is built using Flask and integrates HTMX for dynamic content updates. Access the application by running `main.py` and visiting [http://localhost:5000](http://localhost:5000) in your web browser.

## Screenshots

- **Ham (Legitimate Email)**
  ![Ham](https://github.com/MrMDrX/Email-Spam-Detector/blob/main/screenshots/ham.png)

- **Spam**
  ![Spam](https://github.com/MrMDrX/Email-Spam-Detector/blob/main/screenshots/spam.png)

## Notes

- The model and vectorizer files (`model.pkl` and `vectorizer.pkl`) in the `models` directory are essential for the spam detection functionality.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open issues for bug reports or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding!
