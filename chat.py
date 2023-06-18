import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END


class ChatClientGUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Chat Room")
        self.chat_room = "Chat Room"
        self.server_address = "127.0.0.1"  # Change to the server's IP address


        self.chat_box = scrolledtext.ScrolledText(self.root, state="disabled")
        self.chat_box.pack()

        self.message_entry = Entry(self.root)
        self.message_entry.pack()
        self.message_entry.bind("<Return>", self.send_message)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, 6666))
        threading.Thread(target=self.receive_messages).start()


        self.root.protocol("WM_DELETE_WINDOW", self.handle_quit)
        # Create a button to send messages
        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

      # https://github.com/AmirMamd/Distributed-Project/pull/7/conflict?name=ChatServer.py&ancestor_oid=a2a6169de9ec9f07ac0c803f28e9561b9bd29d2d&base_oid=c2b7bd22bf24f9bd13f840b92aabd6da55c18a73&head_oid=83d8c93359dd83584066a9923461b4f3f9155328  # Create a client socket and connect to the server
      #   self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #   self.client_socket.connect((self.server_address, 7777))

    def Username(self, username):
        self.client_socket.sendall(username.encode("utf-8"))

    def send_message(self, event=None):
        message = self.message_entry.get()
        self.client_socket.sendall(message.encode("utf-8"))
        self.message_entry.delete(0, END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                self.display_message(message)
            except ConnectionResetError:
                self.client_socket.close()
                break

    def display_message(self, message):
        self.chat_box.config(state="normal")
        self.chat_box.insert(END, message + "\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see(END)

    def close_connection(self):
        self.client_socket.close()

    def handle_quit(self):
        self.close_connection()
        self.root.quit()
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     client_gui = ChatClientGUI(root)
#     root.mainloop()