anoAtual = 2023
mesAtual = 9
diaAtual = 29

ano_nascimento = int(input("Digite seu ano de nasicmento:"))
mes_nascimento = int(input("Digite o mes do seu nascimento:"))
dia_nascimento = int(input("Digite o dia do seu nascimento:"))

dias_ano = (anoAtual - ano_nascimento)*365
mes_ano = (mesAtual - mes_nascimento)*30
dia_ano = (diaAtual - dia_nascimento)

total_de_dias = dias_ano + mes_ano + dia_ano

print("Seu ano de nascimento foi: {} \n"
      "Seu mes de nascimento foi: {} \n"
      "Seu dia de nascimento foi: {} \n"
      "Sua idade em dias: {}"
      .format(ano_nascimento, mes_nascimento,dia_nascimento,total_de_dias))
