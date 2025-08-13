import os
import shutil
import subprocess
import tempfile
from qtpy.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox
)
from qtpy.QtCore import Qt

class GitUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exportar .py para GitHub")
        self.setMinimumWidth(500)

        layout = QVBoxLayout()

        # Seleção de pasta
        self.folder_label = QLabel("Pasta de origem:")
        layout.addWidget(self.folder_label)

        self.folder_input = QLineEdit()
        layout.addWidget(self.folder_input)

        self.folder_btn = QPushButton("Selecionar Pasta")
        self.folder_btn.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_btn)

        # Link do repositório
        self.repo_label = QLabel("Link completo do repositório GitHub:")
        layout.addWidget(self.repo_label)

        self.repo_input = QLineEdit()
        layout.addWidget(self.repo_input)

        # Token pessoal
        self.token_label = QLabel("Token pessoal do GitHub:")
        layout.addWidget(self.token_label)

        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.token_input)

        # Botão de exportar
        self.export_btn = QPushButton("Exportar para GitHub")
        self.export_btn.clicked.connect(self.export_to_github)
        layout.addWidget(self.export_btn)

        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Selecione a pasta")
        if folder:
            self.folder_input.setText(folder)

    def export_to_github(self):
        source_dir = self.folder_input.text().strip()
        repo_url = self.repo_input.text().strip()
        token = self.token_input.text().strip()

        if not source_dir or not os.path.isdir(source_dir):
            QMessageBox.warning(self, "Erro", "Selecione uma pasta válida.")
            return
        if not repo_url.startswith("https://"):
            QMessageBox.warning(self, "Erro", "Informe o link completo do repositório GitHub.")
            return
        if not token:
            QMessageBox.warning(self, "Erro", "Informe o token pessoal do GitHub.")
            return

        try:
            temp_dir = tempfile.mkdtemp()

            # Copiar apenas arquivos .py preservando estrutura
            for root, dirs, files in os.walk(source_dir):
                rel_path = os.path.relpath(root, source_dir)
                target_dir = os.path.join(temp_dir, rel_path)
                os.makedirs(target_dir, exist_ok=True)
                for file in files:
                    if file.endswith(".py"):
                        shutil.copy2(os.path.join(root, file), target_dir)

            # Inicializar git se não existir
            if not os.path.exists(os.path.join(temp_dir, ".git")):
                subprocess.run(["git", "init"], cwd=temp_dir, check=True)

            # Adicionar remote
            repo_with_token = repo_url.replace(
                "https://", f"https://{token}@"
            )
            subprocess.run(["git", "remote", "remove", "origin"], cwd=temp_dir, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "remote", "add", "origin", repo_with_token], cwd=temp_dir, check=True)

            # Commit e push
            subprocess.run(["git", "add", "."], cwd=temp_dir, check=True)
            subprocess.run(["git", "commit", "-m", "Export .py files"], cwd=temp_dir, check=True)
            subprocess.run(["git", "branch", "-M", "main"], cwd=temp_dir, check=True)
            subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=temp_dir, check=True)

            QMessageBox.information(self, "Sucesso", "Arquivos exportados para o GitHub com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {str(e)}")

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    app = QApplication([])
    window = GitUploader()
    window.show()
    app.exec()
