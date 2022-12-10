import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px




# st.set_page_config(
#     page_title="FE. Final Project",
#     layout="wide",
# )

st.title("MCD. Ingeniería de características. Proyecto final")

st.subheader(
    "Relación entre presupuesto a la educación pública del estado de Sonora y Salario promedio mensual."
)
col1, col2 = st.columns(2)




# dataframe
df = pd.read_csv('https://raw.githubusercontent.com/elgiroma/MCD.-FE-Final-project/main/data_final/final_df_crime_wage_amount.csv')

df["Municipality"].value_counts().reset_index().to_csv("cities_df.csv")
df = df.drop("Unnamed: 0", axis=1)
municipality = pd.read_csv("./cities_df.csv")
municipality = municipality["index"].to_numpy()


# ********************************************************************************************************************************************
# ********************************************************************************************************************************************




# dashboard
with col1:

    # Choosing municipality
    chosen_municipality = st.selectbox("Selecciona algún municipio.", municipality)

    # dataframe of chosen municipality
    df_municipality = df[df.Municipality == chosen_municipality]


    # -----------------------------------------------------------------------------------------------

    # Plotting monthly wage vs worked hours weekly
    fig = px.line(
        df_municipality,
        x= "worked_hours_week",
        y= "monthly_wage"
    )
    fig.update_layout(
        title="Salario mensual conforme las horas trabajadas semanales",
        xaxis_title="Horas semanales trabajadas",
        yaxis_title="Salario mensual promedio",
)
    st.plotly_chart(fig, use_container_width=True)


    # -----------------------------------------------------------------------------------------------
 

    # correlation matrix
    correlation_matrix = df_municipality.corr()
    fig = px.imshow(correlation_matrix, color_continuous_scale=px.colors.sequential.Blues)
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


    # Plotting amount executed vs worked hours weekly
    fig = px.line(
        df_municipality,
        x= "amount_executed",
        y= "worked_hours_week"
    )
    fig.update_layout(
        title="Horas trabajadas semanales conforme el presupuesto a la educación pública en Sonora",
        xaxis_title="Presupuesto a educación pública en Sonora",
        yaxis_title="Horas trabajadas semanales",
    )
    st.plotly_chart(fig, use_container_width=True)


    # -----------------------------------------------------------------------------------------------
    

    # Plotting amount executed vs monthly wage
    fig = px.line(
        df_municipality,
        x= "amount_executed",
        y= "monthly_wage"
    )
    fig.update_layout(
        title="Salario mensual promedio conforme el presupuesto a la educación pública en Sonora",
        xaxis_title="Presupuesto a educación pública en Sonora",
        yaxis_title="Salario mensual promedio",
    )
    st.plotly_chart(fig, use_container_width=True)


    
    
# st.subheader(
#     "Municipio: {}.".format(chosen_municipality)
# )

# st.subheader(
#     "Correlación entre presupuesto a la educación pública de Sonora y el número de crímenes: {} ".format(str(correlation_matrix.iloc[3, 0])
#                                                                                                         )
# )
