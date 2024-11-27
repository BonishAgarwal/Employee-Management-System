from app.observers.base import Observer

class EmailNotification(Observer):
    
    def notify(self, data):
        print(f"Email Observer: {data}")
        # Implement the logic for sending email to a user
    
    def send_email():
        pass