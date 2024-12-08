import argparse

def gerar_comando(nome_variavel):
    nome_parametro = f"PARAM_{nome_variavel.upper()}"
    
    bloco_parametro = f"""
    // Definição do parâmetro
    const char* {nome_parametro} = "{nome_variavel}";
    """
    
    bloco_html_form = f"""
    // Formulário HTML
    <form action="/set{nome_variavel.capitalize()}">
        <label for="{nome_variavel}">{nome_variavel.capitalize()} value:</label>
        <input type="number" id="{nome_variavel}" name="{nome_variavel}" value="%{nome_variavel.upper()}%">
        <input type="submit" value="Save">
    </form>
    """
    
    bloco_html_replace = f"""
    // Substituição no conteúdo HTML
    htmlContent.replace("%{nome_variavel.upper()}%", String({nome_variavel}));
    """
    
    bloco_server_handler = f"""
    // Manipulador do servidor
    server.on("/set{nome_variavel.capitalize()}", HTTP_GET, [](AsyncWebServerRequest* request) {{
        if (request->hasParam("{nome_variavel}")) {{
            {nome_variavel} = request->getParam("{nome_variavel}")->value().toInt();
            Serial.println("{nome_variavel.capitalize()} Value: " + String({nome_variavel}));
            preferences.putInt({nome_parametro}, {nome_variavel});
        }}
        request->redirect("/");
    }});
    """
    
    bloco_condicional = f"""
    // Atualização da variável através da Serial Console
    if (label == "{nome_variavel}") {{ // Para a variável {nome_variavel}
        int {nome_variavel} = valorStr.toInt();
        {nome_variavel} = valor;
        preferences.putInt("{nome_variavel}", {nome_variavel}); // Armazena o novo valor nas Preferences 
        Serial.println("{nome_variavel} atualizado para: " + String({nome_variavel}));
    }}
    """
    
    comando = (
        f"{bloco_parametro}\n\n"
        f"{bloco_html_form}\n\n"
        f"{bloco_html_replace}\n\n"
        f"{bloco_server_handler}\n\n"
        f"{bloco_condicional}"
    )
    
    return comando

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerar comando HTML baseado em uma variável.")
    parser.add_argument("nome_variavel", type=str, help="Nome da variável para gerar o comando.")
    args = parser.parse_args()

    # Gerar o comando com base no argumento fornecido
    comando_gerado = gerar_comando(args.nome_variavel)
    print(comando_gerado)
