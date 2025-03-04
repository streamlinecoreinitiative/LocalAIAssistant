# Offline AI Assistant

This project is an offline AI chatbot using Mistral 7B for text-based interactions and ChromaDB for memory storage. It can remember past conversations, answer questions, and operate entirely without an internet connection.

## Features
- Offline AI – No internet required.
- Persistent Memory – Stores user conversations in ChromaDB.
- Fast Responses – Runs locally on CPU/GPU.
- Lightweight Setup – Works on low-resource machines.

## 1. Installation Guide

### System Requirements

| Component | Minimum                        | Recommended                           |
|-----------|--------------------------------|---------------------------------------|
| CPU       | Intel i5 / Ryzen 5             | Intel i7 / Ryzen 7                     |
| RAM       | 8GB                            | 16GB+                                  |
| Storage   | 20GB Free                      | 50GB SSD                               |
| OS        | Windows 10/11, Ubuntu 22.04+   | Windows 11, Ubuntu 22.04+              |
| GPU       | Not required                   | NVIDIA GTX 1650+ (for acceleration)    |

### Step 1: Install Dependencies

#### Windows
1. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Install Ollama from [https://ollama.com/download](https://ollama.com/download).
3. Open Command Prompt and run:
   ```sh
   pip install chromadb
   ```

#### Linux (Ubuntu/Debian)
1. Open Terminal and run:
   ```sh
   sudo apt update && sudo apt install python3 python3-pip curl -y
   curl -fsSL https://ollama.com/install.sh | sh
   pip install chromadb
   ```

### Step 2: Setting Up AI Memory

ChromaDB is used for storing and retrieving conversations.

1. Clone this repository:
   ```sh
   git clone https://github.com/YOUR-USERNAME/OFFLINE-AI-ASSISTANT.git
   cd OFFLINE-AI-ASSISTANT
   ```
2. Run the memory manager:
   ```sh
   python memory.py
   ```
   - This initializes ChromaDB and prepares the memory storage.

### Step 3: Running the AI Assistant

Once Mistral 7B and ChromaDB are installed, launch the AI assistant.
```sh
python ai_assistant.py
```

#### How to Use:
- Type your questions or statements.
- The AI will respond based on memory and stored knowledge.
- Type “exit” to stop the program.

### Step 4: How Memory Works
- The assistant saves important user details in ChromaDB.
- By default, it remembers past conversations unless explicitly erased.

**Forget Everything:**

To reset memory, type:
```
forget everything
```
This will delete all stored interactions.

### Step 5: Use Cases
This AI can be used for:
- Education – Acts as a personal tutor.
- Small Business – Automates customer FAQs.
- Remote Areas – Provides offline information access.
- Accessibility – Helps people with disabilities.

### Step 6: Future Improvements
- Add Voice Support – Integrate Speech-to-Text.
- Multi-Language Support – Expand AI capabilities.
- Web Interface – Create a UI using Flask.

### Step 7: Contributing
Feel free to submit issues, pull requests, or suggestions.

## License
This project is open-source under the MIT License.
