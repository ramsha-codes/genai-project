# Training Results Documentation

## Training Configuration
- **Model**: DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit
- **Dataset**: FreedomIntelligence/medical-o1-reasoning-sft (500 samples)
- **Training Steps**: 60
- **Batch Size**: 1
- **Gradient Accumulation**: 4 steps
- **Learning Rate**: 2e-4
- **Optimizer**: AdamW 8-bit

## Training Progress
- **Initial Loss**: 1.716500
- **Final Loss**: 1.393200 
- **Loss Reduction**: 1.716500 - 1.393200 = 0.3233
- **Training Duration**: 16 minutes and 11 seconds

## Memory Usage
- **GPU**: Google Colab T4
- **Memory Optimizations Used**:
  - 4-bit quantization
  - Gradient checkpointing
  - Small batch size with accumulation
  - FP16 precision

## Challenges Encountered
- GPU memory limitations with 8B parameter model
- Import management in Colab environment
- Reconnecting the notebook

## Solutions Applied
- Used aggressive memory management settings
- Implemented proper import sequence

## Training Success Indicators
- Training completed without out-of-memory errors
- Loss decreased consistently over training steps
- Model generated coherent responses to medical queries
- Memory usage stayed within T4 limits

### WandB Dashboard
![Dashboard](images/wandb-dashboard.png)

### Training Curves
![Training Metrics](images/training-loss-curve.png)

![Learning Rate](images/learning-rate.png)

### System Metrics
![GPU Memory Allocated](images/gpu-memory.png)

![GPU Utilized](images/gpu-utilization.png)

