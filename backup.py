import json
import os

class BackupManager:
    def __init__(self, backup_dir="backups"):
        self.backup_dir = backup_dir
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def create_backup(self, data: dict, filename: str):
        """Создание резервной копии (например, пространственных векторов)."""
        filepath = os.path.join(self.backup_dir, f"{filename}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Резервная копия создана: {filepath}")

    def restore_backup(self, filename: str) -> dict:
        """Восстановление данных из резервной копии."""
        filepath = os.path.join(self.backup_dir, f"{filename}.json")
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Бэкап {filename} не найден!")
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно восстановлены из {filepath}")
        return data
