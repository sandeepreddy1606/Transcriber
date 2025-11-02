#!/usr/bin/env python3
"""
Diagnostic script to check GPU and PyTorch installation
"""

import sys
import torch

print("\n" + "="*70)
print("PYTORCH & GPU DIAGNOSTIC")
print("="*70 + "\n")

print("1. PYTHON INFO")
print(f"   Python Version: {sys.version}")
print(f"   Python Executable: {sys.executable}\n")

print("2. PYTORCH INFO")
print(f"   PyTorch Version: {torch.__version__}")
print(f"   PyTorch Location: {torch.__file__}\n")

print("3. CUDA INFO")
print(f"   CUDA Available: {torch.cuda.is_available()}")
print(f"   CUDA Version (in PyTorch): {torch.version.cuda}")
print(f"   CuDNN Version: {torch.backends.cudnn.version()}\n")

if torch.cuda.is_available():
    print("4. GPU INFO (FOUND!)")
    print(f"   Number of GPUs: {torch.cuda.device_count()}")
    print(f"   GPU Name: {torch.cuda.get_device_name(0)}")
    print(f"   GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f}GB")
    print(f"   Current Device: {torch.cuda.current_device()}\n")
    
    print("5. TESTING GPU")
    try:
        x = torch.randn(1000, 1000).cuda()
        y = torch.randn(1000, 1000).cuda()
        z = torch.matmul(x, y)
        print(f"   ✅ GPU WORKS! Matrix multiplication successful\n")
    except Exception as e:
        print(f"   ❌ GPU ERROR: {e}\n")
else:
    print("4. GPU INFO")
    print("   ⚠️  NO GPU DETECTED!\n")
    
    print("5. SOLUTIONS:")
    print("   a) NVIDIA GPU not installed")
    print("   b) PyTorch installed CPU-only version")
    print("   c) NVIDIA drivers not installed")
    print("   d) CUDA toolkit not installed\n")
    
    print("6. FIX: Install GPU version of PyTorch")
    print("   Run this command:")
    print("   pip install torch --index-url https://download.pytorch.org/whl/cu118\n")

print("="*70)