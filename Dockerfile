# Use the image we originally intended to use
FROM python:3.8.0-slim-buster

# Change our working directory to /code/app for simplicity
WORKDIR /app

# Simplify the pip install (we do NOT want upgrades)
RUN pip install fastapi==0.92.0
RUN pip install uvicorn==0.20.0

# Copy code in app directory to app directory under code in image
COPY ./app/File_IO.py /app/File_IO.py
COPY ./app/File_IO_API.py /app/File_IO_API.py

RUN mkdir /app/files

# Start from app directory now. Set host and port to typical settings
CMD ["uvicorn", "File_IO_API:app", "--host", "0.0.0.0", "--port", "8000"]
