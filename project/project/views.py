from django.shortcuts import render

def projects(request):
    # These example cards can be edited as your projects grow.
    project_list = [
        {
            "name": "Car Management System",
            "description": (
                "A practice system for organising vehicle and infraction "
                "information. I am learning how to connect Django pages "
                "with database records."
            ),
            "technologies": "Python, Django, SQL",
            "image": "",
        },
        {
            "name": "Python Object-Oriented Projects",
            "description": (
                "Small programs that use classes and objects to represent "
                "real-world ideas and keep code organised."
            ),
            "technologies": "Python, Object-Oriented Programming",
            "image": "",
        },
        {
            "name": "Personal Portfolio Website",
            "description": (
                "This website introduces me, presents my learning projects, "
                "and provides a contact page."
            ),
            "technologies": "Python, Django, HTML, CSS",
            "image": "",
        },
    ]

    # Send the project list to the HTML template.
    return render(request, "project/projects.html", {"project_list": project_list})
