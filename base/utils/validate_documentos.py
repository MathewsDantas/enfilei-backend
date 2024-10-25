from django.core.exceptions import ValidationError


from base.utils.format_documentos import clear_cpf


def validate_cpf(cpf):
    cpf = clear_cpf(cpf)
    if len(cpf) != 11:
        raise ValidationError("CPF deve ter 11 dígitos.")

    if cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais
        raise ValidationError("CPF inválido.")

    for i in range(9, 11):  # Valida os dois últimos dígitos verificadores
        value = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digit = (value * 10 % 11) % 10
        if digit != int(cpf[i]):
            raise ValidationError("CPF inválido.")
