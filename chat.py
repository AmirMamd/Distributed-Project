import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END

class ChatClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Room")
        self.chat_room = "Chat Room"
        self.server_address = "3.133.154.143"  # Change to the server's IP address

        # Create a scrolled text widget to display the chat messages
        self.chat_box = scrolledtext.ScrolledText(self.root, state="disabled")
        self.chat_box.pack()

        # Create an entry widget for typing messages
        self.message_entry = Entry(self.root)
        self.message_entry.pack()

        # Create a button to send messages
        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Create a client socket and connect to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, 7777))

        # Prompt the user to enter a username and send it to the server
        username = input("Enter your username: ")
        self.client_socket.sendall(username.encode("utf-8"))

        # Receive the welcome message from the server and display it
        welcome_message = self.client_socket.recv(1024).decode("utf-8")
        self.display_message(welcome_message)

        # Start a thread to receive messages from the server
        threading.Thread(target=self.receive_messages).start()

    def send_message(self):
        # Get the message from the entry widget and send it to the server
        message = self.message_entry.get()
        self.client_socket.sendall(message.encode("utf-8"))

        # Clear the entry widget after sending the message
        self.message_entry.delete(0, END)

    def receive_messages(self):
        while True:
            try:
                # Receive messages from the server and display them
                message = self.client_socket.recv(1024).decode("utf-8")
                self.display_message(message)
            except ConnectionResetError:
                # If a connection reset error occurs, close the socket and break the loop
                self.client_socket.close()
                break

    def display_message(self, message):
        # Enable the chat box, insert the message, and disable it again
        self.chat_box.config(state="normal")
        self.chat_box.insert(END, message + "\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see(END)

# Create a Tkinter root window
root = tk.Tk()

# Create an instance of the ChatClientGUI class
client_gui = ChatClientGUI(root)

# Start the Tkinter event loop
root.mainloop()
