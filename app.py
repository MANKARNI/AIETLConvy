# app.py

from flask import Flask, render_template, request, jsonify, send_file
import json
import azure_oai_connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML page

@app.route('/uploads', methods=['POST'])
def process_xml():
    try:
        xml_file = request.files['file']
        xml_filename = xml_file.filename  # Get the file name
        xml_content = xml_file.read()  # Read the XML content

        # Call Azure OAI and process the response
        # (Replace this with your actual logic)
        # For demonstration purposes, we'll return a dummy response
        azure_oai_response = azure_oai_connector.process_xml_data(xml_content)
        
        print("response")
        print(azure_oai_response)

        # Create a JSON filename based on the XML filename
        json_filename = os.path.splitext(xml_filename)[0] + '.json'

        # Save the response as a JSON file
        with open(json_filename, 'w') as json_file:
            json.dump(azure_oai_response, json_file, indent=4)

        # Inside your process_xml route
        return jsonify({'message': f'Processing successful for file: {xml_filename}. Download the JSON file:', 'file_link': f'/download/{json_filename}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_response(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
