import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
option1 = st.selectbox("Select the data for the X-axis",
                       ("GDP", "Happiness", "Generosity"))
option2 = st.selectbox("Select the data for the Y-axis",
                       ("GDP", "Happiness", "Generosity"))
st.subheader(f"{option1} and {option2}")
df = pd.read_csv("happy.csv")


def get_plot(x_axis, y_axis):
    x_axis = option1
    y_axis = option2
    return x_axis, y_axis


while True:
    match get_plot(x_axis=option1, y_axis=option2):
        case _:
            if option1 == "GDP" and option2 == "GDP":
                gdp_plot = px.scatter(x=df['gdp'], y=df['gdp'],
                                      labels={"x": "GDP", "y": "GDP"})
                st.plotly_chart(gdp_plot)
            elif option1 == "GDP" and option2 == "Happiness":
                hap_plot = px.scatter(x=df['gdp'], y=df['happiness'],
                                      labels={"x": "GDP", "y": "Happiness"})
                st.plotly_chart(hap_plot)
            elif option1 == "GDP" and option2 == "Generosity":
                gen_plot = px.scatter(x=df['gdp'], y=df['generosity'],
                                      labels={"x": "GDP", "y": "Generosity"})
                st.plotly_chart(gen_plot)

            elif option1 == "Happiness" and option2 == "GDP":
                gdp_plot2 = px.scatter(x=df['happiness'], y=df['gdp'],
                                       labels={"x": "Happiness", "y": "GDP"})
                st.plotly_chart(gdp_plot2)
            elif option1 == "Happiness" and option2 == "Happiness":
                hap_plot2 = px.scatter(x=df['happiness'], y=df['happiness'],
                                       labels={"x": "Happiness",
                                               "y": "Happiness"})
                st.plotly_chart(hap_plot2)
            elif option1 == "Happiness" and option2 == "Generosity":
                gen_plot2 = px.scatter(x=df['happiness'], y=df['generosity'],
                                       labels={"x": "Happiness",
                                               "y": "Generosity"})
                st.plotly_chart(gen_plot2)

            elif option1 == "Generosity" and option2 == "GDP":
                gdp_plot3 = px.scatter(x=df['generosity'], y=df['gdp'],
                                       labels={"x": "Generosity", "y": "GDP"})
                st.plotly_chart(gdp_plot3)
            elif option1 == "Generosity" and option2 == "Happiness":
                hap_plot3 = px.scatter(x=df['generosity'], y=df['happiness'],
                                       labels={"x": "Generosity",
                                               "y": "Happiness"})
                st.plotly_chart(hap_plot3)
            else:
                gen_plot3 = px.scatter(x=df['generosity'], y=df['generosity'],
                                       labels={"x": "Generosity",
                                               "y": "Generosity"})
                st.plotly_chart(gen_plot3)
            break
