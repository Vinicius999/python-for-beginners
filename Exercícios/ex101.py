def voto(nasc):
    from datetime import date
    if date.today().year - nasc < 16:
        return f'Com {date.today().year - nasc} anos: NÃ0 VOTA.'
    elif 16 <= date.today().year - nasc < 18 or date.today().year - nasc >= 65:
        return f'Com {date.today().year - nasc} anos: VOTO OPCIONAL.'
    else:
        return f'Com {date.today().year - nasc} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
sit = voto(int(input('Em que ano você nasceu? ')))
print(sit)
