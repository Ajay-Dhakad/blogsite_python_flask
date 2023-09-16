# My Flask Blog

Welcome to **My Flask Blog**, a simple blog project built using Flask, a Python web framework. This project allows you to create, edit, and manage blog posts. It includes features like user authentication, email notifications, and more.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This Flask blog project is designed for simplicity and flexibility. It enables you to:

- Create and edit blog posts with ease.
- Allow user authentication for administrators.
- Receive email notifications for new contact messages.
- Organize your posts with pagination.
- Upload featured images for your blog posts.

## Features

- **User Authentication**: Administrators can log in to create, edit, and manage blog posts.

- **Blog Posts**: Create and edit blog posts using a user-friendly interface.

- **Contact Form**: Includes a contact form for users to send messages.

- **Email Notifications**: Receive email notifications when a new contact message is received.

- **Pagination**: Display a specified number of blog posts per page.

- **Image Upload**: Allows image uploads for blog post featured images.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python (3.6 or higher)
- Git
- A Gmail account (for email notifications)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/my-flask-blog.git
   cd my-flask-blog

    Create a Virtual Environment (optional but recommended): python -m venv venv

    Activate the Virtual Environment:

        On Windows: .\venv\Scripts\activate

        On macOS and Linux:

    Install Dependencies:

        pip install -r requirements.txt


## Configuration:

2. **Create a Configuration File**:

            Create a config.json file in the templates directory with the following structure:

                            {
                  "params": {
                    "secret_key": "your_secret_key",
                    "mail_username": "your_email@gmail.com",
                    "mail_password": "your_email_password",
                    "mail_recipient": "recipient_email@gmail.com",
                    "local_uri": "sqlite:///nerdycoder",
                    "prod_uri": "your_production_database_uri",
                    "admin_user": "admin_username",
                    "admin_pass": "admin_password",
                    "upload_folder": "static/uploads",
                    "posts_per_page": 5
                  }
                }
        replace the placeholders with your own values.


## Initialize the Database:

      NO WORRIES THE CODE WILL AUTOMATICALLY GENERATE ITS DATABASE AS SQLITE YOU CAN CHANGE ACCORDING TO YOU

## Usage


1. **Visit the homepage to view blog posts and navigate to individual post pages.**
2.**Use the "/dashboard" route to log in as an administrator and manage blog posts.**
3.**To create a new blog post or edit an existing one, log in as an administrator and access the "/edit" route.**
4.**Use the "/contact" route to send messages through the contact form.**
5.**Log out using the "/logout" route.**


## Contributing

Contributions are welcome! If you have suggestions or would like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Enjoy building your blog with Flask! If you have any questions or need further assistance, feel free to reach out.



