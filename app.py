from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
from datetime import datetime, timedelta
from Utilities.until import load_accounts
from Api.Account import get_garena_token, get_major_login
from Api.InGame import get_player_personal_show, get_player_stats, search_account_by_keyword


accounts = load_accounts()


app = Flask(__name__)
# Enable CORS for all origins on all routes
CORS(app)


@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JuTt X Hacker | Matric Fail Hacker API</title>

<!-- Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@500&display=swap" rel="stylesheet">

<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
    background: #0d0d0d;
    font-family: 'Share Tech Mono', monospace;
    color: #00ffcc;
    overflow-x: hidden;
    scroll-behavior: smooth;
}

/* Fixed Header with stacked branding */
header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(13,13,13,0.95);
    backdrop-filter: blur(5px);
    z-index: 999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px 10px;
    border-bottom: 1px solid #00ffcc;
    text-align: center;
}
header h1 {
    font-family: 'Orbitron', sans-serif;
    font-size: 36px;
    font-weight: bold;
    color: #00ffcc;
    text-shadow: 0 0 10px #00ffcc,0 0 20px #00ffcc;
    margin-bottom: 5px;
}
header h2 {
    font-family: 'Share Tech Mono', monospace;
    font-size: 18px;
    color: #ff00ff;
    text-shadow: 0 0 8px #ff00ff,0 0 16px #ff00ff;
}

/* Spacer so content is below navbar */
.spacer { height: 90px; }

/* Social Links */
.social-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    margin: 50px 0;
}
.social-links a {
    text-decoration: none;
    color: #00ffff;
    border: 1px solid #00ffff;
    padding: 14px 28px;
    border-radius: 10px;
    font-size: 18px;
    transition: all 0.3s ease-in-out;
}
.social-links a:hover {
    color: black;
    background: #00ffff;
    box-shadow: 0 0 20px #00ffff,0 0 40px #00ffff;
}

/* API Section */
.api-container {
    max-width: 900px;
    margin: 60px auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
    padding: 0 20px;
}
.api-card {
    background: rgba(0,255,204,0.07);
    border: 1px solid #00ffcc;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 0 15px #00ffcc;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.api-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 25px #00ffcc, 0 0 50px #00ffcc;
}
.api-card h3 {
    color: #ff00ff;
    margin-bottom: 15px;
    text-shadow: 0 0 10px #ff00ff,0 0 20px #ff00ff;
}
.api-card code {
    display: block;
    background: #0d0d0d;
    color: #00ffcc;
    padding: 14px;
    border-radius: 10px;
    font-size: 14px;
    overflow-x: auto;
}

/* Footer */
footer {
    text-align: center;
    margin: 80px 0 40px 0;
    font-size: 14px;
    color: #00ffcc;
}

/* Particles optimized */
#particles-js {
    position: fixed;
    top:0; left:0;
    width:100%; height:100%;
    z-index:-1;
    pointer-events:none;
}
</style>
</head>
<body>

<!-- Particles -->
<div id="particles-js"></div>

<header>
    <h1>JuTt X Hacker</h1>
    <h2>Matric Fail Hacker</h2>
</header>

<div class="spacer"></div>

<div class="social-links">
    <a href="https://youtube.com/@matricfailhacker?si=zGxShSh7SdX7xpDR" target="_blank">YouTube</a>
    <a href="https://whatsapp.com/channel/0029Vb5czH6IXnllDW2uNs1i" target="_blank">WhatsApp</a>
    <a href="mailto:Juttxhacker12@gmail.com" target="_blank">Email</a>
</div>

<div class="api-container">
    <div class="api-card">
        <h3>Get Player Personal Show</h3>
        <code>https://ff-infobyjxh.vercel.app/get_player_personal_show?server=pk&uid=11647508073</code>
    </div>
    <div class="api-card">
        <h3>Get Player Stats</h3>
        <code>https://ff-infobyjxh.vercel.app/get_player_stats?server=pk&uid=11647508073</code>
    </div>
    <div class="api-card">
        <h3>Search Account By Keyword</h3>
        <code>https://ff-infobyjxh.vercel.app/get_search_account_by_keyword?server=pk&keyword=jut</code>
    </div>
</div>

<footer>
&copy; 2026 JuTt X Hacker | Matric Fail Hacker
</footer>

<!-- Particles.js -->
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script>
particlesJS("particles-js", {
  "particles": {
    "number": {"value":35,"density":{"enable":true,"value_area":700}},
    "color":{"value":"#00ffcc"},
    "shape":{"type":"circle"},
    "opacity":{"value":0.5,"random":true},
    "size":{"value":2.5,"random":true},
    "line_linked":{"enable":true,"distance":100,"color":"#00ffcc","opacity":0.25,"width":1},
    "move":{"enable":true,"speed":1.5,"out_mode":"out"}
  },
  "interactivity":{
    "detect_on":"canvas",
    "events":{"onhover":{"enable":true,"mode":"grab"},"onclick":{"enable":true,"mode":"push"}}
  }
});
</script>

</body>
</html>
    """

@app.route('/get_search_account_by_keyword', methods=['GET'])
def get_search_account_by_keyword():
    try:
        # Get request parameters
        region = request.args.get('server', 'IND').upper()
        search_term = request.args.get('keyword')
        
        # Validate keyword parameter
        if not search_term:
            return json.dumps({"error": "Keyword parameter is required"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Enforce minimum keyword length
        if len(search_term.strip()) < 3:
            return json.dumps({"error": "Keyword must be at least 3 characters long"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate server exists in accounts
        if region not in accounts:
            return json.dumps({"error": f"Invalid server: {region}"}, indent=2), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Authenticate with Garena
        auth_response = get_garena_token(accounts[region]['uid'], accounts[region]['password'])
        if not auth_response or 'access_token' not in auth_response:
            return json.dumps({"error": "Authentication failed"}, indent=2), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Get major login credentials
        login_response = get_major_login(auth_response["access_token"], auth_response["open_id"])
        if not login_response or 'token' not in login_response:
            return json.dumps({"error": "Major login failed"}, indent=2), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Search for accounts
        search_results = search_account_by_keyword(login_response["serverUrl"], login_response["token"], search_term)
        
        # Return formatted response
        formatted_response = json.dumps(search_results, indent=2, ensure_ascii=False)
        return formatted_response, 200, {'Content-Type': 'application/json; charset=utf-8'}
        
    except KeyError as e:
        return json.dumps({"error": f"Missing configuration: {str(e)}"}, indent=2), 500, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return json.dumps({"error": f"Internal server error: {str(e)}"}, indent=2), 500, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/get_player_stats', methods=['GET'])
def get_player_stat():
    try:
        # Get and validate parameters
        server = request.args.get('server', 'IND').upper()
        uid = request.args.get('uid')
        gamemode = request.args.get('gamemode', 'br').lower()
        matchmode = request.args.get('matchmode', 'CAREER').upper()

        # Validate required parameters
        if not uid:
            return jsonify({
                "success": False,
                "error": "Missing required parameter",
                "message": "UID parameter is required"
            }), 400

        if not uid.isdigit():
            return jsonify({
                "success": False,
                "error": "Invalid UID",
                "message": "UID must be a numeric value"
            }), 400

        # Validate server
        if server not in accounts:
            return jsonify({
                "success": False,
                "error": "Invalid server",
                "message": f"Server '{server}' not found. Available servers: {list(accounts.keys())}"
            }), 400

        # Validate gamemode
        if gamemode not in ['br', 'cs']:
            return jsonify({
                "success": False,
                "error": "Invalid gamemode",
                "message": "Gamemode must be 'br' or 'cs'"
            }), 400

        # Validate matchmode
        if matchmode not in ['CAREER', 'NORMAL', 'RANKED']:
            return jsonify({
                "success": False,
                "error": "Invalid matchmode",
                "message": "Matchmode must be 'CAREER', 'NORMAL', or 'RANKED'"
            }), 400

        # Step 1: Get Garena token
        try:
            garena_token_result = get_garena_token(accounts[server]['uid'], accounts[server]['password'])
            
            if not garena_token_result or 'access_token' not in garena_token_result:
                return jsonify({
                    "success": False,
                    "error": "Garena authentication failed",
                    "message": "Failed to obtain Garena access token"
                }), 401
                
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Garena authentication error",
                "message": f"Failed to authenticate with Garena: {str(e)}"
            }), 502

        # Step 2: Get Major login
        try:
            major_login_result = get_major_login(garena_token_result["access_token"], garena_token_result["open_id"])
            
            if not major_login_result or 'token' not in major_login_result:
                return jsonify({
                    "success": False,
                    "error": "Major login failed",
                    "message": "Failed to obtain Major login token"
                }), 401
                
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Major login error",
                "message": f"Failed to login to Major: {str(e)}"
            }), 502

        # Step 3: Get player stats
        try:
            player_stats = get_player_stats(
                major_login_result["token"], 
                major_login_result["serverUrl"], 
                gamemode, 
                uid, 
                matchmode
            )
            
            if not player_stats:
                return jsonify({
                    "success": False,
                    "error": "No stats data",
                    "message": "No player statistics found for the given parameters"
                }), 404

            # Return formatted JSON response
            return jsonify({
                "success": True,
                "data": player_stats,
                "metadata": {
                    "server": server,
                    "uid": uid,
                    "gamemode": gamemode,
                    "matchmode": matchmode
                }
            }), 200
            
        except ValueError as e:
            return jsonify({
                "success": False,
                "error": "Invalid request parameters",
                "message": str(e)
            }), 400
        except ConnectionError as e:
            return jsonify({
                "success": False,
                "error": "Connection error",
                "message": str(e)
            }), 503
        except ProtobufError as e:
            return jsonify({
                "success": False,
                "error": "Data processing error",
                "message": str(e)
            }), 500
        except APIError as e:
            return jsonify({
                "success": False,
                "error": "External API error",
                "message": str(e)
            }), 502
        except Exception as e:
            return jsonify({
                "success": False,
                "error": "Stats retrieval error",
                "message": f"Failed to retrieve player stats: {str(e)}"
            }), 500

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({
            "success": False,
            "error": "Internal server error",
            "message": "An unexpected error occurred while processing your request"
        }), 500

@app.route('/get_player_personal_show', methods=['GET'])
def get_account_info():
    try:
        # Get parameters with defaults
        server = request.args.get('server', 'IND').upper()
        uid = request.args.get('uid')
        need_gallery_info = request.args.get('need_gallery_info', False)
        call_sign_src = request.args.get('call_sign_src', 7)
        
        # Validate UID parameter - must be integer
        if not uid:
            response = {
                "status": "error",
                "error": "Missing UID",
                "message": "Empty 'uid' parameter. Please provide a valid 'uid'.",
                "code": "MISSING_UID"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Check if UID is a valid integer
        try:
            uid_int = int(uid)
            # Additional validation for UID range if needed
            if uid_int <= 0:
                response = {
                    "status": "error",
                    "error": "Invalid UID",
                    "message": "UID must be a positive integer.",
                    "code": "INVALID_UID_RANGE"
                }
                return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid UID",
                "message": "UID must be a valid integer.",
                "code": "INVALID_UID_FORMAT"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate server parameter
        if server not in accounts:
            response = {
                "status": "error",
                "error": "Invalid Server",
                "message": f"Server '{server}' not found. Available servers: {list(accounts.keys())}",
                "available_servers": list(accounts.keys()),
                "code": "SERVER_NOT_FOUND"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate need_gallery_info parameter
        try:
            if isinstance(need_gallery_info, str):
                if need_gallery_info.lower() in ['true', '1', 'yes']:
                    need_gallery_info = True
                elif need_gallery_info.lower() in ['false', '0', 'no']:
                    need_gallery_info = False
                else:
                    raise ValueError("Invalid boolean value")
            need_gallery_info = bool(need_gallery_info)
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid Parameter",
                "message": "need_gallery_info must be a boolean value (true/false, 1/0).",
                "code": "INVALID_GALLERY_PARAM"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Validate call_sign_src parameter
        try:
            call_sign_src_int = int(call_sign_src)
            if call_sign_src_int < 0:
                response = {
                    "status": "error",
                    "error": "Invalid Parameter",
                    "message": "call_sign_src must be a non-negative integer.",
                    "code": "INVALID_CALL_SIGN_SRC"
                }
                return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        except (ValueError, TypeError):
            response = {
                "status": "error",
                "error": "Invalid Parameter",
                "message": "call_sign_src must be a valid integer.",
                "code": "INVALID_CALL_SIGN_FORMAT"
            }
            return jsonify(response), 400, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Check if server account credentials exist
        if 'uid' not in accounts[server] or 'password' not in accounts[server]:
            response = {
                "status": "error",
                "error": "Server Configuration Error",
                "message": f"Server '{server}' is missing required credentials.",
                "code": "SERVER_CONFIG_ERROR"
            }
            return jsonify(response), 500, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 1: Get Garena token
        garena_token_result = get_garena_token(accounts[server]['uid'], accounts[server]['password'])
        if not garena_token_result or 'access_token' not in garena_token_result or 'open_id' not in garena_token_result:
            response = {
                "status": "error",
                "error": "Authentication Failed",
                "message": "Failed to obtain Garena token. Invalid credentials or service unavailable.",
                "code": "GARENA_AUTH_FAILED"
            }
            return jsonify(response), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 2: Get major login
        major_login_result = get_major_login(garena_token_result["access_token"], garena_token_result["open_id"])
        if not major_login_result or 'serverUrl' not in major_login_result or 'token' not in major_login_result:
            response = {
                "status": "error",
                "error": "Login Failed",
                "message": "Failed to perform major login. Service unavailable.",
                "code": "MAJOR_LOGIN_FAILED"
            }
            return jsonify(response), 401, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Step 3: Get player personal show data
        player_personal_show_result = get_player_personal_show(
            major_login_result["serverUrl"], 
            major_login_result["token"], 
            uid_int, 
            need_gallery_info, 
            call_sign_src_int
        )

        if not player_personal_show_result:
            response = {
                "status": "error",
                "error": "Data Not Found",
                "message": f"No player data found for UID: {uid_int}",
                "code": "PLAYER_DATA_NOT_FOUND"
            }
            return jsonify(response), 404, {'Content-Type': 'application/json; charset=utf-8'}
        
        # Success response
        formatted_json = json.dumps(player_personal_show_result, indent=2, ensure_ascii=False)
        return formatted_json, 200, {'Content-Type': 'application/json; charset=utf-8'}
    
    except Exception as e:
        # Log the unexpected error for debugging
        print(f"Unexpected error in get_player_personal_show: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        
        response = {
            "status": "error",
            "error": "Internal Server Error",
            "message": "An unexpected error occurred while processing your request.",
            "code": "INTERNAL_SERVER_ERROR"
        }
        return jsonify(response), 500, {'Content-Type': 'application/json; charset=utf-8'}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)