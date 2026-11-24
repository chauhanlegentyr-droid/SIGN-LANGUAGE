from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# Complete Regional Dictionary Matrix mapping vocabulary terms to kinetic movements
DICTIONARY_METADATA = {
    "ASL": {
        "hello": {"label": "HELLO", "hand": "👋", "animation": "wave-motion"},
        "bathroom": {"label": "BATHROOM", "hand": "✊", "animation": "shake-motion"}, # ASL "T-Fist" Shake
        "where": {"label": "WHERE", "hand": "🤷", "animation": "shrug-motion"}
    },
    "JSL": {
        "hello": {"label": "こんにちは (Konnichiwa)", "hand": "🙇", "animation": "bow-motion"}, # JSL Polite Bow
        "bathroom": {"label": "お手洗い (Toire)", "hand": "👇", "animation": "point-motion"},
        "where": {"label": "どこ (Doko)", "hand": "🤨", "animation": "head-tilt-motion"} # Unique JSL Syntax Face
    },
    "ISL": {
        "hello": {"label": "NAMASTE", "hand": "🙏", "animation": "hands-together-motion"}, # Two hands pressed
        "bathroom": {"label": "BATHROOM", "hand": "✌️", "animation": "dive-motion"}, # ISL "V" Toilet sign
        "where": {"label": "KAHAN", "color": "#ff3333", "hand": "👐", "animation": "palms-up-motion"}
    }
}

def translate_text_to_kinetic_stream(input_text, language):
    if language not in DICTIONARY_METADATA:
        return []
        
    lang_catalog = DICTIONARY_METADATA[language]
    clean_text = input_text.lower().replace("?", "").replace(".", "").replace("!", "")
    words = clean_text.split()
    
    # Universal interrogative syntax flip configuration execution
    if "where" in words:
        words.remove("where")
        words.append("where")
        
    compiled_timeline = []
    for word in words:
        if word in lang_catalog:
            compiled_timeline.append(lang_catalog[word])
        else:
            # Fallback signature configuration if an unknown word is processed
            compiled_timeline.append({"label": word.upper(), "hand": "🤟", "animation": "idle-breath"})
            
    return compiled_timeline

@app.route('/api/translate', methods=['POST'])
def process_universal_translation():
    data = request.get_json()
    user_text = data.get('text', '')
    target_lang = data.get('language', 'ASL')
    
    timeline_data = translate_text_to_kinetic_stream(user_text, target_lang)
    return jsonify({"status": "success", "language": target_lang, "timeline": timeline_data})

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Universal Dynamic Sign Hub</title>
    <style>
        body { font-family: 'Segoe UI', system-ui, sans-serif; background-color: #0f0f15; color: #e4e4e7; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; box-sizing: border-box; }
        .dashboard-container { width: 1100px; background: #181825; border-radius: 20px; border: 1px solid #2d2d3d; display: flex; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.5); height: 640px; }
        
        .player-panel { width: 50%; padding: 30px; box-sizing: border-box; border-right: 1px solid #2d2d3d; display: flex; flex-direction: column; justify-content: space-between; }
        h2 { color: #fff; margin: 0 0 15px 0; font-size: 24px; font-weight: 700; display: flex; align-items: center; gap: 10px; }
        select, input { width: 100%; padding: 14px; margin: 8px 0 16px 0; border-radius: 10px; border: 1px solid #3f3f56; box-sizing: border-box; font-size: 15px; background: #11111a; color: #fff; }
        button { width: 100%; padding: 15px; margin: 5px 0; border-radius: 10px; border: none; font-weight: bold; font-size: 16px; cursor: pointer; transition: all 0.2s; background-color: #00b4d8; color: #fff; }
        button:hover { background-color: #0096b4; transform: translateY(-1px); }
        
        /* The Kinetic Sign Language Player Monitor Viewport Container */
        .flash-viewport { width: 100%; height: 300px; background-color: #0b0b11; border-radius: 14px; border: 2px solid #00b4d8; display: flex; flex-direction: column; justify-content: center; align-items: center; overflow: hidden; position: relative; }
        #hud { position: absolute; top: 15px; left: 15px; font-size: 12px; color: #71717a; font-family: monospace; }
        .caption { font-family: monospace; color: #00ffcc; font-size: 20px; margin-bottom: 5px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
        
        /* The Master 3D Hand Vector Node Core Container */
        .hand-vector-node { font-size: 95px; margin: 15px 0; display: inline-block; transform-origin: bottom center; transition: all 0.3s ease; }

        /* --- DYNAMIC TRANSFORMATION KINETIC LIBRARIES (CSS ANIMATIONS) --- */
        .idle-breath { animation: breath 2s infinite ease-in-out; }
        @keyframes breath { 0%, 100% { transform: scale(1) translateY(0); } 50% { transform: scale(1.03) translateY(-4px); } }

        .wave-motion { animation: wave 0.4s infinite ease-in-out alternate; }
        @keyframes wave { 0% { transform: rotate(-15deg); } 100% { transform: rotate(25deg); } }

        .shake-motion { animation: shake 0.15s infinite linear; }
        @keyframes shake { 0% { transform: translateX(-6px) rotate(-5deg); } 50% { transform: translateX(6px) rotate(5deg); } 100% { transform: translateX(-6px) rotate(-5deg); } }

        .shrug-motion { animation: shrug 0.8s infinite ease-in-out alternate; }
        @keyframes shrug { 0% { transform: scale(0.95) translateY(5px); } 100% { transform: scale(1.05) translateY(-8px); } }

        .bow-motion { animation: bow 1.2s infinite ease-in-out; }
        @keyframes bow { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(25px) rotate(10deg); } }

        .point-motion { animation: point 0.5s infinite ease-in-out alternate; }
        @keyframes point { 0% { transform: translateY(-10px); } 100% { transform: translateY(15px); } }

        .head-tilt-motion { animation: tilt 0.6s infinite ease-in-out alternate; }
        @keyframes tilt { 0% { transform: rotate(-10deg) scale(0.95); } 100% { transform: rotate(15deg) scale(1.05); } }

        .hands-together-motion { animation: press 0.7s infinite ease-in-out alternate; }
        @keyframes press { 0% { transform: scale(1); } 100% { transform: scale(1.15) rotate(-5deg); } }

        .dive-motion { animation: dive 0.9s infinite cubic-bezier(0.25, 1, 0.5, 1); }
        @keyframes dive { 0% { transform: translateY(-20px) scale(0.8) rotate(-10deg); opacity: 0.5; } 50% { opacity: 1; } 100% { transform: translateY(20px) scale(1.1) rotate(15deg); opacity: 0; } }

        .palms-up-motion { animation: palms 0.8s infinite ease-in-out alternate; }
        @keyframes palms { 0% { transform: scale(0.9) rotate(-8deg); } 100% { transform: scale(1.08) rotate(8deg); } }

        /* Right Panel Setup */
        .template-panel { width: 50%; padding: 30px; box-sizing: border-box; background: #1e1e2f; display: flex; flex-direction: column; }
        .template-card { background: #11111a; border: 1px solid #2d2d3d; padding: 15px; border-radius: 10px; margin-bottom: 12px; cursor: pointer; transition: all 0.2s; }
        .template-card:hover { border-color: #00b4d8; background: #141424; }
        .template-card h4 { margin: 0 0 6px 0; color: #fff; font-size: 15px; }
        .template-card p { margin: 0; color: #71717a; font-size: 13px; line-height: 1.4; }
    </style>
</head>
<body>

    <div class="dashboard-container">
        <div class="player-panel">
            <div>
                <h2>🌐 Universal Kinetic Engine</h2>
                <select id="langSelect">
                    <option value="ASL">ASL Module (Kinetic Filters)</option>
                    <option value="JSL">JSL Module (Kinetic Filters)</option>
                    <option value="ISL">ISL Module (Kinetic Filters)</option>
                </select>
                <input type="text" id="msgInput" placeholder="Type your message here..." value="bathroom where">
                <button onclick="bootKineticStream()">Animate Vector Signs</button>
            </div>
            
            <div class="flash-viewport">
                <div id="hud">Engine: Standby</div>
                <div class="caption" id="wordCaption">AWAITING SEQUENCE</div>
                <!-- The Live Hand Vector Component Node -->
                <div class="hand-vector-node idle-breath" id="handVector">🤟</div>
            </div>
        </div>

        <div class="template-panel">
            <h3 style="margin: 0 0 15px 0; font-size: 18px; color: #fff;">Quick Conversation Mappers</h3>
            <div class="template-card" onclick="document.getElementById('msgInput').value='bathroom where'">
                <h4>🚽 Facility Locator Sequence</h4>
                <p>Loads core interrogative flip string target: "bathroom where"</p>
            </div>
            <div class="template-card" onclick="document.getElementById('msgInput').value='hello'">
                <h4>👋 Core Initialization Greeting</h4>
                <p>Loads initial greeting track: "hello"</p>
            </div>
            <div class="template-card" onclick="document.getElementById('msgInput').value='hello bathroom where'">
                <h4>🛠️ Full Structural Compound Sentence</h4>
                <p>Runs a full composite conversation sequence chain: "hello bathroom where"</p>
            </div>
        </div>
    </div>

    <script>
        let streamTimeline = [];
        let trackerIndex = 0;

        function bootKineticStream() {
            const msg = document.getElementById('msgInput').value;
            const lang = document.getElementById('langSelect').value;
            const hud = document.getElementById('hud');
            
            hud.innerText = "Processing vector kinematics...";
            
            fetch('/api/translate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: msg, language: lang })
            })
.then(res => res.json())
.then(data => {
streamTimeline = data.timeline;
trackerIndex = 0;
executeKineticLoop(data.language);
});
}
function executeKineticLoop(activeLang) {
const handEl = document.getElementById('handVector');
const capEl = document.getElementById('wordCaption');
const hudEl = document.getElementById('hud');
if (trackerIndex >= streamTimeline.length) {
hudEl.innerText = "Engine Status: Done";
capEl.innerText = "SEQUENCE FINISHED";
handEl.className = "hand-vector-node idle-breath";
handEl.innerText = "✅";
return;
}
const currentFrame = streamTimeline[trackerIndex];
hudEl.innerHTML = "Active Pipeline: " + activeLang + " Module Engine Running";
capEl.innerText = currentFrame.label;
// Swap out the physical handshape configuration structure string dynamically
handEl.innerText = currentFrame.hand;
// Wipe out old motion templates and attach the new target animation matrix style class
handEl.className = "hand-vector-node " + currentFrame.animation;
trackerIndex++;
// Keeps the vector sign loop active for 1.8 seconds before triggering the next word node sequence
setTimeout(() => executeKineticLoop(activeLang), 1800);
}
    </script>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True, port=5000)