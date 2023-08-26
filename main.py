from googletrans import Translator
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import urllib
from flag import Flag

# init the Google API translator
translator = Translator()

# detect a language
# detection = translator.detect("привет, братан, ты такой крутой и профи")
# print("Language code:", detection.lang)
# print("Confidence:", detection.confidence)

# translation = translator.translate("привет, братан, ты такой крутой и профи", "en", detection.lang)
# print(translation.text)
  
class requestHandeler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type', 'text/html')
    self.end_headers()
    self.wfile.write(b"im on")

  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    body = self.rfile.read(content_length)
    body = body.decode("utf_8")
    bodylines = body.splitlines()
    try:
        line2 = bodylines[1]
    except IndexError:
        self.send_response(400)
        self.end_headers()
        return
    # print(body)
    # body = body.decode('string_escape')
    
    if body.isspace() or len(body) == 0:
        self.send_response(400)
        self.end_headers()
    else:
        line1 = bodylines[0]
        detection = translator.detect(line1)
        translation = ""
        if type(detection.confidence) == list:
            for i in detection.confidence:
                if i >= .5:
                    self.send_response(200)
                    self.end_headers()
                    translation = translator.translate(line1, "en", detection.lang[detection.confidence.index(i)])
                    response = BytesIO()
                    response.write(b'')
                    response.write(bytes(detection.lang[detection.confidence.index(i)], 'utf-8'))
                    response.write(b'\n')
                    response.write(bytes(translation.text, 'utf-8'))
                    if detection.lang[detection.confidence.index(i)] == "hi":
                        print(line2+": "+Flag.flag("in")+' -> '+"🇪🇳 - "+translation.text)
                        self.wfile.write(response.getvalue())
                        return
                    if detection.lang[detection.confidence.index(i)] == "bn":
                        print(line2+": "+Flag.flag("bd")+' -> '+"🇪🇳 - "+translation.text)
                        self.wfile.write(response.getvalue())
                        return
                    if detection.lang[detection.confidence.index(i)].lower().endswith("cn"):
                        print(line2+": "+Flag.flag("cn")+' -> '+"🇪🇳 - "+translation.text)
                        self.wfile.write(response.getvalue())
                        return
                    if detection.lang[detection.confidence.index(i)] == "en":
                        print(line2+": "+"🇪🇳"+' -> '+"🇪🇳 - "+translation.text)
                        self.wfile.write(response.getvalue())
                        return
                    else:
                        print(line2+": "+Flag.flag(detection.lang[detection.confidence.index(i)])+' -> '+"🇬🇧 - "+translation.text)
                        self.wfile.write(response.getvalue())
                        return
        elif detection.confidence == None:
            self.send_response(200)
            self.end_headers()
            translation = translator.translate(line1, "en", detection.lang)
            response = BytesIO()
            response.write(b'')
            response.write(bytes(detection.lang, 'utf-8'))
            response.write(b'\n')
            response.write(bytes(translation.text, 'utf-8'))
            if detection.lang == "hi":
                print(line2+": "+Flag.flag("in")+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            if detection.lang == "bn":
                print(line2+": "+Flag.flag("bd")+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
            if detection.lang.lower().endswith("cn"):
                print(line2+": "+'🇨🇳'+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            if detection.lang == "en":
                print(line2+": "+'🇪🇳'+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            else:
                print(line2+": "+Flag.flag(detection.lang)+' -> '+"🇬🇧 - "+translation.text)
                self.wfile.write(response.getvalue())
        elif detection.confidence >= .5:
            self.send_response(200)
            self.end_headers()
            translation = translator.translate(line1, "en", detection.lang)
            response = BytesIO()
            response.write(b'')
            response.write(bytes(detection.lang, 'utf-8'))
            response.write(b'\n')
            response.write(bytes(translation.text, 'utf-8'))
            if detection.lang == "hi":
                print(line2+": "+Flag.flag("in")+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            if detection.lang == "bn":
                print(line2+": "+Flag.flag("bd")+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            if detection.lang.lower().endswith("cn"):
                print(line2+": "+'🇨🇳'+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            if detection.lang == "en":
                print(line2+": "+"🇪🇳"+' -> '+"🇪🇳 - "+translation.text)
                self.wfile.write(response.getvalue())
                return
            else:
                print(line2+": "+Flag.flag(detection.lang)+' -> '+"🇬🇧 - "+translation.text)
                self.wfile.write(response.getvalue())
        else:
            self.send_response(400)
            self.end_headers()
    # print(detection.lang)
    # print(detection.confidence)
  
  def log_message(self, format, *args):
    return
def main():
  PORT = 9800
  server_address = ('0.0.0.0', PORT)
  server = HTTPServer(server_address, requestHandeler)
  print("Server running on port 9800. I am not gonna tell with variabl bc you alr kno what it is.")
  server.serve_forever()

main()

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("500x400")
# app.grid_columnconfigure(0, weight=1)
# app.grid_rowconfigure((0, 1), weight=1)

# def button_function():
#   text = textbox.get("0.0", "end")
#   print("button pressed", text)

# # Use CTkButton instead of tkinter Button
# textbox = customtkinter.CTkTextbox(app, 1, 10)
# textbox.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# class MyCheckboxFrame(customtkinter.CTkScrollableFrame):
#     def __init__(self, master, title, values):
#         super().__init__(master, label_text=title)
#         self.grid_columnconfigure(0, weight=1)
#         self.values = values
#         self.labels = []

#         for i, value in enumerate(self.values):
#             label = customtkinter.CTkLabel(self, text=value, fg_color="transparent", font=customtkinter.CTkFont(size=12))
#             label.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.labels.append(label)

# class App(customtkinter.CTk):
#   def __init__(self):
#         super().__init__()

#         self.title("my app")
#         self.geometry("500x400")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
#         self.scrollable_checkbox_frame = MyCheckboxFrame(self, title="", values=values)
#         self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

#         self.textbox = customtkinter.CTkTextbox(self, 1, 10)
#         self.textbox.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

# app = App()
# app.mainloop()

# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)