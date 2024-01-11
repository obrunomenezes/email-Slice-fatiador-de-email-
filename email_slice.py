email= input ("informe seu e-mail: ").strip() 

# Solicita ao usuário que informe seu e-mail e remove espaços em branco antes e depois do texto
# Extrai o nome de usuário (parte antes do @) e o domínio (parte depois do @) do e-mail

usuario = email[:email.index("@")]  # Obtém a substring até o índice do "@" no e-mail

dominio = email[email.index("@") + 1:]  # Obtém a substring após o "@" no e-mail

# Exibe uma mensagem formatada com o nome de usuário e o domínio do e-mail
print(f"O seu e-mail é {usuario}, e seu domínio é {dominio}")
