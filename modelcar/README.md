# modelcar

This folder contains resources and instructions for building and deploying the `modelcar-example` container image.

## Build the Container Image

To build the container image for `modelcar-example` targeting the `linux/amd64` platform, run:

```sh
podman build . -t modelcar-example:latest --platform linux/amd64 
```

## Push to Container Registry

Replace <your-registry> with your actual Quay.io registry namespace and push the image:

```sh
podman push modelcar-example:latest quay.io/<your-registry>/modelcar-example:latest
```

## Deploy to RHOAI
* To begin, create a new project in the OpenShift AI dashboard where you plan to deploy your model.

* Next you will need to choose the Select single-model option in the Single-model serving platform section.

* Click the option to Deploy model

```
Model deployment name: granite-3.1-2b-instruct
Serving runtime: vLLM ServingRuntime for KServe
Number of model server replicas to deploy: 1
Model server size: Small
Accelerator: nvidia-gpu
Number of accelerators: 1
Model route: Checked
Token authentication: Unchecked 
Connection Type: UR-v1
Connection name: granite-3.1-8b-instruct
URI: oci://quay.io/redhat-ai-services/modelcar-catalog:granite-3.1-2b-instruct
```

