from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy data for fan lights
fan_lights = {
    1: {'name': 'Fan Light 1', 'status': 'off'},
    2: {'name': 'Fan Light 2', 'status': 'off'}
}

# Route to serve the HTML template
@app.route('/')
def home():
    return render_template('index.html')

# Route to toggle a fan light
@app.route('/toggle_fan_light/<int:fan_light_id>', methods=['POST'])
def toggle_fan_light(fan_light_id):
    if fan_light_id in fan_lights:
        # Toggle status
        fan_lights[fan_light_id]['status'] = 'on' if fan_lights[fan_light_id]['status'] == 'off' else 'off'
        return jsonify({'message': 'Toggle successful', 'status': fan_lights[fan_light_id]['status']}), 200
    else:
        return jsonify({'error': 'Fan light not found'}), 404

if __name__ == '_main_':
    app.run(debug=True)