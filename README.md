**!!! NOTE: This project is still under construction. The backend is functional, but not perfect. The frontend is still very much under development !!!**

Fun little side project to learn django-rest-framework and React.

The purpose of the application is to allow raffles to take place at large events where its difficult for participants to submit their names before hand.

The goal is to eliminate the need for authentication of users, and instead do a session based approach for both a raffle host and the participants.

**How to start a development server**

Requirements:
* Docker
* Docker Compose (comes pre-installed with Docker Desktop if you're on Windows, and I believe Mac OS)

After cloning the repository down to you machine, run the following command in your terminal:

```bash
docker-compose up -d

These are currently the default ports:
Django API - 8000
React Frontend - 3000
