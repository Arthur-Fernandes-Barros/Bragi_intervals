def campoharmonico(tonica):
    notas = ['C','C#','D','D#','E','F','F#','G','G#','A', 'A#','B']

    if tonica not in notas or not isinstance(tonica,str):
        return 'Nota invalida'
    else:
        if tonica in notas:
            posicao = notas.index(tonica)
            print(f'Campo harmonico maior {notas[posicao]} {notas[ posicao - 10]}m {notas[ posicao - 8]}m {notas[posicao - 7]} {notas[ posicao - 5]} {notas[ posicao - 3]}m {notas[posicao - 1]}m7')
            print(f'Campo harmonico menor {notas[posicao]}m {notas[ posicao - 10]} {notas[ posicao - 9]}m {notas[posicao - 7]} {notas[ posicao - 5]} {notas[ posicao - 4]}m {notas[posicao - 2]}')
            print(f'Campo harmonico relativo menor {notas[(posicao-3)%12]}m {notas[((posicao-3)-10)%12]} {notas[((posicao-3)-9)%12]}m {notas[((posicao-3)-7)%12]} {notas[((posicao-3)-5)%12]} {notas[((posicao-3)-4)%12]}m {notas[((posicao-3)-2)%12]}')

campoharmonico('C')