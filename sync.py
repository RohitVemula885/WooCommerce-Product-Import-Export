import os
import shutil
import datetime

def ignore_git(dir, files):
    """Ignore .git folder and other git-related files."""
    ignore_list = []
    for f in files:
        if f in [".git", ".gitignore", ".gitattributes", "debug.log", "debug2.log"]:
            ignore_list.append(f)
    return ignore_list

def sync_plugin(source_plugin_path, dest_plugin_path):
    # Check if source exists
    if not os.path.exists(source_plugin_path):
        print(f"Source plugin path does not exist: {source_plugin_path}")
        return

    # Preserve debug logs from destination before removing
    dest_debug_log = os.path.join(dest_plugin_path, "debug.log")
    dest_debug2_log = os.path.join(dest_plugin_path, "debug2.log")
    
    dest_debug_content = ""
    dest_debug2_content = ""
    
    if os.path.exists(dest_debug_log):
        with open(dest_debug_log, "r", encoding="utf-8") as f:
            dest_debug_content = f.read()
        print("Preserved destination debug.log")
    
    if os.path.exists(dest_debug2_log):
        with open(dest_debug2_log, "r", encoding="utf-8") as f:
            dest_debug2_content = f.read()
        print("Preserved destination debug2.log")

    # Remove old destination plugin folder
    if os.path.exists(dest_plugin_path):
        print("Removing existing plugin in destination...")
        shutil.rmtree(dest_plugin_path)

    # Copy plugin folder but ignore git-related files/folders
    print("Copying plugin (excluding .git)...")
    shutil.copytree(
        source_plugin_path,
        dest_plugin_path,
        ignore=ignore_git
    )

    print("Plugin sync completed!")
    
    # Path definitions
    source_debug_log = os.path.join(source_plugin_path, "debug.log")
    source_debug2_log = os.path.join(source_plugin_path, "debug2.log")
    
    # Read source debug contents
    source_old_content = ""
    
    if os.path.exists(source_debug_log):
        with open(source_debug_log, "r", encoding="utf-8") as f:
            source_old_content = f.read()
    
    # Restore destination's debug logs
    if dest_debug_content:
        with open(dest_debug_log, "w", encoding="utf-8") as f:
            f.write(dest_debug_content)
        print("Restored destination debug.log")
    
    if dest_debug2_content:
        with open(dest_debug2_log, "w", encoding="utf-8") as f:
            f.write(dest_debug2_content)
        print("Restored destination debug2.log")
    
    # Cross-copy debug logs
    with open(source_debug2_log, "w", encoding="utf-8") as f:
        f.write(dest_debug_content)
    print(f"Copied destination's debug.log to source as debug2.log")
    
    with open(dest_debug2_log, "w", encoding="utf-8") as f:
        f.write(source_old_content)
    print(f"Copied source's debug.log to destination as debug2.log")

if __name__ == "__main__":
    # UPDATE THESE PATHS
    source_plugin = r"C:\Users\vinay\Local Sites\importproducts\app\public\wp-content\plugins\woocommerce-product-import-export"
    dest_plugin = r"C:\Users\vinay\Local Sites\ltc\app\public\wp-content\plugins\woocommerce-product-import-export"

    sync_plugin(source_plugin, dest_plugin)
