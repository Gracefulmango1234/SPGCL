import torch

print(f"PyTorch version: {torch.__version__}")
if torch.cuda.is_available():
    print(f"CUDA is available. Version: {torch.version.cuda}")
else:
    print("CUDA is not available.")