"""Faça um sistema de conversão de real para dolar e vice-versa."""
import dearpygui.dearpygui as dpg
import sys

dpg.create_context()
def fecharprograma():
    dpg.stop_dearpygui() 

def converter_moeda():
    # Obtém os valores inseridos nos campos de "input" da interface
    moedaInicial = dpg.get_value("moedaInicial")
    valorConverter = dpg.get_value("valorConverter")
    euroConversao = dpg.get_value("euroConversao")


    try:
        # Converte os valores obtidos para os tipos de variáveis adequados
        real = float(0.1933) # Valor do real para o dólar
        dolar = float(5.1729) # Valor do dólar para o real
        euro = float(0.18) # Valor do dólar para o real
        moedaInicial = (moedaInicial) # Moeda a ser convertida escolhida pelo usuário
        valorConverter = float(valorConverter) # Valor que o usuário deseja converter
        realConversao = float(valorConverter * dolar) # Converte o DÓLAR para o REAL
        dolarConversao = float(valorConverter * real) # Converte o REAL para o DÓLAR
        euroConversao = float(valorConverter * euro) # Converte o REAL para o Euro
       


        # Avalia a moeda escolhida e converte para a outra.
        if moedaInicial == "dólar".lower() or moedaInicial == "dolar".lower() or moedaInicial == "euro".lower(): # Converte o DÓLAR, REAL for euro 
            resultado = f"${valorConverter} equivale a R${realConversao:.2f}"

        elif moedaInicial == "real".lower(): # Converte o REAL para o DÓLAR
            resultado = f"R${valorConverter} equivale a ${dolarConversao:.2f}"

        elif moedaInicial == "real".lower(): # Converte o REAL para o DÓLAR
            resultado = f"R${valorConverter} equivale a ${euroConversao:.2f}"

        else:
            resultado = f"'{moedaInicial}' não foi reconhecido. Por favor, escolha entre 'DÓLAR', 'REAL' e 'Euro'." # Mensagem de erro em caso de moeda digitada errada

        # Configura o valor do texto de resultado na interface com o final e interpretação ou mensagem de erro
        dpg.set_value("resultado", resultado)

    # Define uma mensagem de erro se os valores inseridos não forem identificados (não forem "real" ou "dólar")
    except ValueError:
        dpg.set_value("resultado", "Erro: Por favor, escolha entre 'DÓLAR', 'REAL' e 'REAL'.")

# Cria uma janela para visualização da aplicação com um título e dimensões definidas
dpg.create_viewport(title='Conversor de moedas', width=1000, height=300)

# Define a janela principal onde os elementos da interface serão colocados
with dpg.window(label="Conversor", width=1000, height=300):
    # Adiciona um campo de texto para o usuário inserir a moeda a ser convertida.
    dpg.add_input_text(label="Moeda a ser convertida (real, dólar ou euro):", tag="moedaInicial")
    dpg.add_input_text(label="Valor a ser convertido:", tag="valorConverter")
    # Adiciona um botão que, quando clicado, chama a função 'converter_moeda'
    dpg.add_button(label="Converter moeda", callback=converter_moeda)
    dpg.add_button(label="sair", callback=fecharprograma) #Button adcionado.-----

    # Adiciona um espaço para exibir o resultado ou mensagens de erro
    dpg.add_text("", tag="resultado")

# Configura e mostra a janela
dpg.setup_dearpygui()
dpg.show_viewport()
# Inicia o loop de eventos da interface, onde a aplicação efetivamente roda e espera por interações do usuário
dpg.start_dearpygui()
# Destroi o contexto da aplicação após o fechamento da janela, liberando recursos
dpg.destroy_context()
dpg.stop_dearpygui() 

