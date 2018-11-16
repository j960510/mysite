from django import forms

from sinabro.models import ConsultationRequest



class ConsultationRequestForm(forms.ModelForm):
    """
        bootstrap 을 사용하기위해 form 의 태그에 class 추가함.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['region'].widget.attrs['class'] = 'form-control'
        self.fields['reservation_time'].widget.attrs['class'] = 'form-control'
        self.fields['reservation_time'].widget.attrs['id'] = 'datepicker'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'

    class Meta:

        model = ConsultationRequest
        fields = ['region', 'reservation_time', 'name', 'phone_number', 'note']
        
        
        


    
    
