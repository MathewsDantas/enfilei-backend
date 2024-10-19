import re


def format_cpf(cpf):
    return "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]) if cpf else ""


def clear_cpf(cpf):
    return re.sub(r"[^0-9]", "", cpf) if cpf else ""
