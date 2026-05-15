# ACAS Xu Equivalent Networks Benchmark

This repository contains the ACAS Xu equivalent networks benchmark for **VNNCOMP 2026** (Verification of Neural Networks Competition).

## Overview
This benchmark evaluates the verification of monotonicity specifications using equivalent network formulations of the ACAS Xu models. It generates VNN-LIB 2.0 compliant specifications.

## Prerequisites
Ensure you have the environment set up. You can install any required dependencies via:
```bash
pip install -r requirements.txt
```

## Usage Instructions

To generate the VNN-LIB properties and the `instances.csv` file required for VNNCOMP, use the provided `generate_properties.py` script. The script requires a numeric random seed as an argument.

```bash
python generate_properties.py <random_seed>
```

### Example
```bash
python generate_properties.py 42
```

This will:
1. Generate `vnnlib/instance_0.vnnlib` using the VNN-LIB 2.0 format template.
2. Select random ONNX models from the `onnx/original/` directory.
3. Produce the `instances.csv` file mapping the ONNX models to the generated VNN-LIB specification, along with a per-instance verification timeout of 100 seconds.

## Directory Structure
- `generate_properties.py`: Main script to generate properties and the `instances.csv` file.
- `python_scripts/create_specifications.py`: Contains the template logic for the VNN-LIB 2.0 file, including the neural network declarations and input/output constraints.
- `onnx/`: Directory for the original ONNX model files representing the ACAS Xu networks.
- `vnnlib/`: Directory where the generated `.vnnlib` specifications are saved.
- `instances.csv`: The output file mapping the verification problems for the competition.