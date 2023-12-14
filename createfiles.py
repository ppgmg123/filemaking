import argparse
import os

def createfiles(files_amount, byte, megabytes, path):
    large_file = 0
    
    if path == " ":
        path = os.path.abspath(os.getcwd())
    
    if megabytes == True:
        large_file = bytearray(byte * 1024 * 1024)
    else:
        large_file = bytes(byte)
        
    for i in range(1 , files_amount+1):
        f = open(f'{os.path.join(path, f"{i}")}', "wb")
        f.write(large_file)
        f.close()
            
    return f"Files written! Total files: {files_amount}, Total bytes: {len(large_file) * files_amount}"

def parsing():
    parser = argparse.ArgumentParser(
                    prog='File creator',
                    description='Creates a specific amount of files with specific amount of bytes.',
                    epilog='files_amount bytes')
    parser.add_argument('files_amount', help='decides how many files to create.',type=int)
    parser.add_argument('bytes', help='decides how many bytes should the file use.',type=int)
    parser.add_argument('-m','--megabytes',help="decides if the input should be counted in megabytes instead of bytes.",
                    action='store_true')
    parser.add_argument('path',nargs='?', help='decides the path of the files. The default path is the path of this file.',default="")
    return parser.parse_args()

if __name__ == '__main__':
    args = parsing()
    result = createfiles(args.files_amount, args.bytes, args.megabytes, args.path)
    print(result)
