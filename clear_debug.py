import os

def clear_debug_logs():
    # Paths to debug logs (inside plugin directories)
    source_debug_log = r"C:\Users\vinay\Local Sites\importproducts\app\public\wp-content\plugins\woocommerce-product-import-export\debug.log"
    source_debug2_log = r"C:\Users\vinay\Local Sites\importproducts\app\public\wp-content\plugins\woocommerce-product-import-export\debug2.log"
    dest_debug_log = r"C:\Users\vinay\Local Sites\ltc\app\public\wp-content\plugins\woocommerce-product-import-export\debug.log"
    dest_debug2_log = r"C:\Users\vinay\Local Sites\ltc\app\public\wp-content\plugins\woocommerce-product-import-export\debug2.log"
    
    logs_cleared = []
    logs_not_found = []
    
    all_logs = [
        ("source debug.log", source_debug_log),
        ("source debug2.log", source_debug2_log),
        ("dest debug.log", dest_debug_log),
        ("dest debug2.log", dest_debug2_log)
    ]
    
    # Clear all logs
    for log_name, log_path in all_logs:
        if os.path.exists(log_path):
            with open(log_path, "w", encoding="utf-8") as f:
                f.write("")  # Clear the file content
            logs_cleared.append(log_name)
            print(f"✓ Cleared: {log_path}")
        else:
            logs_not_found.append(log_name)
            print(f"✗ Not found: {log_path}")
    
    # Summary
    print("\n" + "="*50)
    if logs_cleared:
        print(f"Successfully cleared {len(logs_cleared)} log(s): {', '.join(logs_cleared)}")
    if logs_not_found:
        print(f"Could not find {len(logs_not_found)} log(s): {', '.join(logs_not_found)}")
    print("="*50)

if __name__ == "__main__":
    clear_debug_logs()
