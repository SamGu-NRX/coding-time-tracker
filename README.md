# Coding Time Tracker

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Windows](https://img.shields.io/badge/platform-Windows%2011-blue)

> **Track your coding time seamlessly and visualize your productivity on Google Calendar!**

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Scheduling](#scheduling)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

**Coding Time Tracker** is a Python-based application designed to monitor your active coding time in VSCode using Wakatime and automatically log your productive sessions to Google Calendar. This integration helps you maintain a clear record of your coding habits, enhancing productivity and time management.

## Features

- **Automatic Tracking**: Utilizes Wakatime's API to monitor coding activity.
- **Google Calendar Integration**: Logs coding sessions exceeding a configurable time threshold.
- **Configurable Thresholds**: Set minimum active time (default: 5 minutes) to log sessions.
- **Executable for Windows 11**: Runs seamlessly on Windows 11 as a standalone application.
- **Secure Configuration**: Manages sensitive information using environment variables.

## Demo

![Demo GIF](path_to_demo_gif_or_screenshot)

*Illustration of the application updating Google Calendar after a coding session.*

## Installation

### Prerequisites

- **Python 3.7+**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Wakatime Account**: [Sign Up](https://wakatime.com/signup)
- **Google Account**: Access to Google Calendar.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/coding-time-tracker.git
   cd coding-time-tracker
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate.bat
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Google Calendar API**

   - Follow the [Google Calendar API Setup Guide](#2-set-up-google-calendar-api-access) from the [Assistant's previous response](#2-set-up-google-calendar-api-access).

5. **Obtain Wakatime API Key**

   - Log in to your Wakatime account.
   - Navigate to [API Key](https://wakatime.com/settings/account).
   - Copy your **API Key**.

6. **Create a `.env` File**

   In the root directory, create a `.env` file:

   ```env
   WAKATIME_API_KEY=your_wakatime_api_key_here
   CALENDAR_ID=primary
   MINUTES_THRESHOLD=5
   ```

## Configuration

### `.env` File

Manage your sensitive configurations in the `.env` file to keep them secure and easily configurable.

```env
WAKATIME_API_KEY=your_wakatime_api_key_here
CALENDAR_ID=primary
MINUTES_THRESHOLD=5
```

- **WAKATIME_API_KEY**: Your Wakatime API key.
- **CALENDAR_ID**: Google Calendar ID (`primary` for your main calendar).
- **MINUTES_THRESHOLD**: Minimum minutes of active coding to log (default: 5).

## Usage

### Running the Application

To run the application manually:

1. **Activate the Virtual Environment**

   ```bash
   venv\Scripts\activate.bat
   ```

2. **Execute the Script**

   ```bash
   python src/main.py
   ```

   The first run will prompt you to authorize access to your Google Calendar. Follow the on-screen instructions to complete the authentication.

### Wrapping as an Executable

To create a standalone Windows executable:

1. **Navigate to the `src/` Directory**

   ```bash
   cd src
   ```

2. **Run PyInstaller**

   ```bash
   pyinstaller --onefile --add-data "../credentials/credentials.json;credentials" main.py
   ```

3. **Locate the Executable**

   The executable `main.exe` will be in the `dist/` folder. Move it to the root directory for easy access.

## Scheduling

Automate the execution of **Coding Time Tracker** using Windows Task Scheduler to run at regular intervals.

### Steps

1. **Open Task Scheduler**

   - Press `Win + S`, type **Task Scheduler**, and open it.

2. **Create a New Task**

   - **Name**: `Coding Time Tracker`
   - **Description**: Automatically tracks coding time and updates Google Calendar.

3. **Configure Triggers**

   - **Begin the task**: On a schedule.
   - **Settings**:
     - **Daily**.
     - **Repeat task every**: 10 minutes.
     - **For a duration of**: Indefinitely.

4. **Configure Actions**

   - **Action**: Start a program.
   - **Program/script**: Path to `main.exe` (e.g., `C:\path\to\coding-time-tracker\main.exe`).

5. **Finalize**

   - Click **OK**.
   - Enter your Windows account password if prompted.

*The application will now run every 10 minutes, tracking and logging your coding sessions automatically.*

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

*Ensure your code follows the project's coding standards and includes appropriate documentation.*

## License

This project is licensed under the [MIT License](LICENSE).


### Action Items

- [ ] Logging: Integrate Python's logging module to maintain logs for debugging and monitoring.

- [ ] Error Notifications: Notify yourself via email or messaging platforms (e.g., Slack) in case of errors.

- [ ] GUI Interface: Develop a simple GUI using frameworks like Tkinter or PyQt for easier configuration.

- [ ] Event Deduplication: Implement logic to prevent duplicate events in Google Calendar.

- [ ] Multiple Project Support: Categorize events based on different projects or programming languages.

