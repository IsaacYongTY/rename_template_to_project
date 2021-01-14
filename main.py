# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, uic
import os
import shutil
import sys


def get_correct_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        relative_path = '.'
        self.directory = get_correct_path(relative_path)

        uic.loadUi(f'{self.directory}/rename_template_to_project.ui', self)

        self.load_default_template_path()

        self.chooseTemplateButton.clicked.connect(self.select_directory)
        self.createFolderButton.clicked.connect(self.create_folder_and_rename)

        self.show()

    def load_default_template_path(self):
        default_path_file = self.get_correct_path(f'{self.directory}/default_directory.txt')

        if os.path.isfile(default_path_file):

            with open(default_path_file, 'r') as f:
                self.template_path = f.read().strip()
                self.templateInput.setText(self.template_path)

        else:
            self.template_path = ''

    def select_directory(self):
        new_path = QtWidgets.QFileDialog.getExistingDirectory()

        if new_path:
            self.template_path = new_path

    def create_folder_and_rename(self):

        song_title = self.projectTitleInput.text().strip()
        template_string = 'TEMPLATE'

        destination_path = f'{os.path.dirname(self.template_path)}/{song_title}'

        if os.path.isdir(destination_path):
            self.statusLabel.setText(f'Destination exist\n{destination_path}')

        else:
            shutil.copytree(self.template_path, destination_path)

            for folderName, subfolders, filenames in os.walk(destination_path):

                print(f'The current folder is {folderName}')

                for subfolder in subfolders:
                    print(f'SUBFOLDER of {folderName}: {subfolder}')

                for filename in filenames:
                    print(f'FILE INSIDE {folderName}: {filename}')

                    if template_string in filename:
                        new_filename = filename.replace(template_string, song_title)
                        print(f'{folderName}/{filename}')
                        os.rename(f'{folderName}/{filename}', f'{folderName}/{new_filename}')
                        print('Renamed successfully')

            self.statusLabel.setText(f'Project created!\n{destination_path}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
