FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app/backend/
WORKDIR /app/backend/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt /app/backend/
RUN pip install -r requirements.txt
COPY . /app/backend/