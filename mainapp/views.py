from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse

def main(request):
    title = 'САФУ-Инжиниринг'
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         subject = f'Заявка с IM Consulting Group от {form.cleaned_data["full_name"]}'
    #         email = form.cleaned_data['email']
    #         message = f"Здравствуйте, меня зовут {form.cleaned_data['full_name']}\n" \
    #                   f"Контактный номер: {form.cleaned_data['phone']}\n" \
    #                   f"Email:  {form.cleaned_data['email']}\n\n" \
    #                   f"{form.cleaned_data['message']}\n\n" \
    #                   f""
    #         recipient_list = [settings.EMAIL_HOST_USER]
    #         send_mail(subject=subject, message=message, from_email=email, recipient_list=recipient_list)
    #         return HttpResponseRedirect(reverse('main'))
    # else:
    #     form = ContactForm()

    content = {
        "title": title,
        "media_url": settings.MEDIA_URL,
        # "form": form,
    }
    return render(request, "mainapp/index.html", content)
