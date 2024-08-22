# Default python packages
import logging
import os
from subprocess import check_call

class Installer:
    """Class that performs functions for login"""

    def run(self):
        self._initial_bash_cmds()
        self._modify_bashrc()
        self._install_chrome()
        self._modify_sources()
        self._install_flake8()
        self._manual_tasks()
        input("Add pypy https://askubuntu.com/a/1012356/785421")
        """change installer to use chmod -R 700 ~/.ssh
        sudo ssh-agent bash
        ssh-add /home/anon/.ssh/id_rsa (then github_rsa, pwod is: this is convenient"""
        # Must use the below to configure the wifi properly...
        # https://askubuntu.com/a/1180403/785421
        # https://askubuntu.com/a/1077559/785421
        input("See comments above to fix wifi")
        # https://medium.com/@ahmaddynugroho/swap-caps-lock-and-escape-in-ubuntu-19-10-and-use-esc-easily-in-vim-vs-code-1d3d68f18764
        input("Install gnome-tweaks to swap escape key")
        input("Install hydrapaper using flatpack (look this up) and put vim shortcuts on top left")

    def _initial_bash_cmds(self):
        """Upgrade apt, install deps, and remove dumb folders"""

        cmds = ["sudo apt-get -y update",
                "sudo apt-get -y upgrade",
                "sudo apt-get -y install vim",
                "sudo apt-get -y install git",
                "sudo apt-get -y install python3-venv",
                "sudo apt-get -y install curl",
                "sudo apt-get -y install flake8",
                "sudo apt-get -y install python3-pip",
                "sudo apt-get -y install tmux",
                "rm -rf ~/Music ~/Pictures ~/Public ~/Templates ~/Videos ~/Documents",
                "git config --global user.email 'jfuruness@gmail.com'",
                "git config --global user.name 'Justin Furuness'",
                ]
        self._run_cmds(cmds)

    def _modify_bashrc(self):
        with open(os.path.expanduser("~/.bashrc"), "r") as f:
            lines = f.readlines()
        with open(os.path.expanduser("~/.bashrc"), "w") as f:
            for line in lines:
                if "HISTSIZE" in line:
                    f.write("HISTSIZE=100000\n")
                elif "HISTFILESIZE" in line:
                    f.write("HISTFILESIZE=2000000\n")
                else:
                    f.write(line)
        # Cannot appear to source from within a shell
        # self._run_cmds(["source ~/.bashrc"])

    def _install_chrome(self):
        """Installs google chrome"""

        cmds = ["wget https://dl.google.com/linux/direct/"
                "google-chrome-stable_current_amd64.deb",
                "sudo apt install ./google-chrome-stable_current_amd64.deb",
                "rm ./google-chrome-stable_current_amd64.deb"]

        # Alter favorites bar and add chrome to it
        # https://arcanecode.com/2019/04/17/
        # setting-your-ubuntu-18-10-favorites-bar-in-a-script/
        pin_cmd = 'gsettings set org.gnome.shell favorite-apps "'
        pin_cmd += ("['google-chrome.desktop', 'org.gnome.Nautilus.desktop',"
                    "'libreoffice-writer.desktop', 'org.gnome.Terminal.desktop']")
        pin_cmd += '"'
        cmds.append(pin_cmd)

        self._run_cmds(cmds)

    def _install_chrome_exts(self):
        """Installs lastpass"""

        _dir = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(_dir, "add_chrome_ext.sh")
        self._run_cmds([f"./{path}"])

    def _modify_sources(self):
        """idk what this was for anymore"""

        path = "/etc/apt/sources.list"
        with open(path, "r") as f:
            lines = f.readlines()
        permissions_path = "/tmp/sources.list"
        with open(permissions_path, "w") as f:
            # Comments out cdrom line
            f.write("#")
            for line in lines:
                f.write(line)
        self._run_cmds([f"sudo cp {permissions_path} {path}"])

    def _install_flake8(self):
        cmds = ["mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso "
                "~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim",
                "pip3 install flake8 --break-system-packages"]
        self._run_cmds(cmds)

    def _manual_tasks(self):
        """Tasks that must be done manually"""

        for task in ["Start google chrome and sync to your acct",
                     "Set scroll speed and mouse speed as high as possible",
                     "Download .ssh and .vimrc (later fix this)",
                     "Download displaylink manager"]:
            input(task)
        cmds = ["sudo chmod -R 700 ~/.ssh/",
                "eval `ssh-agent`",
                "ssh-add"]
        self._run_cmds(cmds)

    def _run_cmds(self, cmds):
        assert isinstance(cmds, list)
        for cmd in cmds:
            print(f"Running: {cmd}")
            check_call(cmd, shell=True)
