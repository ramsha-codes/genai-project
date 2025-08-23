# Training Results Documentation

## Training Configuration
- **Model**: DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit
- **Dataset**: FreedomIntelligence/medical-o1-reasoning-sft (500 samples)
- **Training Steps**: 60
- **Batch Size**: 2 per device 
- **Gradient Accumulation**: 4 steps
- **Learning Rate**: 2e-4
- **Optimizer**: AdamW 8-bit

## Training Progress
- **Initial Loss**: 2.150300
- **Final Loss**: 1.473100
- **Loss Reduction**: 2.150300 - 1.473100 = 0.6772
- **Training Duration**: 15 minutes and 14 seconds

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


