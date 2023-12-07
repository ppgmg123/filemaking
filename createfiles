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

result = createfiles(1024, 1024)
print(result)
