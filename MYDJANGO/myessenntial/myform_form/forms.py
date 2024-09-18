from django import forms

JOBS = (
    ('Python', 'Python Developper'),
    ('JavaScript', 'JavaScript Developper'),
    ('Java', 'Java Developper')
)
CITIES = (
    ('Tanger', 'Capitale du nord'),
    ('Fes', 'Capitale culturelle'),
    ('Rabat', 'Capitale administrative'),
    ('Casablanca', 'Capitale economique')
)
LANGUAGES = (
    ('Ar', 'Arabic'),
    ('En', 'English'),
    ('sp', 'Spanish'),
    ('Fr', 'French')
)


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
    jobs = forms.ChoiceField(choices=JOBS)
    city = forms.ChoiceField(choices=CITIES)
    language = forms.ChoiceField(choices=LANGUAGES)
    cgu_accept = forms.BooleanField(initial=True)


class SignupFormWidget(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    city = forms.MultipleChoiceField(choices=CITIES, widget=forms.CheckboxSelectMultiple)
    language = forms.MultipleChoiceField(choices=LANGUAGES, widget=forms.SelectMultiple)
    cgu_accept = forms.BooleanField(initial=True)


class SignupFormData(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
    job = forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    language = forms.MultipleChoiceField(choices=LANGUAGES, widget=forms.CheckboxSelectMultiple)
    cgu_accept = forms.BooleanField(initial=True)