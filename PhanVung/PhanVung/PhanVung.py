import cv2
import numpy as np

# ==============================
# 0. Hàm kiểm tra đồng nhất
# ==============================
def is_homogeneous(region, T):
    return np.max(region) - np.min(region) < T


# ==============================
# 1. SPLIT (cây tứ phân)
# ==============================
def split(image, x, y, size, T, min_size=8):
    region = image[y:y+size, x:x+size]

    # Nếu vùng đồng nhất → lá
    if is_homogeneous(region, T) or size <= min_size:
        return [(x, y, size, int(np.mean(region)))]

    half = size // 2
    regions = []
    regions += split(image, x, y, half, T, min_size)
    regions += split(image, x+half, y, half, T, min_size)
    regions += split(image, x, y+half, half, T, min_size)
    regions += split(image, x+half, y+half, half, T, min_size)

    return regions


# ==============================
# 2. MERGE
# ==============================
def merge_regions(regions, T):
    merged = []
    used = [False]*len(regions)
    region_count = 0  

    for i in range(len(regions)):
        if used[i]:
            continue

        x1, y1, s1, v1 = regions[i]
        group = [(x1, y1, s1, v1)]
        used[i] = True

        for j in range(i+1, len(regions)):
            if used[j]:
                continue

            x2, y2, s2, v2 = regions[j]

            # Điều kiện hợp: gần nhau về mức xám
            if abs(v1 - v2) < T:
                group.append((x2, y2, s2, v2))
                used[j] = True

        avg = int(np.mean([g[3] for g in group]))

        for g in group:
            merged.append((g[0], g[1], g[2], avg))

        region_count += 1

    return merged, region_count


# ==============================
# 3. MAIN
# ==============================

# Đọc ảnh xám
img = cv2.imread(r"D:\BT_XULYANH\anh_lena.jpg", 0)

if img is None:
    print("Không tìm thấy ảnh")
    exit()

# ===== LỌC NHIỄU TRUNG VỊ =====
img_filtered = cv2.medianBlur(img, 3)

# Padding để ảnh vuông
h, w = img_filtered.shape
size = max(h, w)

img_pad = np.zeros((size, size), np.uint8)
img_pad[:h, :w] = img_filtered

T = 20  # Ngưỡng

# ===== SPLIT =====
regions = split(img_pad, 0, 0, size, T)

print("Số lá của cây tứ phân (sau Split):", len(regions))

split_result = np.zeros_like(img_pad)
for (x, y, s, v) in regions:
    split_result[y:y+s, x:x+s] = v

split_result = split_result[:h, :w]

# ===== MERGE =====
merged_regions, merge_count = merge_regions(regions, T)

print("Số vùng sau khi Merge:", merge_count)

merge_result = np.zeros_like(img_pad)
for (x, y, s, v) in merged_regions:
    merge_result[y:y+s, x:x+s] = v

merge_result = merge_result[:h, :w]


# ===== HIỂN THỊ =====
cv2.imshow("Anh goc", img)
cv2.imshow("Split", split_result)
cv2.imshow("Merge", merge_result)

cv2.imwrite("split.jpg", split_result)
cv2.imwrite("merge.jpg", merge_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
