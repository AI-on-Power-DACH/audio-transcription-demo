# Audio Transcription Demo using whisper.cpp

## Description

This repository contains a sample installation of whisper.cpp and a UI to transcribe audio files.

- `ansible`: contains all Ansible-related files
- `src`: contains the frontend to interact with the whisper.cpp service 


## Usage

First, adjust the `inventory.yml` in the `ansible` directory as needed.
Execute the `local-setup.yml` playbook to download all additional playbooks needed for setting up this demo:

```shell
$ ansible-playbook -i ansible/inventory.yml ansible/local-setup.yml
```

Next, deploy the whisper.cpp service:

```shell
$ ansible-playbook -i ansible/inventory.yml ansible/basic-whisper.cpp.yml
```

Lastly, deploy the UI:

```shell
$ ansible-playbook -i ansible/inventory.yml ansible/deploy-ui.yml
```

The UI should now be available under the hostname and port you specified in the `inventory.yml` (defaults to `http://<LPAR IP>:7860`).
The whisper.cpp inferencing endpoint is available under the specified hostname and port from the `inventory.yml` (defaults to `http://<LPAR IP>:8080/inference`).