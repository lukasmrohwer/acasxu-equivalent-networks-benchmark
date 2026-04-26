import onnx
import sys
import numpy as np

def perturb_network(onnx_path, perturbed_onnx_path, p, seed):
    with open(onnx_path, "rb") as f:
        onnx_model = onnx.load(f)

    for i in range(len(onnx_model.graph.initializer)):
        tensor = onnx.numpy_helper.to_array(onnx_model.graph.initializer[i])

        np.random.seed(seed)
        noise = np.random.normal(loc=0.0, scale=p, size=tensor.shape).astype(tensor.dtype)

        perturbed_tensor = tensor + noise

        new_tensor = onnx.numpy_helper.from_array(perturbed_tensor, name=onnx_model.graph.initializer[i].name)
        
        onnx_model.graph.initializer[i].CopyFrom(new_tensor)

    onnx.save(onnx_model, perturbed_onnx_path)

if __name__ == "__main__":
    main("onnx/original/ACASXU_run2a_1_1_batch_2000.onnx", "onnx/perturbed/ACASXU_run2a_1_1_batch_2000_perturbed.onnx", 0.001, 0)