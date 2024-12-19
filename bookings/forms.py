from django import forms

from .models import Booking, Coupon, Event






class EventForm(forms.ModelForm):

  class Meta:

    model = Event

    fields = ['name', 'price_per_ticket']

    widgets = {

      'name': forms.TextInput(attrs={'placeholder': 'Enter event name'}),

      'price_per_ticket': forms.NumberInput(attrs={'placeholder': 'Enter ticket price'}),

    }



  def clean_price_per_ticket(self):

    price = self.cleaned_data.get('price_per_ticket')

    if price <= 0:

      raise forms.ValidationError("Price per ticket must be greater than 0.")

    return price




class BookingForm(forms.ModelForm):

  coupon_code = forms.CharField(max_length=50, required=False, label="Coupon Code")



  class Meta:

    model = Booking

    fields = ['event', 'number_of_tickets']



  def clean_number_of_tickets(self):

    tickets = self.cleaned_data.get('number_of_tickets')

    if tickets <= 0:

      raise forms.ValidationError("Number of tickets must be greater than 0.")

    return tickets















