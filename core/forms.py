from django import forms


class userinput(forms.Form):
    q = forms.IntegerField(required=True,label='Customer ID')

    def __init__(self, *args, **kwargs):
        super(userinput, self).__init__(*args, **kwargs)
        self.fields['q'].widget = forms.TextInput(attrs={'placeholder': 'Set Id', 'style' :'margin-left: 50px;margin-right: 10px;width:50%'})
        #change one
        #change two
        #change 4
        # change 5
        # change 6
