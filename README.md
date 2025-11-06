# CoreMind AI - Offline-First Modular Artificial Intelligence Architecture

## Overview

CoreMind AI is a modular, offline-first artificial intelligence system designed to operate autonomously on user devices (laptops, desktops) without requiring continuous cloud connectivity. It addresses critical challenges of data privacy, network dependency, and user sovereignty over AI processes.

The system supports dynamic loading of feature packs such as chat assistance, code analysis, and document summarization, enabling extensible AI capabilities that run entirely locally on consumer-grade hardware. Adaptive resource management ensures efficient performance based on real-time hardware monitoring, while a privacy controller enforces audit logging and local-only processing.

## Features

- **Offline AI inference:** AI models run locally without internet access or cloud dependency.
- **Modular architecture:** Dynamically loadable feature packs that can be added or removed at runtime without restart.
- **Adaptive resource management:** Monitors CPU, RAM, and thermal conditions to select optimal AI model variants.
- **Privacy-first design:** Comprehensive audit logging and data encryption with zero external network calls.
- **Web-based user interface:** Responsive and intuitive GUI built with Flask and Bootstrap.
- **Multiple AI capabilities:** Includes chat assistant, code assistant, and document summarizer feature packs.

## Implementation Details

- **Language:** Python 3.12.7
- **Framework:** Flask 3.0.0 for the web interface
- **AI Engine:** Ollama (local LLM inference) with Llama 3.2 1B quantized model
- **Resource Monitoring:** psutil 5.9.6 for system metrics
- **Operating System:** Tested on Windows 11 with 16GB RAM
- **Architecture:** Four layers - User Interface, CoreMind Engine, AI Processing Layer, Data Layer

## Getting Started

### Prerequisites

- Python 3.12 or later
- Ollama LLM server installed and running locally
- Llama 3.2 1B quantized model downloaded in Ollama
- Recommended OS: Windows 10/11 or Linux

### Installation
1. Clone this repository  
git clone <your-repository-url>
cd CoreMindAI

2. Install Python dependencies  
pip install -r requirements.txt

3. Download and start Ollama LLM server  
ollama pull llama3.2:1b
ollama serve

4. Start the CoreMind AI web application  
python web_ui/app.py

5. Open your web browser and navigate to  
http://localhost:8080

## Usage

- Use the web interface to access different AI feature packs:
- Chat Assistant for conversational AI
- Code Assistant for code analysis and debugging
- File Summarizer for document summarization

- Monitor system resource usage and privacy audit logs in real-time from the dashboard.

- Dynamically load or unload feature packs as needed without restarting the application.

## Testing

Comprehensive functional and non-functional test cases have been performed including:

- Offline AI inference validation  
- Dynamic module loading/unloading  
- Code analysis correctness  
- Summarization accuracy  
- Resource monitoring accuracy  
- Privacy compliance (zero external network calls)  
- Performance and scalability analysis

Refer to the `CoreMind-TestCases-Final.pdf` document for detailed test results.

## Project Structure
CoreMindAI/
├── coremind/
│ ├── core_engine.py
│ ├── resource_monitor.py
│ ├── privacy_controller.py
│ └── feature_packs/
│ ├── chat_pack.py
│ ├── code_assistant_pack.py
│ └── file_summary_pack.py
├── web_ui/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
├── requirements.txt
└── README.md

## Contributing

Contributions and suggestions are welcome! Please fork the repository and submit pull requests for new feature packs or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

Arman Ranjan  
Email: armanranjangs@gmail.com  
VIT University, Chennai, India

---

Thank you for using CoreMind AI — the future of private, offline-first artificial intelligence!  


1. Clone this repository  
