import subprocess

def list_disks():
    print("🔍 Listing available disks...\n")
    subprocess.run(["diskutil", "list"])

def get_disk_choice():
    disk = input("\nEnter the disk identifier (e.g. disk4): ").strip()
    confirm = input(f"⚠️  You chose /dev/{disk}. Continue? (y/n): ").lower()
    if confirm != "y":
        print("❌ Operation cancelled.")
        exit(0)
    return disk

def get_format_choice():
    print("\nChoose the filesystem format:")
    print("1. ExFAT (recommended, compatible with macOS/Windows/Linux)")
    print("2. FAT32 (for legacy systems)")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice == "1":
        return ("ExFAT", "GPT")
    elif choice == "2":
        return ("FAT32", "MBRFormat")
    else:
        print("❌ Invalid choice. Exiting.")
        exit(1)

def format_disk(disk, fs_type, partition_scheme):
    label = input("\nEnter a name for the new volume (e.g. MyUSB): ").strip() or "MyUSB"
    cmd = ["diskutil", "eraseDisk", fs_type, label, partition_scheme, f"/dev/{disk}"]
    
    print(f"\n⚙️  Running: {' '.join(cmd)}")
    confirm = input("This will ERASE all data on the disk. Proceed? (y/n): ").lower()
    if confirm != "y":
        print("❌ Cancelled.")
        exit(0)

    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Disk /dev/{disk} formatted successfully as {fs_type} ({label})")
    except subprocess.CalledProcessError:
        print("\n❌ Failed to format the disk. Please check permissions or try again.")

def main():
    print("=== macOS External Drive Formatter ===\n")
    list_disks()
    disk = get_disk_choice()
    fs_type, partition_scheme = get_format_choice()
    format_disk(disk, fs_type, partition_scheme)

if __name__ == "__main__":
    main()