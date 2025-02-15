# Distributed Task Scheduler with Celery and RabbitMQ

## Overview
This project implements a distributed task scheduling system using Celery and RabbitMQ. It demonstrates how tasks are scheduled and processed across multiple workers.

## Files:
- `tasks.py`: Python script defining the Celery tasks and their execution logic.
- `README.md`: Project documentation.

## Prerequisites:
- Celery
- RabbitMQ or Redis (for task queue management)
- Python 3.x

## Usage:
1. Install the required Python dependencies via `pip install -r requirements.txt`.
2. Start RabbitMQ and run the Celery worker using the command: `celery -A tasks worker --loglevel=info`.
3. Run the `tasks.py` script to enqueue tasks.
