import subprocess
import tempfile
import os

def compile_c_to_bitcode(c_code):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a temporary file for the C code in the current directory
    with tempfile.NamedTemporaryFile(delete=False, suffix='.c', dir=current_dir) as c_file:
        c_file_path = c_file.name
        c_file.write(c_code.encode())
    
    # Determine the output bitcode file path
    bitcode_file_path = c_file_path + '.bc'
    
    # Compile the C code to LLVM bitcode
    clang_command = [
        "clang", "-I", "../../include", "-emit-llvm", "-c", "-g", "-O0",
        "-Xclang", "-disable-O0-optnone", c_file_path, "-o", bitcode_file_path
    ]
    
    try:
        subprocess.run(clang_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Compilation error: {e}")
        return None
    finally:
        os.remove(c_file_path)
    
    return bitcode_file_path

c_code = """
#include <stdio.h>
int main() {
    printf("Hello, World!\\n");
    return 0;
}
"""
bitcode_file_path = compile_c_to_bitcode(c_code)
if bitcode_file_path:
    print(f"Compiled to bitcode at: {bitcode_file_path}")
else:
    print("Compilation failed.")