# File operations with try-except
try:
    file = open("example.txt", "r")
    print("📄 File Content:")
    print(file.read())
except FileNotFoundError:
    print("❌ File not found.")
except Exception as e:
    print("❌ An error occurred:", e)
finally:
    try:
        file.close()
    except:
        pass