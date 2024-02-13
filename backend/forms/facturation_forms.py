from django import forms

from backend.models.gestion_ecole import Career, StudentCareer
from backend.models.user_account import Student
from ..models.facturation import Invoice, Item, Regulations

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'default_amount', 'defaut_quantity', 'is_active', 'analytic_code', 'school']
        
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'type': 'text',
                    'id': 'label',
                    'class': 'form-control',
                    'name': 'label',
                    'placeholder': 'ex: Frais scolaire',
                    'required': True

                }
            ),
            'default_amount' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True

                }
            ),
            'defaut_quantity' : forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True

                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            ),
            'analytic_code': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }

class InvoiceForm(forms.ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        # Filtrer les niveaux en fonction de l'utilisateur connecté
        self.fields['career'].queryset = Career.objects.filter(sector__school=user.school)
        self.fields['item'].queryset = Item.objects.filter(school=user.school)
        student_ids = StudentCareer.objects.filter(academic_year__school=user.school, academic_year__status=True).values_list('student', flat=True).distinct()
        self.fields['student'].queryset = Student.objects.filter(id__in=student_ids)
    
    class Meta:
        model = Invoice
        fields = ['student', 'career', 'item', 'invoice_status', 'comment']
        widgets = {
            'student': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'career': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'item': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'invoice_status': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'5',
                    'rows':'5'
                }
            )
        }


class RegulationsForm(forms.ModelForm):
    class Meta:
        model = Regulations
        fields = ['invoice', 'student', 'payment_method', 'amount_payment', 'comment']
        widgets = {
            'invoice': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'student': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'amount_payment': forms.NumberInput(
                attrs={
                    'type':'number',
                    'class': 'form-control',
                    'required': True
                }
            ),
            'payment_method': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'4',
                    'rows':'2'
                }
            )
        }