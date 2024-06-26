from pathlib import Path 

def get_config():
    return {
        "batch_size": 2048*2,
        "num_epochs": 18,
        "lr": 10**-3,
        "seq_len": 160,
        "d_model": 512,
        "lang_src": "en",
        "lang_tgt": "it",
        "model_folder": "weights",
        "model_basename": "tmodel_",
        "preload": False,
        "tokenizer_file": "tokenizer_{0}.json",
        "experiment_name": "rus/tmodel_param_grad_zero",
    }

def get_weights_file_path(config, epoch:str):
    model_folder = config['model_folder']
    model_basename = config['model_basename']
    model_filename = f"{model_basename}{epoch}.pt"
    return str(Path(".") / model_folder / model_filename)
