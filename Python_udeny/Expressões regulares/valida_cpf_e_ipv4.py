import re
# 0.0.0.0 até 255.255.255.255
# 025.258.963-10

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

print(cpf_reg_exp.search(cpf))
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf))