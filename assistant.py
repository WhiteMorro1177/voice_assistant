import recognizer
import command_executor

def main():    
    text_open = "григорий открой браузер"

    r = recognizer.Recognizer()
    r_open_cmd = r.recognize(text_open, "cmd")
    print(f"from recognizer: {r_open_cmd}")

    ex = command_executor.CommandExecutor()
    ex.execute(r_open_cmd)



if __name__ == "__main__": main()