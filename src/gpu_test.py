import torch

def test_gpu():
    # Check if GPU is available
    if torch.cuda.is_available():
        print("GPU is available!")
        
        # Get GPU name
        gpu_name = torch.cuda.get_device_name(0)
        print(f"Using GPU: {gpu_name}")
        
        # Create a tensor and move it to the GPU
        tensor = torch.randn((1000, 1000))  # A random tensor
        tensor_gpu = tensor.to('cuda')     # Move tensor to GPU
        
        # Perform a simple operation on the GPU
        result = tensor_gpu * 2
        print("Tensor operation on GPU successful.")
    else:
        print("GPU is not available!")

if __name__ == "__main__":
    test_gpu()