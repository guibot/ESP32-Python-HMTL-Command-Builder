# Dynamic Code Generator for ESP32 Projects

This repository contains a Python script designed to simplify the development of ESP32 IOT projects by dynamically generating HTML code.
This generated code can be useful for common structures such as parameter definitions and HTML forms.

## Features
- Automatically generate **parameter constants** for use in C++.
- Create **HTML forms** with placeholders for dynamic values.
- Implement **HTML content replacements** to update displayed values.
- Define **HTTP server endpoints** to handle variable updates and store values using Preferences.

## How It Works
The script takes a variable name as input and generates the following:

In this case, we are using the word "test" as a variable to be adapted to the following commands.

variavel = "example"

On Terminal, just call the script and type the variable name:

python .\HTMLCommandBuilder.py example

### Generated Code, just copy, past, adapt
```cpp

const char* PARAM_EXAMPLE = "example";

<form action="/setExample">
    <label for="example">Example value:</label>
    <input type="number" id="example" name="example" value="%EXAMPLE%">
    <input type="submit" value="Save">
</form>

htmlContent.replace("%EXAMPLE%", String(example_var));

server.on("/setExample", HTTP_GET, [](AsyncWebServerRequest* request) {
    if (request->hasParam("example")) {
        example_var = request->getParam("example")->value().toInt();
        Serial.println("Example Value: " + String(example_var));
        preferences.putInt(PARAM_EXAMPLE, example_var);
    }
    request->redirect("/");
});
