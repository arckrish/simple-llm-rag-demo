# vLLM Deployment

Example deployment of the [vLLM](https://github.com/vllm-project/vllm) server for OpenShift.

This deployment uses a UBI9 image defined in `Containerfile` and accessible at `quay.io/rh-aiservices-bu/vllm-openai-ubi9` (check for the latest version available).

This image implement the OpenAI API interface for maximum compatibility with other tools. See [here](https://docs.vllm.ai/en/latest/getting_started/quickstart.html#openai-compatible-server) for more information.

A notebook example using Langchain is available [here](../../examples/notebooks/langchain/Langchain-vLLM-Prompt-memory.ipynb).

## Installation

The default installation deploys the [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) model. Although on the smaller side of LLMs, it will still require a GPU to work properly in a fast enough manner. See [Advanced installation](#advanced-installation) for instructions on how to change the model as well as various settings.

### Automated Deployment

- Use the OpenShift GitOps/ArgoCD Application definition at `gitops/vllm-app.yaml`

### Manual Deployment using Kustomize

After logging in to OpenShift, run the following commands:

```bash
$ oc new-project vllm
$ kustomize build https://github.com/arckrish/simple-llm-rag-demo.git/vllm/gpu/gitops | oc apply -f -
```

You can also replace the github.com URL in the kustomize command with a local path instead, if this repository has been locally cloned.

### Manual Deployment 

Using the contents of the [gitops folder](gitops), perform the following steps:

- Create PVC named `vllm-models-cache` with enough space to hold all the models you want to try.
- Create the Deployment using the file [deployment.yaml](gitops/deployment.yaml).
- Create the Service using file [service.yaml](gitops/service.yaml).
- If you want to expose the server outside of your OpenShift cluster, create the Route with the file [route.yaml](gitops/route.yaml)

