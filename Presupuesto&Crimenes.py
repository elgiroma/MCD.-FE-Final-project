import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="MCD. Ingeniería de características. Proyecto final",
    layout="wide",
)

st.title("MCD. Ingeniería de características. Proyecto final")

# st.sidebar.success('Elige página')

st.subheader(
    "Relación del número de crimenes en los municipios del estado de Sonora con el presupuesto dado a la educación pública de Sonora."
)
col1, col2 = st.columns(2)


# dataframe
df = pd.read_csv('https://raw.githubusercontent.com/elgiroma/MCD.-FE-Final-project/main/data_final/final_df_crime_wage_amount.csv')

df["Municipality"].value_counts().reset_index().to_csv("cities_df.csv")
df = df.drop("Unnamed: 0", axis=1)
municipality = pd.read_csv("./cities_df.csv")
municipality = municipality["index"].to_numpy()
# municipality = sorted(municipality)
# municipality.remove('San Javier')
# municipality.insert(0,'San Javier')

# ********************************************************************************************************************************************
# ********************************************************************************************************************************************


# dashboard
with col1:

    # Choosing municipality
    chosen_municipality = st.selectbox("Selecciona algún municipio.", municipality)
#     st.write("Chosen city:", chosen_municipality)

    # dataframe of chosen municipality
    df_municipality = df[df.Municipality == chosen_municipality]


    # -----------------------------------------------------------------------------------------------

    # Plotting amount executed over the years
    fig = px.line(
        df_municipality,
        x= "Year",
        y= "amount_executed"
    )
    fig.update_layout(
        title="amount_executed over the years in Sonora",
        xaxis_title="Years",
        yaxis_title="Amount executed",
    )
    st.plotly_chart(fig, use_container_width=True)


    # -----------------------------------------------------------------------------------------------
 
    # Plotting number of crimes over the years
    fig = px.line(
        df_municipality,
        x= "Year",
        y= "number_crimes"
    )
    fig.update_layout(
        title="Number of crimes over the years",
        xaxis_title="Years",
        yaxis_title="Number of crimes",
    )
    st.plotly_chart(fig, use_container_width=True)


# ********************************************************************************************************************************************
# ********************************************************************************************************************************************


with col2:
    st.text("  ")
    st.text("  ")
    st.text("  ")
    st.text("  ")
    st.text("  ")
    st.text("  ")
    st.text("  ")
    st.text("  ")

    # -----------------------------------------------------------------------------------------------

    # Plotting number of crimes as more amount of money was executed
    fig = px.line(
        df_municipality,
        x= "amount_executed",
        y= "number_crimes"
    )
    fig.update_layout(
        title="Number of crimes as more amount of money was executed",
        xaxis_title="Amount executed",
        yaxis_title="Number of crimes",
    )
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------------------------------------------------------------------------

    # correlation matrix
    correlation_matrix = df_municipality.corr()
    fig = px.imshow(correlation_matrix, color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig, use_container_width=True)
    
    
st.subheader(
    "Municipio: {}.".format(chosen_municipality)
)

st.subheader(
    "Correlación entre presupuesto a la educación pública de Sonora y el número de crímenes: {}% ".format(str(100*correlation_matrix.iloc[3, 0])
                                                                                                        )
)






