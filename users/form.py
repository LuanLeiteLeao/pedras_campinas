from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class DateInput(forms.DateInput):
	input_type = 'date'

FoneInput = forms.TextInput(attrs={'placeholder' : "00 00000-0000",
						"onkeypress": "formatar('## #####-####', this)"})

CpfInput = forms.TextInput(attrs={'placeholder' : "000.000.000-00",
						"onkeypress": "formatar('###.###.###-##', this)"})
CepInput =forms.TextInput(attrs={'placeholder' : "00000-000",
						"onkeypress": "formatar('#####-###', this)",
						"onblur":"pesquisacep(this.value)",})
class FormUser(forms.ModelForm):

	class Meta:
		model = User
		fields = ['nome', 'email', 'cpf', 'data_de_nascimento', 'genero','cep','endereco'  , 'observacao_endereco','cidade' ,'estado' ,'telefone' , 'celular'  ]
		widgets = {
			'cpf' : CpfInput,
			'data_de_nascimento'  : DateInput(),
			'cep' : CepInput,
			'cidade' : forms.TextInput(attrs={ 'readonly':'true', 'id' : 'cidade'}),
			'estado' : forms.TextInput(attrs={ 'readonly':'true', 'id' : 'uf'}),
			'telefone' : FoneInput,
			'celular' : FoneInput,
		}
		

