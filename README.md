# ALBERT

[ALBERT](https://arxiv.org/abs/1909.11942) is a transformers model pretrained on a large corpus of English data in a
self-supervised fashion. ALBERT was proposed by Google. We can use ALBERT to accomplish these 2 tasks: taking a
sentence, ALBERT randomly masks 15% of the words in the input then run the entire masked sentence through ALBERT
and has to predict the masked words; predicting the order of two consecutive text segments with ALBERT. ALBERT can
only handle English input.

## 1. Create a new Notebook Server

Create a new Notebook Server on the Kubeflow on vSphere platform.

- You can create your own custom image or use an image published by us here:

  `projects.registry.vmware.com/models/notebook/hf-inference-deploy@sha256:8c5960ce436881f37336b12556d7a661ea20e4dbfe9ac193516cf384daa51c19`

- set 2 CPUs, 4GB memory for this Notebook Server.

## 2. Connect to the Notebook Server

Open a Terminal window. Pull the code of this project by running

`git clone https://github.com/blueskyztt/ALBERT.git`

## 3. Download model

- (Option1) Download the model from https://huggingface.co/albert-base-v2/tree/main and put all model
  files in `./albert` directory which under the current directory.

- (Option2) Alternatively, you can download the model with the script `Download_model.py`, an example is
  in `prepare.sh`. 

```shell
bash ./prepare.sh
```

Finally, The directory structure is as follows:

```text
./albert
├── README.md
├── config.json
├── flax_model.msgpack 
├── model.safetensors 
├── pytorch_model.bin 
├── rust_model.ot 
├── spiece.model
├── tf_model.h5 
├── tokenizer.json
└── with-prefix-tf_model.h5
```

## 4. Preparation

### 4.1 Python requirements
Install the python packages necessary for the service, listed in `requirements.txt`.

```shell
pip install -r ./requirements.txt
```

## 5. Create TorchServe Model Archiver File

```shell
bash ./create_mar.sh
```

After waiting for a while, we got the mar file needed for the service. Then we can start our service.

## 6. Start TorchServe

Now you can start service with below command.

```shell
bash ./start_ts.sh
```

## 7. Test Service

Request the service in the terminal, execute

```shell
python ./client.py
```

After a while, you will see the output of the model in the terminal.

