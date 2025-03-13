FROM python:3.11-slim

# work directory

WORKDIR /app

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
