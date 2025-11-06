from flask import Flask, render_template, request, jsonify
import os
from coremind.core_engine import CoreMindEngine
from coremind.resource_monitor import ResourceMonitor
from coremind.privacy_controller import PrivacyController
from coremind.feature_packs.chat_pack import ChatFeaturePack
from coremind.feature_packs.code_assistant_pack import CodeAssistantPack
from coremind.feature_packs.file_summary_pack import FileSummaryPack

# Set template and static folders explicitly
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'web_ui', 'templates')
static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'web_ui', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Instantiate main components
engine = CoreMindEngine()
monitor = ResourceMonitor()
privacy = PrivacyController()

# Load feature packs
chat_pack = ChatFeaturePack(engine)
code_pack = CodeAssistantPack(engine)
summary_pack = FileSummaryPack(engine)

engine.load_feature_pack('Chat Assistant', chat_pack)
engine.load_feature_pack('Code Assistant', code_pack)
engine.load_feature_pack('File Summarizer', summary_pack)

@app.route('/')
def index():
    system = monitor.get_system_info()
    packs = engine.list_feature_packs()
    return render_template('index.html', system=system, packs=packs)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    result = chat_pack.process(user_input)
    privacy.log_operation('Chat Inference', f'User: {user_input}')
    return jsonify({'response': result})

@app.route('/code', methods=['POST'])
def code_assist():
    code = request.form.get('code')
    question = request.form.get('question')
    result = code_pack.process(code, question or "")
    privacy.log_operation('Code Analysis', f'Code snippet received (length: {len(code)})')
    return jsonify({'response': result})

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form.get('text')
    result = summary_pack.process(text)
    privacy.log_operation('File Summarization', f'Text received (length: {len(text)})')
    return jsonify({'response': result})

@app.route('/resources')
def resources():
    usage = monitor.get_current_usage()
    recommended = monitor.recommend_model()
    status = monitor.get_health_status()
    return jsonify({
        'usage': usage,
        'recommended': recommended,
        'status': status
    })

@app.route('/privacy')
def privacy_status():
    stats = privacy.get_privacy_stats()
    return jsonify(stats)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
