
meses = (
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
)


num = int(input("Digite um número de 1 a 12: "))


if num >= 1 and num <= 12:
    print("Mês correspondente:", meses[num - 1])
else:
    print("Erro")
