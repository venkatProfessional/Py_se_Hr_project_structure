import pandas as pd
import os
import time

def read_excel(file_path):
    """Read data from an Excel file into a DataFrame."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Excel file not found at {file_path}")
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error reading Excel file: {str(e)}")

def write_excel(df, output_path):
    """Write DataFrame to an Excel file with permission handling."""
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            df.to_excel(output_path, index=False)
            print(f"📊 Final Results saved to {output_path}")
            return
        except PermissionError:
            if attempt < max_attempts - 1:
                print(f"⚠️ Permission denied. Attempt {attempt + 1}/{max_attempts}. Retrying in 2 seconds...")
                time.sleep(2)
                continue
            else:
                # Attempt to save to a backup file if permission is still denied
                backup_path = output_path.replace(".xlsx", f"_backup_{int(time.time())}.xlsx")
                df.to_excel(backup_path, index=False)
                print(f"❌ Failed to save to {output_path}. Backup saved to {backup_path}")
                raise Exception(f"Permission denied after {max_attempts} attempts. Backup created at {backup_path}")
        except Exception as e:
            raise Exception(f"❌ Failed to save Excel file to {output_path}: {str(e)}")