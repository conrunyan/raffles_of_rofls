FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend/
WORKDIR /app/backend/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY ./raffle_backend/requirements.txt /app/backend/
RUN pip install -r requirements.txt
COPY . /app/backend/
COPY ./raffles_of_rofls /app/backend/
COPY ./raffle_backend /app/backend/
COPY ./manage.py /app/backend/

# Create plank DB

RUN python manage.py makemigrations
RUN python manage.py migrate
