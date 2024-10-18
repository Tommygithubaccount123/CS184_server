from flask import Flask, request, jsonify
import populartimes, dotenv, os

# load env_var
dotenv.load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")


@app.route('/gym', methods=['GET'])
def process_data():
    try:
        data = request.get_json()

        # check if token is valid
        if data['token'] != TOKEN:
            raise Exception('Invalid token')

        result = get_rec_cen_data()
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

def get_rec_cen_data():
    # rec cen id
    place_id = "ChIJ9cr5_WQ_6YARXHdQRCb-xeY"
    return populartimes.get_id(api_key=API_KEY, place_id=place_id)

if __name__ == "__main__":
    app.run(port=1000, debug=True)
