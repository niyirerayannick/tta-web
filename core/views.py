from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    contact_form = ContactForm(request.POST or None)

    if request.method == "POST" and contact_form.is_valid():
        cleaned_data = contact_form.cleaned_data
        body = (
            "New website inquiry from TRANSTRADE AFRICA website.\n\n"
            f"Name: {cleaned_data['name']}\n"
            f"Email: {cleaned_data['email']}\n"
            f"Phone: {cleaned_data.get('phone') or 'Not provided'}\n"
            f"Subject: {cleaned_data['subject']}\n\n"
            f"Message:\n{cleaned_data['message']}"
        )
        email = EmailMessage(
            subject=f"TTA Website Inquiry: {cleaned_data['subject']}",
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[cleaned_data["email"]],
        )
        email.send(fail_silently=False)
        messages.success(request, "Thank you. Your message has been sent successfully.")
        return redirect("/#contact")

    if request.method == "POST":
        messages.error(request, "Please check the form and try again.")

    context = {
        "contact_form": contact_form,
        "activities": [
            "Agricultural Products",
            "Oil and Petroleum Products",
            "Metals and Minerals",
            "Deep-Sea Trading",
        ],
        "values": [
            "Integrity",
            "Ownership",
            "Teamwork",
            "Community Impact",
            "Innovation",
        ],
        "partners": [
            "Global Suppliers",
            "Agriculture Networks",
            "Energy Producers",
            "Metals & Minerals",
            "Logistics Partners",
            "Strategic Buyers",
        ],
        "offices": [
            {
                "country": "RWANDA",
                "address": "KK 4 Ave Gikondo, Kigugu I, Kigali.",
                "phones": [
                    "+250 788 358 601",
                    "+250 788 324 065",
                    "+250 784 799 316",
                ],
            },
            {
                "country": "ZIMBABWE",
                "address": "Unit 5 Madokero Business Park, Madokero, Harare.",
                "phones": ["+263 77 305 8006"],
            },
            {
                "country": "UAE",
                "address": "1403 Metropolis Tower, Burj Khalifa Street, Business Bay, Dubai.",
                "phones": [
                    "+971 58 565 5300",
                    "+971 55 382 8975",
                    
                ],
            },
        ],
    }
    return render(request, "core/home.html", context)
