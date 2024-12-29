# Mental Illness and Happiness Prediction

#### Technologies Used: Python, Flask, HTML5, CSS3, JavaScript, MySQL

### Project Overview

- The **Mental Illness and Happiness Prediction** project aims to predict the severity levels of mental health conditions, such as depression, anxiety, and stress, using machine learning models. The project employs **AdaBoost** and **Support Vector Machine (SVM)** algorithms to provide accurate predictions, offering valuable insights into mental well-being. Additionally, the project uses linear regression to predict happiness level, helping to understand the relationship between mental health and overall happiness.
- Project Demo is available [here](https://drive.google.com/file/d/1SBtCfBzXo0h1PzaLPApbVTBKBAZ8SjGC/view?usp=sharing).

### Key Features

- **Machine Learning Model:**
  - Built a machine learning model using AdaBoost and SVM algorithm to predict the severity levels of depression, anxiety, and stress.
  - Achieved an impressive 94% accuracy in predicting mental health conditions based on user inputs.
- **Web Application:**
  - Developed a Flask-based web application to provide users with a platform for tracking mental health and receiving predictions.
  - Integrated MySQL for efficient storage and management of user data, ensuring a smooth interaction between the front end and back end.
- **User Interface:**
  - Utilized HTML5, CSS3, and JavaScript to create an interactive and responsive user interface.
  - Ensured smooth navigation and a positive user experience, allowing users to track their mental health and receive personalized predictions.

### Functionality

- **User Input:**
  - For mental illness prediction, users input their data based on the standard DASS-21 scale, which includes questions related to depression, anxiety, and stress. This data is used to predict the severity of the user’s mental health condition.
  - For happiness prediction, users provide responses to the Flourishing Scale to assess their happiness level, which is used to calculate a happiness score.
- **Prediction Results:**
  - Based on the input, the model classifies the user’s mental health condition into one of five levels: Normal, Mild, Moderate, Severe, Extremely Severe.
  - For happiness prediction, the model calculates a score that reflects the user’s overall happiness.
- **Data Management:**
  - All user data is securely stored in MySQL, allowing for continuous tracking and analysis.

### Technologies Used

- **Python:** For developing the machine learning model and backend logic.
- **Flask:** To build the web application and manage the server-side operations.
- **HTML5, CSS3, JavaScript:** For designing the interactive and responsive front-end.
- **MySQL:** For storing user data and ensuring seamless interaction between the front end and back end.

### Conclusion

- This project combines machine learning and web development to offer a meaningful solution for tracking and predicting mental health conditions. By integrating a powerful machine learning model with a user-friendly web interface, it provides users with valuable insights into their mental well-being.

## How to Run the App

To run the Mental Illness and Happiness Prediction app, follow these steps:

1.  **Install Dependencies:**

    - First, make sure you have Python installed on your system. You can download Python from the official website.
    - Create a virtual environment (optional but recommended):

          python -m venv venv

    - Activate the virtual environment:

      - On Windows:

            venv\Scripts\activate

      - On macOS/Linux:

            source venv/bin/activate

    - Install the required dependencies by running:

          pip install -r requirements.txt

      - The requirements.txt file includes all the necessary libraries, such as Flask, scikit-learn, MySQL connector, and others.

2.  **Set Up MySQL Database:**

    - Create a MySQL database for the app. In the database folder, you will find SQL queries to create the necessary tables. Run the queries in your MySQL database.
    - Create a .env file in the root directory of the project and set up the variables. An example is provided in the .env.example file.

3.  **Run the Application:**

    - You can run the app directly from your IDE (such as PyCharm, VSCode, etc.) by running the main.py file.
    - Alternatively, you can run the app using Gunicorn for a production-ready setup:

          gunicorn app:app

      - This command will start the app using Gunicorn, which is a WSGI HTTP server for Python web applications.

4.  **Access the App:**

    - Once the app is running, the URL will pop up on the screen, allowing you to interact with the app.

5.  **Credentials:**

    - For admin access, use the credentials provided in the admin table in the database.
    - For regular users, you can sign up through the website and use the credentials you create.

That’s it! You can now start using the Mental Illness and Happiness Prediction app to predict mental health conditions and happiness levels based on user input.
