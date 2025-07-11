from huggingface_hub import snapshot_download

# Specify the Hugging Face repository containing the model
model_repo = "ibm-granite/granite-3.1-2b-instruct"
#model_repo = "meta-llama/Llama-3.2-3B-Instruct"
snapshot_download(
    repo_id=model_repo,
    local_dir="/models",
    allow_patterns=["*.safetensors", "*.json", "*.txt"],
)