# ESP32-Python-HMTL-Command-Builder

Dynamic Code Generator for ESP32 Projects
This repository contains a Python script that generates dynamic code blocks for ESP32-based projects. The script simplifies the creation of repetitive structures such as parameter definitions, HTML forms, HTML content replacements, and HTTP server handlers, all tailored to a specific variable name.

Features
Generate parameter constants for use in ESP32 projects.
Automatically create HTML forms with dynamic variable placeholders.
Define HTML content replacement logic for variable updates.
Build HTTP server endpoints to process and store variable values using Preferences.
Fully customizable for any variable name.
How It Works
Provide a variable name to the Python function, and it will generate:

A parameter definition for use in C++:
cpp
Copy code
const char* PARAM_EXAMPLE = "example";
A corresponding HTML form:
html
Copy code
<form action="/setExample">
    <label for="example">Example value:</label>
    <input type="number" id="example" name="example" value="%EXAMPLE%">
    <input type="submit" value="Save">
</form>
A replacement command for HTML content:
cpp
Copy code
htmlContent.replace("%EXAMPLE%", String(example_var));
An HTTP GET server handler to handle variable updates:
cpp
Copy code
server.on("/setExample", HTTP_GET, [](AsyncWebServerRequest* request) {
    if (request->hasParam("example")) {
        example_var = request->getParam("example")->value().toInt();
        Serial.println("Example Value: " + String(example_var));
        preferences.putInt(PARAM_EXAMPLE, example_var);
    }
    request->redirect("/");
});
Use Case
This tool is ideal for projects involving:

ESP32 and the AsyncWebServer library.
Dynamic web interfaces to control hardware parameters.
Persistent storage of parameters using the Preferences library.