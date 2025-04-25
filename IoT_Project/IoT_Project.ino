#include <Bridge.h>
#include <Process.h>

String inputString = "";       // Buffer for incoming serial data
bool inputComplete = false;    // Flag to track end of input line

void setup() {
  Serial.begin(9600);          // Initialize Serial
  Bridge.begin();              // Initialize Bridge (connects MCU to Linux)
  while (!Serial);             // Wait for Serial port (especially for Leonardo boards)
  Serial.println("Arduino Yun Ready. Type a message and press Enter:");
}

void loop() {
  // Read serial input
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      inputComplete = true;
    } else {
      inputString += c;
    }
  }

  // If input is complete, send to Google Sheet
  if (inputComplete) {
    sendToGoogleSheet(inputString);
    inputString = "";
    inputComplete = false;
  }
}

void sendToGoogleSheet(String data) {
  Process curl;
  String json = "{\"value\":\"" + data + "\"}";

  // Start curl command
  curl.begin("curl");

  // Set HTTP method to POST
  curl.addParameter("-X");
  curl.addParameter("POST");

  // Set content type to JSON
  curl.addParameter("-H");
  curl.addParameter("Content-Type: application/json");

  // Add JSON payload
  curl.addParameter("-d");
  curl.addParameter(json);

  // 🔗 Your Google Apps Script Web App URL
  curl.addParameter("https://script.google.com/macros/s/AKfycbw8yxIErShUR07fJRkCOXHIDsz2_aDpOjRajUc2oAahWS58vl0W9lhv_v4JspIWg0-QdA/exec");

  // Run the process
  curl.run();

  Serial.println("✅ Sent to Google Sheet: " + data);
}
