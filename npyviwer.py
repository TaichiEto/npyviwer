import numpy as np
import matplotlib.pyplot as plt

def read_and_save_npy_image(file_path, image_index=0, output_file="output_image.png"):
    try:
        # メモリ効率を考慮して大きなデータを読み込む
        data = np.load(file_path, mmap_mode='r')

        # データ情報の確認
        print(f"データの形状: {data.shape}")
        print(f"データ型: {data.dtype}")

        # インデックスの範囲チェック
        if image_index < 0 or image_index >= data.shape[0]:
            raise IndexError(f"指定されたインデックス {image_index} は有効範囲外です (0 ～ {data.shape[0]-1})")

        # 特定の画像を取得して保存
        image = data[image_index, 0, :, :]
        plt.imshow(image, cmap='gray')
        plt.axis('off')  # 軸を非表示

        # 画像をファイルに保存
        plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
        print(f"画像が保存されました: {output_file}")

    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    # ファイルパスとインデックスの入力
    file_path = input("読み込む .npy ファイルのパスを入力してください: ")
    image_index = int(input("表示する画像のインデックスを入力してください (0から始まる): "))
    output_file = input("保存する画像のファイル名を入力してください（例: output.png）: ")
    read_and_save_npy_image(file_path, image_index, output_file)