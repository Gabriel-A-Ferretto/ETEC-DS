# Configurações do campeonato
TOTAL_TIMES = 3
JOGADORES_POR_TIME = 8
TOTAL_JOGADORES = TOTAL_TIMES * JOGADORES_POR_TIME

# Variáveis globais para acumular os dados do campeonato
qtd_menores_18 = 0
soma_alturas_campeonato = 0
qtd_mais_80kg = 0

for t in range(1, TOTAL_TIMES + 1):
    print(f"\n--- TIME {t} ---")
    soma_idades_time = 0
    
    for j in range(1, JOGADORES_POR_TIME + 1):
        print(f"Jogador {j}:")
        idade = int(input("  Idade: "))
        peso = float(input("  Peso (kg): "))
        altura = float(input("  Altura (m): "))
        
        # 1. Quantidade de jogadores com idade inferior a 18 anos
        if idade < 18:
            qtd_menores_18 += 1
            
        # Acumula idade para a média do time atual
        soma_idades_time += idade
        
        # Acumula altura para a média geral do campeonato
        soma_alturas_campeonato += altura
        
        # 4. Jogadores com mais de 80kg
        if peso > 80:
            qtd_mais_80kg += 1
            
    # Média de idade do time
    media_idade_time = soma_idades_time / JOGADORES_POR_TIME
    print(f"> Média de idade do Time {t}: {media_idade_time:.2f} anos")

# Cálculos finais
media_altura_geral = soma_alturas_campeonato / TOTAL_JOGADORES
porcentagem_80kg = (qtd_mais_80kg / TOTAL_JOGADORES) * 100

print("\n" + "="*40)
print("RELATÓRIO FINAL DO CAMPEONATO")
print(f"1. Jogadores menores de 18 anos: {qtd_menores_18}")
print(f"2. Média de altura de todos os jogadores: {media_altura_geral:.2f} m")
print(f"3. Porcentagem de jogadores com mais de 80kg: {porcentagem_80kg:.2f}%")
print("="*40)