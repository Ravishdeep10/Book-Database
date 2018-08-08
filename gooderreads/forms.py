from django import forms


class BookForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    book_title = forms.CharField(label='Book Title', max_length=100)
    isbn = forms.CharField(label='ISBN', max_length=100)
    review = forms.CharField(widget=forms.Textarea(attrs={'size':10, 'title': "Your Review"}))

    def get_name(self):
        return self.cleaned_data['your_name']

    def get_title(self):
        return self.cleaned_data['book_title']

    def get_review(self):
        return self.cleaned_data['review']

    def get_isbn(self):
        return self.cleaned_data['isbn']
