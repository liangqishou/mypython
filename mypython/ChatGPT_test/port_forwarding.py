import tkinter as tk
import subprocess

class PortForwardingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("端口转发应用程序")

        self.host_label = tk.Label(self.master, text="本地IP地址：")
        self.host_label.grid(row=0, column=0, padx=5, pady=5)
        self.host_entry = tk.Entry(self.master)
        self.host_entry.grid(row=0, column=1, padx=5, pady=5)

        self.local_port_label = tk.Label(self.master, text="本地端口：")
        self.local_port_label.grid(row=1, column=0, padx=5, pady=5)
        self.local_port_entry = tk.Entry(self.master)
        self.local_port_entry.grid(row=1, column=1, padx=5, pady=5)

        self.remote_host_label = tk.Label(self.master, text="远程IP地址：")
        self.remote_host_label.grid(row=2, column=0, padx=5, pady=5)
        self.remote_host_entry = tk.Entry(self.master)
        self.remote_host_entry.grid(row=2, column=1, padx=5, pady=5)

        self.remote_port_label = tk.Label(self.master, text="远程端口：")
        self.remote_port_label.grid(row=3, column=0, padx=5, pady=5)
        self.remote_port_entry = tk.Entry(self.master)
        self.remote_port_entry.grid(row=3, column=1, padx=5, pady=5)

        self.forward_button = tk.Button(self.master, text="启动转发", command=self.start_forwarding)
        self.forward_button.grid(row=4, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.master, text="停止转发", command=self.stop_forwarding)
        self.stop_button.grid(row=4, column=1, padx=5, pady=5)

    def start_forwarding(self):
        host = self.host_entry.get()
        local_port = self.local_port_entry.get()
        remote_host = self.remote_host_entry.get()
        remote_port = self.remote_port_entry.get()

        command = f"netsh interface portproxy add v4tov4 listenaddress={host} listenport={local_port} connectaddress={remote_host} connectport={remote_port}"
        subprocess.run(command, shell=True)

    def stop_forwarding(self):
        host = self.host_entry.get()
        local_port = self.local_port_entry.get()

        command = f"netsh interface portproxy delete v4tov4 listenaddress={host} listenport={local_port}"
        subprocess.run(command, shell=True)

if __name__ == '__main__':
    root = tk.Tk()
    app = PortForwardingApp(root)
    root.mainloop()
