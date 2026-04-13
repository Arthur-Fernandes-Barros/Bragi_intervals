import streamlit as st


def campoharmonico(tonica):
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    if tonica not in notas or not isinstance(tonica, str):
        st.error('Nota inválida')
    else:
        if tonica in notas:
            posicao = notas.index(tonica)

            # Strings formatadas com os intervalos (I, II, III, etc.)
            maior = f"**I:** {notas[posicao]} | **II:** {notas[ posicao - 10]}m | **III:** {notas[ posicao - 8]}m | **IV:** {notas[posicao - 7]} | **V:** {notas[ posicao - 5]} | **VI:** {notas[ posicao - 3]}m | **VII:** {notas[posicao - 1]}m"

            menor = f"**I:** {notas[posicao]}m | **II:** {notas[ posicao - 10]} | **III:** {notas[ posicao - 9]}m | **IV:** {notas[posicao - 7]} | **V:** {notas[ posicao - 5]} | **VI:** {notas[ posicao - 4]}m | **VII:** {notas[posicao - 2]}"

            relativo = f"**I:** {notas[(posicao-3)%12]}m | **II:** {notas[((posicao-3)-10)%12]} | **III:** {notas[((posicao-3)-9)%12]}m | **IV:** {notas[((posicao-3)-7)%12]} | **V:** {notas[((posicao-3)-5)%12]} | **VI:** {notas[((posicao-3)-4)%12]}m | **VII:** {notas[((posicao-3)-2)%12]}"

            # Exibição formatada no Streamlit
            st.subheader("Campo Harmônico Maior")
            st.info(maior)

            st.subheader("Campo Harmônico Menor")
            st.info(menor)

            st.subheader("Campo Harmônico Relativo Menor")
            st.info(relativo)

# --- Interface em Streamlit ---


# Título alterado conforme solicitado
st.title("🎵 Bragi_intervals")
st.write("Escolha a nota tônica para visualizar os seus respectivos campos harmônicos e intervalos.")

# Lista de notas para o menu de seleção
notas_disponiveis = ['C', 'C#', 'D', 'D#',
                     'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Cria um menu dropdown simples
nota_selecionada = st.selectbox("Selecione a Tônica:", notas_disponiveis)

# Botão para executar a função com a nota escolhida
if st.button("Mostrar Campos Harmônicos"):
    campoharmonico(nota_selecionada)
