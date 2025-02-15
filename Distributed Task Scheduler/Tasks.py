from celery import Celery
import time

# Set up Celery app with RabbitMQ as the broker and Redis for result backend
app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='redis://localhost:6379/0')

# Task definition for distributed scheduling
@app.task
def process_data(task_id):
    print(f"Processing task {task_id}...")
    time.sleep(10)  # Simulate time-consuming processing
    return f"Task {task_id} completed successfully!"

@app.task
def analyze_data(task_id):
    print(f"Analyzing task {task_id}...")
    time.sleep(15)  # Simulate analysis processing
    return f"Analysis of task {task_id} complete!"

# Main function to add tasks to the queue
if __name__ == "__main__":
    for task_id in range(1, 6):
        process_data.delay(task_id)  # Dispatch tasks asynchronously
        analyze_data.delay(task_id)  # Dispatch analysis tasks asynchronously
        print(f"Task {task_id} has been scheduled.")

    print("All tasks have been scheduled. Waiting for completion...")

