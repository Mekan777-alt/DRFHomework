from celery import shared_task
from django.core.mail import EmailMessage



@shared_task
def send_mail(project_id: int):
    from projects.models import Project
    from_email = 'mekan.mededov@mail.ru'
    project = Project.objects.get(id=project_id)

    message = EmailMessage(
        subject=f'Проект {project.name} профинансирован!',
        body='Ура!',
        from_email=from_email,
        to=[project.user.email]
    )

    message.send()
