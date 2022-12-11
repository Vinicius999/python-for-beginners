def notas(* num, sit=False):
    """
    -> Analisar as notas e situações de vários alunos
    :param num: Notas inseridas (aceita várias)
    :param sit: (opcional) Mostra a situação:
    :return: Dicionário com várias informações sobre a situação da turma
    """
    notes = dict()
    notes['total'] = len(num)
    notes['maior'] = max(num)
    notes['menor'] = min(num)
    notes['média'] = sum(num) / len(num)
    if sit:
        if notes['média'] >= 7:
            notes['situação'] = 'BOA'
        elif notes['média'] >= 5:
            notes['situação'] = 'RAZOÁVEL'
        else:
            notes['situação'] = 'RUIM'
    return notes


resp = notas(3.5, 9, 9.5, sit=True)
print(resp)
