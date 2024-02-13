import pandas as pd
import plotly.express as px
import streamlit as st
    
car_data = pd.read_csv ("vehicles.csv")
st.header('Graficos dos Dados de Anucios de vendas')




hist_button = st.button('Criar histograma') # criar um botão
  
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)



# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')


if build_histogram: # se a caixa de seleção for selecionada
  # escrever uma mensagem
  st.write('Criando um histograma para a coluna odometer')
  

  fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
     
  # exibir um gráfico Plotly interativo
  st.plotly_chart(fig, use_container_width=True)
