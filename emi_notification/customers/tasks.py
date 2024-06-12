from celery import shared_task
from django.core.mail import send_mail
from datetime import date, timedelta
from .models import Customer



@shared_task(name='customers.tasks.send_emi_reminders')
def send_emi_reminders():
    today = date.today()
    upcoming_date = today + timedelta(days=1)
    customers = Customer.objects.filter(emi_date=upcoming_date)
    emails_sent = 0
    
    for customer in customers:
        send_mail(
            'EMI Reminder',
            f'Dear {customer.name}, your EMI is scheduled on {customer.emi_date}, please make sure to submit it on time.',
            'your_email@example.com',
            [customer.email],
            fail_silently=False,
        )
        emails_sent += 1
    
    return f'{emails_sent} email(s) sent successfully.'
