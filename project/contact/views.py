from django.shortcuts import render

def contact(request):
    # Start with an empty message for the form.
    success_message = ""

    # This block runs when the visitor submits the form.
    if request.method == "POST":
        # Read the submitted fields from the form.
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # Check that every field has been filled in.
        if name and email and subject and message:
            success_message = (
                "Thank you, " + name + ". The form was submitted successfully. "
                "This starter project does not email the message yet."
            )
        else:
            success_message = "Please complete every field before submitting."

    # Show the contact page and any message above the form.
    return render(
        request,
        "contact/contact.html",
        {"success_message": success_message},
    )
