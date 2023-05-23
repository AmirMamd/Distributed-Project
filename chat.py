import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END
from chat_network import chat_network
import pickle

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

        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, 9999))
        # self.username=username
        threading.Thread(target=self.receive_messages).start()
    #     self.receive_username()
    #
    #
    # def receive_username(self):
    #     # username = self.client_socket.recv(4096).decode()
    #     self.display_message(f"Welcome : {username}")
    def Username(self,username):
        self.client_socket.sendall(username.encode("utf-8"))
    def send_message(self):
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

if __name__ == "__main__":
    root = tk.Tk()
    # username="amir"
    client_gui = ChatClientGUI(root)
    root.mainloop()
