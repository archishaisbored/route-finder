from flask import Flask, request, jsonify
from route_calculator import get_route  # Import the simplified script

app = Flask(__name__)

@app.route('/calculate_route', methods=['POST'])
def calculate_route():
    # Get JSON data from the request
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input, JSON required.'}), 400

    # Extract start and end coordinates
    try:
        start = data['start']  # Expected as [latitude, longitude]
        end = data['end']      # Expected as [latitude, longitude]
    except KeyError:
        return jsonify({'error': 'Missing start or end coordinates.'}), 400

    # Validate coordinate format
    if not (isinstance(start, list) and isinstance(end, list) and
            len(start) == 2 and len(end) == 2):
        return jsonify({'error': 'Coordinates must be [lat, lon] lists.'}), 400

    # Calculate the route
    try:
        route = get_route(start, end)
        return jsonify({'route': route}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)