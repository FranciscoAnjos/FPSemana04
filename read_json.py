import json

def read_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            c = json.load(f)
        print(c)
    except Exception as e:
        print("Ocorreu um erro!")
    finally:
        print("Processo concluído!")

if __name__ == "__main__":
    p = input()
    read_json(p)