from django import forms

class prof_perf_form(forms.Form):
    """Professor Performances search form"""
    pname = forms.CharField(label="Professor Name", max_length=20, required=True)
    year = forms.IntegerField(label="Year", required=True)
    SEMESTER = ((1,'Fall'),(2,'Spring'))
    sem = forms.ChoiceField( label="Semester",choices=SEMESTER)

