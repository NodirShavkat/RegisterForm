from django import forms
from .models import Volunteer


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        labels = {
            'full_name': 'Full Name',
            'date_of_birth': 'Date of Birth',
            'phone': 'Phone Number',
            'telegram': 'Telegram username',
            'email': 'Email Address',
            'study_work': 'Place of Study / Work (University, faculty, or job position)',
            'english_level': 'English Level',
            'additional_languages': 'Additional Foreign Languages',
            'has_experience': 'Do you have previous experience volunteering at international or national events?',
            'previous_experience': 'If yes, describe where and what role',
            'why_volunteer': 'Why do you want to volunteer for IChO 2026?',
            'cv_file': 'Please upload your CV',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select your date of birth'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+998 XX XXX XX XX'
            }),
            'telegram': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '@username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com'
            }),
            'study_work': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'University name, faculty or job position'
            }),
            'english_level': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'A1, A2, B1, B2, C1 or C2'
            }),
            'additional_languages': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional'
            }),
            'has_experience': forms.RadioSelect(choices=[
                (True, 'Yes'),
                (False, 'No'),
            ]),
            'previous_experience': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your previous volunteering experience',
                'rows': 3
            }),
            'why_volunteer': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Explain your motivation',
                'rows': 4
            }),
            'cv_file': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }