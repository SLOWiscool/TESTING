import subprocess
import sys

# Path to your qcow2 file
qcow2_file = "win10.qcow2"
new_size = "20G"  # Example: resize to 20GB

# Step 1: Make sure qemu-utils is installed
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "-y", "qemu-utils"])

# Step 2: Resize the qcow2
subprocess.run(["qemu-img", "resize", qcow2_file, new_size])

print(f"{qcow2_file} resized to {new_size}")
