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

    def _initial_bash_cmds(self):
        """Upgrade apt, install deps, and remove dumb folders"""

        cmds = ["sudo apt-get update",
                "sudo apt-get upgrade",
                "sudo apt-get install vim",
                "sudo apt-get install git",
                "sudo apt-get install python3-venv",
                "sudo apt-get install curl",
                "sudo apt-get install flake8",
                "sudo apt-get install python3-pip",
                "rm -rf Music Pictures Public Templates Videos",
                ]
        self._run_cmds(cmds)

    def _modify_bashrc(self):
        with open("~/.bashrc", "r") as f:
            lines = f.readlines()
        with open("~/.bashrc", "w") as f:
            for line in lines:
                if "HISTSIZE" in line:
                    f.write("HISTSIZE=100000\n")
                elif "HISTFILESIZE" in line:
                    f.write("HISTFILESIZE=2000000\n")
                else:
                    f.write(line)
        self._run_cmds(["source ~/.bashrc"])

    def _install_chrome(self):
        """Installs google chrome"""

        cmds = ["wget https://dl.google.com/linux/direct/"
                "google-chrome-stable_current_amd64.deb",
                "sudo apt install ./google-chrome-stable_current_amd64.deb",
                "rm ./google-chrome-stable_current_amd64.deb"]

        # Alter favorites bar and add chrome to it
        # https://arcanecode.com/2019/04/17/
        # setting-your-ubuntu-18-10-favorites-bar-in-a-script/
        pin_cmd = 'gsettings set org.gnome.shell favorit-apps "'
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
        with open(path, "w") as f:
            # Comments out cdrom line
            f.write("#")
            for line in lines:
                f.write(lin)

    def _install_flake8(self):
        cmds = ["mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso "
                "~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim",
                "pip3 install flake8"]
        self._run_cmds(cmds)

    def _manual_tasks(self):
        """Tasks that must be done manually"""

        for task in ["Start google chrome and sync to your acct",
                     "Set scroll speed and mouse speed as high as possible",
                     "Download .ssh and .vimrc (later fix this)"]
        cmds = ["chmod -R 400 .ssh/",
                "eval `ssh-agent`",

    def _run_cmds(self, cmds):
        assert isinstance(cmds, list)
        for cmd in cmds:
            check_call(cmd, shell=True)
