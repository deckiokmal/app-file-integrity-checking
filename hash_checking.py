import hashlib


def hash_generator(file_path):
    hash = input("Masukkan hash: ")
    with open(file_path, "rb") as file:
        content = file.read()

        # md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()

        # md5.update(content)
        sha1.update(content)
        sha256.update(content)

    # md5_result = "{}: {}".format(md5.name, md5.hexdigest())
    sha1_result = "{}".format(sha1.hexdigest())
    sha256_result = "{}".format(sha256.hexdigest())

    if sha1_result == hash:
        return f"hash sha1 match, your file is secure. {sha1_result}"
    elif sha256_result == hash:
        return f"hash sha256 match, your file is secure. {sha256_result}"
    else:
        return (
            f"your file have been modified!. result is: \n {sha1_result, sha256_result}"
        )


file_path = r"D:\file_integrity_checking\my_file.txt"
print(hash_generator(file_path))
