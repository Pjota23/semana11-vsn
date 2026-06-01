#REGISTRO DA SEMANA 11
# Feature Flags
habilitar_cupom_desconto = False
habilitar_pagamento_pix = False
 
def renderizar_tela_de_pagamento():
 
    # Campo de cupom
    if habilitar_cupom_desconto:
        print("Mostrar campo: Cupom de Desconto")
 
    # Forma de pagamento
    if habilitar_pagamento_pix:
        print("Mostrar botão: Pagar com PIX")
    else:
        print("Mostrar botão: Pagar com Cartão")
 
renderizar_tela_de_pagamento()
