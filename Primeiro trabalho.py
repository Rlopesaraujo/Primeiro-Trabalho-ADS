print("Passo 1: Chego para trabalhar no Sushi")
print("Passo 2: Abro o sistema nos computadores e verifico se já tem pedidos para sair na cozinha")
print("Passo 3: Pego o pedido do cliente para fechar e enviar via delivery")

molho_shoyo = input("Colocar molho shoyo no pedido? (sim/não?): ").lower()
molho_tare = input("Colocar molho tare no pedido? (sim/não?): ").lower()
if molho_shoyo == "sim":
    print("Shoyo adicionado ao pedido")
else:
    print("Pedido sem molho shoyo adicionado")
if molho_tare == "sim":
    print("Tare adicionado ao pedido")
else:
    print("Pedido sem molho tare adicionado")

print("Passo 4: Perguntar ao cliente se é débito ou crédito")

pergunta_pagamento = input("O pagamento vai ser no débito, crédito ou dinheiro? ").lower()
if pergunta_pagamento == "débito":
    print("Pagamento no débito realizado, tenha uma boa noite.")
elif pergunta_pagamento == "crédito":
    print("Pagamento no crédito realizado, tenha uma boa noite.")
else:
    print("Pagamento realizado no dinheiro, tenha uma boa noite.")

