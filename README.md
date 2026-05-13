# Course Materials Access

A small Streamlit application to provide controlled access to course materials through access codes.

## Overview

This project provides a simple interface where users enter an access code and receive the corresponding course resource.

The app is designed to keep configuration values outside the source code by using Streamlit Secrets.

## Features

- Access-code-based resource distribution
- Support for two material versions
- Simple Streamlit interface
- External configuration through Streamlit Secrets
- Lightweight project structure

## Project structure

```text
course-materials-access/
├── app.py
├── requirements.txt
└── README.md
```

## How it works

The app reads the access codes and resource URLs from Streamlit Secrets.

When a user enters a valid code, the app displays the corresponding resource link.

## Run locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Configuration

This application requires a specific configuration structure in Streamlit Secrets

```toml

## Technologies

- Python
- Streamlit
- pandas

## Author

PhD. Lucía Alvarez-Nuñez  
2026
