def register_routes(app):
    @app.route('/send', methods=['POST'])
    def send_message():
        from flask import request
        data = request.get_json()
        print("Received:", data)
        return {"status": "ok"}
