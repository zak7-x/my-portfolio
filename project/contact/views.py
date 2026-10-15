from django.shortcuts import render
from django.core.mail import send_mail


def contact(request):
    success_message = ""

    if request.method == "POST":
        # Get the information entered in the form.
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and subject and message:

            # Prepare the email content.
            email_message = (
                    "Name: " + name + "\n"
                                      "Email: " + email + "\n\n"
                    + message
            )

            # Send the email to your Gmail inbox.
            send_mail(
                subject,
                email_message,
                None,
                ["zakwaanmohammad7@gmail.com"],
            )

            # Display a success message.
            success_message = "Your message has been sent!"
        else:
            success_message = "Please complete every field."

    return render(
        request,
        "contact/contact.html",
        {"success_message": success_message},
    )
