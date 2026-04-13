import streamlit as st


def campoharmonico(tonica):
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    if tonica not in notas or not isinstance(tonica, str):
        st.error('Nota inválida')
    else:
        if tonica in notas:
            posicao = notas.index(tonica)

            # Helper para formatar a nota grande com o grau pequeno
            def formatar(nota, grau):
                return f'<span style="font-size: 24px; font-weight: bold;">{nota}</span> <span style="font-size: 14px;">({grau})</span>'

            # Construção das strings com HTML
            maior = " | ".join([
                formatar(notas[posicao], "I"),
                formatar(f"{notas[posicao - 10]}m", "II"),
                formatar(f"{notas[posicao - 8]}m", "III"),
                formatar(notas[posicao - 7], "IV"),
                formatar(notas[posicao - 5], "V"),
                formatar(f"{notas[posicao - 3]}m", "VI"),
                formatar(f"{notas[posicao - 1]}m", "VII")
            ])

            menor = " | ".join([
                formatar(f"{notas[posicao]}m", "I"),
                formatar(notas[posicao - 10], "II"),
                formatar(f"{notas[posicao - 9]}m", "III"),
                formatar(notas[posicao - 7], "IV"),
                formatar(notas[posicao - 5], "V"),
                formatar(f"{notas[posicao - 4]}m", "VI"),
                formatar(notas[posicao - 2], "VII")
            ])

            rel_pos = (posicao - 3) % 12
            relativo = " | ".join([
                formatar(f"{notas[rel_pos]}m", "I"),
                formatar(notas[(rel_pos - 10) % 12], "II"),
                formatar(f"{notas[(rel_pos - 9) % 12]}m", "III"),
                formatar(notas[(rel_pos - 7) % 12], "IV"),
                formatar(notas[(rel_pos - 5) % 12], "V"),
                formatar(f"{notas[(rel_pos - 4) % 12]}m", "VI"),
                formatar(notas[(rel_pos - 2) % 12], "VII")
            ])

            # Exibição usando markdown com suporte a HTML
            st.subheader("Campo Harmônico Maior")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #007bff;">{maior}</div>', unsafe_allow_html=True)

            st.subheader("Campo Harmônico Menor")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #28a745;">{menor}</div>', unsafe_allow_html=True)

            st.subheader("Campo Harmônico Relativo Menor")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #ffc107;">{relativo}</div>', unsafe_allow_html=True)

# --- Interface em Streamlit ---


st.set_page_config(page_title="Bragi_intervals", page_icon="🎵")

st.title("🎵 Bragi_intervals")
st.write("Visualize os campos harmônicos com as notas em destaque.")

notas_disponiveis = ['C', 'C#', 'D', 'D#',
                     'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
nota_selecionada = st.selectbox("Selecione a Tônica:", notas_disponiveis)

if st.button("Gerar Intervalos"):
    campoharmonico(nota_selecionada)


def campoharmonico(tonica):
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    if tonica not in notas or not isinstance(tonica, str):
        st.error('Nota inválida')
    else:
        if tonica in notas:
            posicao = notas.index(tonica)

            # Helper para formatar a nota grande com o grau pequeno
            def formatar(nota, grau):
                return f'<span style="font-size: 24px; font-weight: bold;">{nota}</span> <span style="font-size: 14px;">({grau})</span>'

            # Construção das strings com HTML
            maior = " | ".join([
                formatar(notas[posicao], "I"),
                formatar(f"{notas[posicao - 10]}m", "II"),
                formatar(f"{notas[posicao - 8]}m", "III"),
                formatar(notas[posicao - 7], "IV"),
                formatar(notas[posicao - 5], "V"),
                formatar(f"{notas[posicao - 3]}m", "VI"),
                formatar(f"{notas[posicao - 1]}m", "VII")
            ])

            menor = " | ".join([
                formatar(f"{notas[posicao]}m", "I"),
                formatar(notas[posicao - 10], "II"),
                formatar(f"{notas[posicao - 9]}m", "III"),
                formatar(notas[posicao - 7], "IV"),
                formatar(notas[posicao - 5], "V"),
                formatar(f"{notas[posicao - 4]}m", "VI"),
                formatar(notas[posicao - 2], "VII")
            ])

            rel_pos = (posicao - 3) % 12
            relativo = " | ".join([
                formatar(f"{notas[rel_pos]}m", "I"),
                formatar(notas[(rel_pos - 10) % 12], "II"),
                formatar(f"{notas[(rel_pos - 9) % 12]}m", "III"),
                formatar(notas[(rel_pos - 7) % 12], "IV"),
                formatar(notas[(rel_pos - 5) % 12], "V"),
                formatar(f"{notas[(rel_pos - 4) % 12]}m", "VI"),
                formatar(notas[(rel_pos - 2) % 12], "VII")
            ])

            # Exibição usando markdown com suporte a HTML
            st.subheader("Campo Harmônico Maior")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #007bff;">{maior}</div>', unsafe_allow_html=True)

            st.subheader("Campo Harmônico Menor")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #28a745;">{menor}</div>', unsafe_allow_html=True)

            st.subheader("Campo Harmônico Relativo Menor")
            st.write(
                f'<div style="padding: 15px; border-radius: 10px; border-left: 5px solid #ffc107;">{relativo}</div>', unsafe_allow_html=True)

# --- Interface em Streamlit ---


st.set_page_config(page_title="Bragi_intervals", page_icon="🎵")

st.title("🎵 Bragi_intervals")
st.write("Visualize os campos harmônicos com as notas em destaque.")

notas_disponiveis = ['C', 'C#', 'D', 'D#',
                     'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Cria um menu dropdown simples
nota_selecionada = st.selectbox("Selecione a Tônica:", notas_disponiveis)

if st.button("Gerar Intervalos"):
    campoharmonico(nota_selecionada)
