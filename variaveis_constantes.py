nome = "Guilherme"
idade = 30

print(f"Nome: {nome}, Idade: {idade}") 

nome,idade = "Ana", 25

print(f"Nome: {nome}, Idade: {idade}") 

BRAZILIAN_STATES = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul",
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
    "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia"]

print("Estados do Brasil:")
for estado in BRAZILIAN_STATES:
    print(estado)