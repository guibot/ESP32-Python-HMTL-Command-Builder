def gerar_comando(nome_variavel):
    # Transformar o nome da variável para maiúsculas e criar o nome do parâmetro
    nome_parametro = f"PARAM_{nome_variavel.upper()}"
    
    # Criar o comando com a variável e o nome do parâmetro
    comando = f'const char* {nome_parametro} = "{nome_variavel}";'
    
    # Criar o bloco de HTML
    html = f"""
    <form action="/set{nome_variavel.capitalize()}">
        <label for="{nome_variavel}">{nome_variavel.capitalize()} value:</label>
        <input type="number" id="{nome_variavel}" name="{nome_variavel}" value="%{nome_variavel.upper()}%">
        <input type="submit" value="Save">
    </form>
    """
    
    # Criar o bloco de substituição de HTML
    substituicao_html = f'htmlContent.replace("%{nome_variavel.upper()}%", String({nome_variavel}_var));'
    
    # Criar o handler do servidor
    handler_server = f"""
    server.on("/set{nome_variavel.capitalize()}", HTTP_GET, [](AsyncWebServerRequest* request) {{
        if (request->hasParam("{nome_variavel}")) {{
            {nome_variavel}_var = request->getParam("{nome_variavel}")->value().toInt();
            Serial.println("{nome_variavel.capitalize()} Value: " + String({nome_variavel}_var));
            preferences.putInt({nome_parametro}, {nome_variavel}_var);
        }}
        request->redirect("/");
    }});
    """
    
    return comando, html, substituicao_html, handler_server

# Testando o script com a variável 'test'
variavel = "test"
comando_gerado, html_gerado, substituicao_html_gerada, handler_server_gerado = gerar_comando(variavel)
print(comando_gerado)
print(html_gerado)
print(substituicao_html_gerada)
print(handler_server_gerado)
