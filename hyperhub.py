import os
import subprocess
import logging
from datetime import datetime

class HyperHub:
    def __init__(self, log_file='hyperhub.log'):
        self.logger = self._setup_logger(log_file)
        self.patches_dir = 'patches'

    def _setup_logger(self, log_file):
        logger = logging.getLogger('HyperHub')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def discover_patches(self):
        self.logger.info("Discovering patches...")
        try:
            patches = [f for f in os.listdir(self.patches_dir) if f.endswith('.msu')]
            self.logger.info(f"Found patches: {patches}")
            return patches
        except Exception as e:
            self.logger.error(f"Error discovering patches: {e}")
            return []

    def apply_patch(self, patch_file):
        self.logger.info(f"Applying patch: {patch_file}")
        patch_path = os.path.join(self.patches_dir, patch_file)
        try:
            subprocess.run(['wusa.exe', patch_path, '/quiet', '/norestart'], check=True)
            self.logger.info(f"Successfully applied patch: {patch_file}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to apply patch {patch_file}: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error applying patch {patch_file}: {e}")

    def apply_all_patches(self):
        patches = self.discover_patches()
        for patch in patches:
            self.apply_patch(patch)

if __name__ == "__main__":
    hub = HyperHub()
    hub.apply_all_patches()