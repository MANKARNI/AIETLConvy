# app.py

from flask import Flask, render_template, request, jsonify, send_file
import json
import azure_oai_connector

app = Flask(__name__)
xml_filename = 'aoi_response'

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML page

@app.route('/uploads', methods=['POST'])
def process_xml():
    try:
        xml_file = request.files['file']
        global
        xml_filename = xml_file.filename # get the file name
        xml_content = xml_file.read()  # Read the XML content

        # Call Azure OAI and process the response
        # (Replace this with your actual logic)
        # For demonstration purposes, we'll return a dummy response
        azure_oai_response = azure_oai_connector.process_xml_data(xml_content)
        
        print("response")
        print(azure_oai_response)

        # Save the response as a JSON file (optional)
        with open(f'{xml_filename}.json', 'w') as json_file:
            json.dump(azure_oai_response, json_file, indent=4)

        # Inside your process_xml route
        return jsonify({'message': 'Processing successful. Download the JSON file:', 'file_link': '/download/response.json'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/response.json')
def download_response():
    return send_file(f'{xml_filename}.json', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
