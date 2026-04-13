import streamlit as st


def campoharmonico(tonica):
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    if tonica not in notas or not isinstance(tonica, str):
        # Substituído 'return' padrão por um aviso de erro do Streamlit
        st.error('Nota inválida')
    else:
        if tonica in notas:
            posicao = notas.index(tonica)
            # Substituído 'print' por 'st.write' para exibir na interface web
            st.write(
                f'**Campo harmônico maior:** {notas[posicao]} {notas[ posicao - 10]}m {notas[ posicao - 8]}m {notas[posicao - 7]} {notas[ posicao - 5]} {notas[ posicao - 3]}m {notas[posicao - 1]}m7')
            st.write(
                f'**Campo harmônico menor:** {notas[posicao]}m {notas[ posicao - 10]} {notas[ posicao - 9]}m {notas[posicao - 7]} {notas[ posicao - 5]} {notas[ posicao - 4]}m {notas[posicao - 2]}')
            st.write(
                f'**Campo harmônico relativo menor:** {notas[(posicao-3)%12]}m {notas[((posicao-3)-10)%12]} {notas[((posicao-3)-9)%12]}m {notas[((posicao-3)-7)%12]} {notas[((posicao-3)-5)%12]} {notas[((posicao-3)-4)%12]}m {notas[((posicao-3)-2)%12]}')

# --- Interface em Streamlit ---


st.title("🎵 Gerador de Campo Harmônico")
st.write("Escolha a nota tônica para visualizar os seus respectivos campos harmônicos.")

# Lista de notas para o menu de seleção
notas_disponiveis = ['C', 'C#', 'D', 'D#',
                     'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Cria um menu dropdown simples
nota_selecionada = st.selectbox("Selecione a Tônica:", notas_disponiveis)

# Botão para executar a função com a nota escolhida
if st.button("Mostrar Campos Harmônicos"):
    campoharmonico(nota_selecionada)
