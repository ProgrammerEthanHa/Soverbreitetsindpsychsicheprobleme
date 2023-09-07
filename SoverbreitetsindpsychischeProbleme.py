import streamlit as st
import pandas as pd
import altair as alt

st.header("So verbreitet sind psychische Probleme")
st.subheader("Befragte, die in den letzten 12 Monaten folgendes erlebt haben")

source = pd.DataFrame({
        'Anteil (%)': [31, 27, 24, 23, 22, 17, 17, 14, 9, 5],
        'Krankheit': ['Stress', 'Stimmungsumschwang', 'Depressive Phase', 'Phasen der Traurigkeit', 'Phasen der Lethargie', 'Gefühl der Einsamkeit/sozialen Isolation', 'Probleme mit dem Selbstwertgefühl', 'Angst', 'Panikattacken', 'Phobien']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Krankheit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: n=2089; 18-64 Jahren; Deutschland; Mehrfachnennung möglich; 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Global Consumer Survey")