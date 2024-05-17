# Password Manager

Welcome to the Password Manager App! This application allows you to securely manage your passwords for different platforms. It uses MongoDB Atlas for database storage, `pyqrcode` for creating QR codes, and `cryptography` for encryption.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
  - [Add Password](#add-password)
  - [Update Password](#update-password)
  - [Delete Password](#delete-password)
  - [Show Passwords](#show-passwords)
  - [Generate Password](#generate-password)
  - [Create QR Code](#create-qr-code)
  - [Encrypt Password](#encrypt-password)
- [Technologies Used](#technologies-used)
- [License](#license)

## Introduction

This Password Manager App is designed to help users securely store, manage, and retrieve their passwords. It also includes functionality to generate strong passwords and create QR codes for easy access.

## Features

- **Add Password**: Store new passwords with platform and username.
- **Update Password**: Update existing passwords by their unique ID.
- **Delete Password**: Remove passwords from the database.
- **Show Passwords**: Display stored passwords.
- **Generate Password**: Automatically generate strong passwords.
- **Create QR Code**: Generate QR codes for passwords.
- **Encrypt Password**: Securely encrypt passwords before storing them.

## Setup

To set up the project, you need to have Python installed along with the required libraries.

1. Install Python from [python.org](https://www.python.org/).
2. Install the required libraries:
   ```bash
   pip install pymongo pyqrcode cryptography
