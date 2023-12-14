import sys
def createfiles(files_amount, bytes):
    try:
        # Create a large file of 1 GB
        large_file = bytearray(bytes * bytes * bytes)  # 1 GB
        for i in range(files_amount):
           f = open(f'{i}', "wb")
           f.write(large_file)
        return "Files written!"
    except Exception as e:
        return f"Problems writing files: {str(e)}"

if __name__ == '__main__':
    if len(sys.argv) > 3:
        result = createfiles(sys.argv[1], sys.argv[2])
        print(result)
else:
    print ('Usage:\n')
		print ('createfiles.py files_amount bytes')
		exit()
