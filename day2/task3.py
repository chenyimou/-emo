import os
import csv
from pathlib import Path


def match_images_to_names(image_folder, name_file_path, output_csv, rename_images=False):
    """
    将图片与名字一一对应

    参数:
    image_folder: 包含图片的文件夹路径
    name_file_path: 包含名字的文本文件路径
    output_csv: 输出的CSV文件路径
    rename_images: 是否重命名图片文件
    """
    # 检查路径是否存在
    if not os.path.exists(image_folder):
        raise FileNotFoundError(f"图片文件夹不存在: {image_folder}")
    if not os.path.exists(name_file_path):
        raise FileNotFoundError(f"名字文件不存在: {name_file_path}")
    # 1. 读取名字列表
    with open(name_file_path, 'r', encoding='utf-8') as f:
        names = [line.strip() for line in f.readlines() if line.strip()]

    # 2. 获取图片文件夹中的所有图片文件
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    image_files = [f for f in os.listdir(image_folder)
                   if os.path.isfile(os.path.join(image_folder, f))
                   and os.path.splitext(f)[1].lower() in image_extensions]

    # 3. 检查数量是否匹配
    if len(image_files) != len(names):
        print(f"警告: 图片数量({len(image_files)})和名字数量({len(names)})不匹配!")
        return

    # 4. 保持图片原始顺序(按创建时间或其他系统默认顺序)

    # 5. 创建对应关系
    mapping = []
    for i, (img, name) in enumerate(zip(image_files, names)):
        # 创建映射条目
        mapping.append({
            '图片序号': i + 1,
            '原始文件名': img,
            '对应名字': name,
            '新文件名': f"{name}{os.path.splitext(img)[1]}" if rename_images else img
        })

        # 6. 可选：重命名图片文件
        if rename_images:
            old_path = os.path.join(image_folder, img)
            base_path = os.path.join(image_folder, name)
            ext = os.path.splitext(img)[1]
            new_path = f"{base_path}{ext}"

            # 处理文件名冲突
            counter = 1
            while os.path.exists(new_path):
                new_path = f"{base_path}_{counter}{ext}"
                counter += 1

            try:
                os.rename(old_path, new_path)
                print(f"重命名: {img} -> {os.path.basename(new_path)}")
            except Exception as e:
                print(f"重命名失败 {img}: {str(e)}")

    # 7. 保存为CSV文件
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:  # utf-8-sig 支持Excel中文
        writer = csv.DictWriter(f, fieldnames=['图片序号', '原始文件名', '对应名字', '新文件名'])
        writer.writeheader()
        writer.writerows(mapping)

    print(f"\n成功创建对应表! 已保存至: {output_csv}")
    print(f"图片总数: {len(mapping)}")


if __name__ == "__main__":
    # ===== 配置区域 =====
    # 图片文件夹路径 (包含25张图片)
    IMAGE_FOLDER = r"C:\Users\21923\Desktop\新建文件夹"  # 使用用户指定的图片文件夹路径

    # 名字文件路径 (包含25个名字的文本文件)
    NAME_FILE = "新建文本文档.txt"  # 确保此文件存在

    # 输出CSV文件路径
    OUTPUT_CSV = "图片名字对应表.csv"

    # 是否重命名图片文件 (True: 重命名, False: 不重命名)
    RENAME_IMAGES = True  # 启用图片重命名功能
    # ===== 配置结束 =====

    # 运行匹配程序
    match_images_to_names(IMAGE_FOLDER, NAME_FILE, OUTPUT_CSV, RENAME_IMAGES)