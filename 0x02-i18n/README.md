Curriculum <br>
**Short Specializations** <br>


# Project Title: 0x02-i18n - Flask Internationalization (i18n)

## Project Description

The **0x02-i18n** project focuses on internationalization (i18n) and localization in Flask applications. It involves creating a Flask web application that supports multiple languages, allows users to log in, and displays content tailored to the user's language and time zone preferences. The project tasks cover basic Flask setup, Babel integration, URL parameter handling, user login emulation, and displaying the current time in different time zones.

## Project Structure

The project directory is organized as follows:

- **/templates**: Contains HTML templates for the Flask application.
  - **0-index.html**: Basic template displaying "Welcome to Holberton" as the page title and "Hello world!" as a header.
  - **1-index.html, 2-index.html, 3-index.html, 4-index.html, 5-index.html, 6-index.html, 7-index.html**: Templates for different tasks with appropriate placeholders.
- **/translations**: Contains translation files for different languages.
  - **en/LC_MESSAGES/messages.po, fr/LC_MESSAGES/messages.po**: Translation files for English and French.
- **app.py**: Flask application script containing route handlers, localization, and user login emulation logic.
- **babel.cfg**: Configuration file for Babel.
- **README.md**: Project documentation providing an overview, setup instructions, and usage guidelines.

## Tasks Overview

### 0. Basic Flask App
- Created a basic Flask app with a single route (/) and an index.html template displaying "Welcome to Holberton" as the page title and "Hello world!" as a header.

### 1. Basic Babel Setup
- Installed Flask Babel extension.
- Configured available languages in the app using the Config class.
- Set default locale to "en" and timezone to "UTC".

### 2. Get Locale from Request
- Implemented a `get_locale` function to determine the best match for supported languages based on request.accept_languages.

### 3. Parametrize Templates
- Parametrized templates using `_` or `gettext` functions.
- Created translation files for English and French.
- Compiled translation dictionaries for different languages.

### 4. Force Locale with URL Parameter
- Implemented a way to force a specific locale using the `locale` URL parameter.
- Tested different translations by visiting URLs with `?locale=[fr|en]`.

### 5. Mock Logging In
- Emulated user login system by creating a mock user table.
- Implemented `get_user` function to get user information based on the login_as URL parameter.
- Set user information as a global variable in Flask.g.user using a before_request function.
- Displayed different messages based on user login status.

### 6. Use User Locale
- Updated `get_locale` function to prioritize user's preferred locale if available.
- Tested different translations by logging in as different users.

### 7. Infer Appropriate Time Zone
- Defined a `get_timezone` function and used babel.timezoneselector decorator.
- Validated time zone from URL parameters or user settings.
- Defaulted to UTC if no valid time zone was found.

### 8. Display the Current Time (Advanced)
- Displayed the current time on the home page based on the inferred time zone.
- Utilized translations to display the current time message in English and French.

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/username/0x02-i18n.git
   cd 0x02-i18n
   ```

2. **Install Dependencies:**
   ```
   pip install Flask flask-babel pytz
   ```

3. **Run the Application:**
   ```
   python app.py
   ```

4. **Access the Application:**
   Open your web browser and visit `http://localhost:5000` to explore the i18n-enabled Flask application.

## Usage

- **Locale Selection**: The application allows users to switch between English and French translations using the `?locale=[fr|en]` URL parameter.
- **User Login**: Emulated user login by visiting URLs with `?login_as=[user_id]` to see personalized messages based on the logged-in user.

## Localization and Time Zone Guidelines

- **Translation Parametrization**: Ensure all templates are parametrized using `_` or `gettext` functions for dynamic content rendering based on selected language.
- **Translation Files**: Maintain separate translation files for each supported language.
- **User Preferences**: Implement logic to allow users to set their preferred language and time zone through settings in the application.

## Contributing

Contributions are welcome! If you find issues or have suggestions for improvements, please open an issue or create a pull request on the GitHub repository.

---

**Note:** Replace `https://github.com/username/0x02-i18n.git` with the actual URL of your GitHub repository. Modify the project structure and content as needed to match your specific project requirements.