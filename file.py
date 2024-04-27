from pathlib import Path

message = "Hello world!"
print(message.encode())  # UTF-8
print(message.encode("utf-16"))
print(message.encode("cp1251"))
print(b"\xcf\xf0\xe8\xe2\xe5\xf2 \xec\xe8\xf0!".decode("cp1251"))
folder = Path("Test")

#  Save binary
with open(folder / "utf-8.txt", "wb") as f:
    f.write(message.encode())
