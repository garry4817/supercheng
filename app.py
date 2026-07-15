import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import logic
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    """獲取實時數據"""
    return jsonify(logic.data)

@app.route('/api/update', methods=['POST'])
def update_data():
    """更新數據"""
    req_data = request.get_json()
    
    for key, value in req_data.items():
        if key in logic.data:
            setattr(logic, key, value)
            logic.data[key] = value
    
    return jsonify({'status': 'success', 'data': logic.data})

@app.route('/api/data/<key>', methods=['GET'])
def get_value(key):
    """獲取特定值"""
    if key in logic.data:
        return jsonify({key: logic.data[key]})
    return jsonify({'error': 'Key not found'}), 404

@app.route('/api/health', methods=['GET'])
def health():
    """檢查伺服器狀態"""
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    # 使用環境變數中的 PORT，預設為 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)