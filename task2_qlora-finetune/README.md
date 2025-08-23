# Medical QLoRA Fine-tuning Project

## Overview
This project demonstrates fine-tuning a large language model for medical applications using QLoRA (Quantized Low-Rank Adaptation) technique with Unsloth optimization framework.

## Key Achievements
- Successfully fine-tuned 8B parameter model on consumer GPU
- Implemented memory-efficient training with 4-bit quantization
- Achieved improved medical reasoning capabilities
- Demonstrated QLoRA technique on specialized medical dataset

## Technical Implementation

### Model Architecture
- **Base Model**: unsloth/DeepSeek-R1-Distill-Llama-8B
- **Quantization**: 4-bit with BitsAndBytes
- **Adaptation Method**: LoRA with rank 16
- **Target Modules**: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

### Dataset
- **Source**: FreedomIntelligence/medical-o1-reasoning-SFT
- **Language**: English
- **Training Samples**: 500
- **Format**: Question-Complex_CoT-Response triplets

### Training Configuration
- **Hardware**: Google Colab T4 GPU
- **Batch Size**: 2 per device × 4 gradient accumulation steps
- **Learning Rate**: 2e-4
- **Training Steps**: 60
- **Memory Optimization**: Gradient checkpointing, 4-bit quantization, FP16

## Results
- Training successfully completed without memory errors
- Model demonstrates improved medical reasoning
- Responses show better accuracy and formatting consistency
- Memory usage stayed within T4 GPU limits

## How to Run
1. Open notebook in Google Colab
2. Enable GPU runtime (T4 recommended)
3. Run cells sequentially
4. Authenticate with Hugging Face and W&B tokens
5. Monitor training progress

## Key Learning Outcomes
- Practical experience with QLoRA fine-tuning workflow
- Understanding of memory-efficient training techniques
- Hands-on work with medical NLP datasets
- Experience with Unsloth optimization framework

## Technical Challenges Overcome
- GPU memory limitations with 8B parameter model
- Dataset formatting and column name handling
- Import management in Colab environment
- Balancing training efficiency with model quality