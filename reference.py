import os
import shutil

# 資料夾路徑
root_folder = 'C:\\Users\\hanbi\\Gue'

# 新資料夾路徑
output_folder = 'D:\\戀活場景卡\\動態\\Gue'
video_folder = 'D:\\vids\\Reta'
txt_folder = "D:\\txt\\Reta"

def copy_file(attachment_folder, filename, output_folder):
    source_file = os.path.join(attachment_folder, filename)
                # 新檔案路徑
    destination_file = os.path.join(output_folder, filename)
                # 複製檔案到新的資料夾
    shutil.copy(source_file, destination_file)

# 遞迴地遍歷根資料夾
for foldername, subfolders, filenames in os.walk(root_folder):
    # 檢查是否有attachments資料夾
    if 'attachments' in subfolders:
        attachment_folder = os.path.join(foldername, 'attachments')
        # 遍歷attachments資料夾
        for name in filenames:
            if name.endswith('.zip'):
                copy_file(foldername, name, output_folder)
                print("一個zip")
        for filename in os.listdir(attachment_folder):
            # 檢查文件是否是PNG檔案
            if filename.endswith('.png'):
                print("一張png")
                copy_file(attachment_folder, filename, output_folder)
            if filename.endswith('.zip'):
                print("一個zip")
                copy_file(attachment_folder, filename, output_folder)
            if filename.endswith('.mp4'):
                copy_file(attachment_folder, filename, video_folder)
            if filename.endswith('.txt'):
                copy_file(attachment_folder, filename, txt_folder)

