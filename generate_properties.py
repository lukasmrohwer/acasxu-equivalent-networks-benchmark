import csv
import random
import sys

from python_scripts.create_specifications import vnnlib_template_2

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_properties.py <random_seed>")
        sys.exit(1)
        
    try:
        seed = int(sys.argv[1])
    except ValueError:
        print("Error: The random seed must be a numeric integer.")
        sys.exit(1)

    random.seed(seed)

    # create VNN-LIB 2.0 files given the following:
    P = 0.001               # size of the input pertubation
    EPS = 0.05              # size of the output distance
    VNN_COMP_TIMEOUT = 100  # per-instance verification timeout
    num_instances = 10

    i = 0
    instance_data = []
    lines = vnnlib_template_2()
    for ix in range(num_instances):

        vnnlib_filename = f"./vnnlib/instance_{ix}.vnnlib"
        with open(vnnlib_filename, "w") as f:
            f.writelines(line + "\n" for line in lines)

        i = random.randint(1, 5)
        j = random.randint(1, 9)

        ONNX_MODEL_PATH = f"onnx/original/ACASXU_run2a_{i}_{j}_batch_2000.onnx"

        instance = [[("f", ONNX_MODEL_PATH),("g", ONNX_MODEL_PATH)], vnnlib_filename, VNN_COMP_TIMEOUT]
        instance_data.append(instance)

    # save the ONNX/VNN-LIB instance pairs in the required CSV
    with open(f"instances.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(instance_data)

if __name__ == "__main__":
    main()