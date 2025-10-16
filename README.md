# macOS External Drive Formatter

[![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)](https://www.apple.com/macos/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.7-blue)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A minimal, safe, and interactive Python utility that lists and formats external drives on macOS using the native `diskutil` command.

Overview
- Lists connected disks and prompts the user to choose one for formatting.
- Supports ExFAT (recommended) and FAT32.
- Uses macOS’ built-in `diskutil` for reliable disk operations.
- Includes confirmation prompts to reduce risk of accidental data loss.

Requirements
- macOS
- Python 3.7 or later
- Administrator privileges (required to run `diskutil` erase operations)

Quick start
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/macos-drive-formatter.git
   cd macos-drive-formatter
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Run the script:
   ```bash
   python3 format_external_drive.py
   ```

Usage summary
1. The script runs `diskutil list` to display available disks.
2. Enter the disk identifier (for example: `disk4`).
3. Confirm the selected disk (explicit `y` required).
4. Choose the filesystem format:
   - 1 → ExFAT (recommended: cross-platform)
   - 2 → FAT32 (legacy compatibility)
5. Provide an optional volume name (defaults to `MyUSB`).
6. Confirm the final destructive action before the script invokes `diskutil eraseDisk`.

Example session
=== macOS External Drive Formatter ===

🔍 Listing available disks...

/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *30.9 GB    disk4
   1:                      Linux                         28.2 GB     disk4s3

Enter the disk identifier (e.g. disk4): disk4  
⚠️  You chose /dev/disk4. Continue? (y/n): y

Choose the filesystem format:  
1. ExFAT (recommended)  
2. FAT32 (for legacy systems)  
Enter your choice (1 or 2): 1

Enter a name for the new volume (e.g. MyUSB): BackupDrive  
This will ERASE all data on the disk. Proceed? (y/n): y

✅ Disk /dev/disk4 formatted successfully as ExFAT (BackupDrive)

How it works
The script delegates formatting to `diskutil`:

diskutil eraseDisk ExFAT MyUSB GPT /dev/disk4

This leverages macOS's native disk management for compatibility and reliability.

Safety & disclaimers
- This tool will irreversibly erase data on the selected disk.
- Double-check the disk identifier before confirming.
- The author is not responsible for data loss caused by misuse.

Development & contributions
- Contributions and improvements are welcome. Open an issue or pull request with suggested changes.
- Future enhancements may include additional filesystem support (APFS, HFS+), a GUI, and progress reporting.

Author
Dabwitso Mweemba — Co-founder & Lead Developer at Code Savanna  
GitHub • LinkedIn

License
This project is released under the MIT License. See the LICENSE file for details.
