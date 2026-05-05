# Course Materials Access

A small Streamlit app to provide access to course materials through access codes.

## Features

- Access-code-based distribution
- Two material versions
- Simple Streamlit interface
- Configuration through Streamlit secrets

## Project structure

```text
course-materials-access/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml.example
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Configuration

Create a local file:

```text
.streamlit/secrets.toml
```

Using this structure:

```toml
[app]
title = "Fundamentals Course"
start_time = "09:30"
end_time = "12:30"

[versions]
code_a = "Versión 1"
code_b = "Versión 2"
url_a = "https://drive.google.com/drive/folders/1piMw9q8DhNeBl_VkRdbVDJ9Km6Yx3a5r" 
url_b = "https://drive.google.com/drive/folders/16XvdxuI_3Z_AJKPzdwIGD8jipfLpLX97"
```

The real `secrets.toml` file should not be uploaded to GitHub.

## Author

PhD. Lucía Alvarez-Nuñez  
2026