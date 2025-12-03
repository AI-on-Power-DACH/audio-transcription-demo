# Audio Transcription Demo 🚀

## 🎯 Overview

This repository provides a compact demo installation of whisper.cpp including a web UI for transcribing audio files. The goal is to give you a quick and straightforward introduction to local speech-to-text transcription on ppc64le systems.

- whisper.cpp serves as the transcription backend
- The UI in the src folder makes it simple: upload an audio file and receive text

## 🧰 Contents

| Folder   | Purpose                                                            |
| -------- | ------------------------------------------------------------------ |
| ansible/ | All Ansible configurations & playbooks required to set up the demo |
| src/     | Frontend/UI for interacting with the whisper.cpp service           |


## 🚀 Quick Start – in Three Steps

1. Adjust the `ansible/inventory.yml` file to match your environment if needed.
2. Download all required playbooks and start the setup:
```shell
ansible-playbook -i ansible/inventory.yml ansible/local-setup.yml
```
3. Deploy the transcription service:
```shell
ansible-playbook -i ansible/inventory.yml ansible/basic-whisper.cpp.yml
```
4. (optional) Deploy the web UI:
```shell
ansible-playbook -i ansible/inventory.yml ansible/deploy-ui.yml
```

Afterwards, the UI will be available at the address defined in `inventory.yml` (default: `http://<LPAR IP>:7860`). The whisper.cpp inference endpoint runs at `http://<LPAR IP>:8080/inference`.


## 💡 Why This Demo Is Useful

- ✅ Quick start for local audio-to-text transcription — no complex setup required
- 🛠️ Automated setup via Ansible — ideal for developers and system administrators
- 🔐 Local & independent — no external APIs or cloud services required
- 🧑‍💻 Flexible & transparent — full access to all code and infrastructure
