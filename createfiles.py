import sys
import argparse
def createfiles(files_amount, byte):
    try:
        large_file = bytes(byte)
        for i in range(files_amount):
            f = open(f'{i}', "wb")
            f.write(large_file)
        return f"Files written! Total files: {files_amount}, Total bytes: {(byte) * files_amount}"
    except Exception as e:
       print(f"Problems writing files: {e}")

def parsing():
    parser = argparse.ArgumentParser(
                    prog='File creator',
                    description='Creates a specific amount of files with specific amount of bytes.',
                    epilog='files_amount bytes')
    parser.add_argument('files_amount', help='decides how many files to create.',type=int)
    parser.add_argument('bytes', help='decides how many bytes should the file use.',type=int)
    return parser.parse_args()

if __name__ == '__main__':
    args = parsing()
    result = createfiles(args.files_amount, args.bytes)
    print(result)
