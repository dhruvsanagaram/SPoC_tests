import argparse
import subprocess
import tempfile
import os

# Define the code snippets
cpp_codes = {
    '1': """
#include <iostream>
#include <vector>

using namespace std;
int main() {
    int n;
    cin >> n;
    int cur = 1, cnt = 0;
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (x == cur) {
            cnt++;
            cur++;
        } else {
            ans.push_back(cnt);
            cnt = 1;
            cur = 2;
        }
        if (i == n - 1) { ans.push_back(cnt); }
    }
    cout << (int)ans.size() << endl;
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i > 0) cout << " ";
        cout << ans[i];
    }
    cout << endl;
    return 0;
}
""",
    'simple_io': """
#include <iostream>
using namespace std;
int main() {
    int number;
    cin >> number;
    cout << "You entered: " << number << endl;
    return 0;
}
"""
}

def compile_to_bitcode(cpp_code, output_suffix):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=output_suffix, dir=current_dir) as cpp_file:
        cpp_file_path = cpp_file.name
        cpp_file.write(cpp_code.encode())
    
    bitcode_file_path = cpp_file_path + '.bc'
    
    clang_command = [
        "clang", "-I", "../../include", "-emit-llvm", "-c", "-g", "-O0",
        "-Xclang", "-disable-O0-optnone", cpp_file_path, "-o", bitcode_file_path
    ]
    
    try:
        subprocess.run(clang_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Compilation error: {e}")
        return None
    finally:
        os.remove(cpp_file_path)
    
    return bitcode_file_path

def main():
    parser = argparse.ArgumentParser(description="Compile C++ code to LLVM bitcode based on command-line flag.")
    parser.add_argument('-c', '--code', type=str, choices=['1', 'simple_io'], default='1',
                        help='Choose the code snippet to compile.')
    args = parser.parse_args()

    cpp_code = cpp_codes[args.code]
    bitcode_file_path = compile_to_bitcode(cpp_code, '.cpp')
    if bitcode_file_path:
        print(f"Compiled to bitcode at: {bitcode_file_path}")
    else:
        print("Compilation failed.")

if __name__ == "__main__":
    main()
