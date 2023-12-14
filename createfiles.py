import sys
import argparse
def createfiles(files_amount, bytes):
    try:
        large_file = bytearray(bytes * 1024 * 1024)
        for i in range(files_amount):
           f = open(f'{i}', "wb")
           f.write(large_file)
        return "Files written!"
    except Exception as e:
        return f"Problems writing files: {str(e)}"

def parsing():
    parser = argparse.ArgumentParser(
                    prog='Create Files',
                    description='Create files',
                    epilog='createfiles.py files_amount bytes')
    parser.add_argument('files_amount', help='decides how many files to create.', type=amount)
    parser.add_argument('bytes', help='decides how many bytes should the file use.', type=bytes)
    return parser.parse_args()
    
def totallyrandom():
    for arg in sys.argv:
        print(arg) 
        
if __name__ == '__main__':
    totallyrandom()
    args = parsing()
    result = createfiles(args.files_amount, args.bytes)
    print(result)
