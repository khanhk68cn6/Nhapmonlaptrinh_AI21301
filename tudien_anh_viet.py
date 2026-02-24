# Bài 1: Chương trình từ điển Anh - Việt đơn giản

# Kho từ vựng định nghĩa sẵn
dictionary = {
    "hello": "xin chào",
    "world": "thế giới",
    "computer": "máy tính",
    "language": "ngôn ngữ",
    "program": "chương trình",
    "dictionary": "từ điển",
    "simple": "đơn giản",
    "input": "đầu vào",
    "output": "đầu ra",
    "exit": "thoát"
}

def dictionaryy():
    print("Chào mừng bạn đến với Từ điển Anh - Việt!")
    print("Nhập một từ tiếng Anh để tra cứu nghĩa tiếng Việt.")
    print("Nhập 'exit' để thoát chương trình.")

    while True:
        word = input("Nhập từ: ").strip().lower()
        if word == "exit":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        elif word in dictionary:
            print(f"Nghĩa của '{word}' là: {dictionary[word]}")
        else:
            print(f"Không tìm thấy từ '{word}' trong từ điển.")

if __name__ == "__main__":
    dictionaryy()
