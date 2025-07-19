from PIL import Image
import requests
import os
import mercantile

def get_tiles_japan(z):
    # 日本全域の緯度経度
    bounds = (123.0, 20.0, 154.0, 46.0)
    return list(mercantile.tiles(*bounds, zooms=[z]))

def download_dem_tile(tile, output_root="dem_txt"):
    url = f"https://cyberjapandata.gsi.go.jp/xyz/dem/{tile.z}/{tile.x}/{tile.y}.txt"
    r = requests.get(url)
    if r.status_code == 200:
        out_dir = os.path.join(output_root, str(tile.z), str(tile.x))
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{tile.y}.txt")
        with open(out_path, "w") as f:
            f.write(r.text)
        return out_path
    return None

def elevation_to_rgb(elev: float) -> tuple[int, int, int]:
    v = int((elev + 10000) * 10)
    r = (v >> 16) & 0xFF
    g = (v >> 8) & 0xFF
    b = v & 0xFF
    return (r, g, b)

# NoData時のRGB（標高0mに相当）
NODATA_RGB = elevation_to_rgb(0.0)  # (1, 134, 160)

def convert_txt_to_terrain_rgb(txt_path: str, output_root="terrain_rgb"):
    import re
    m = re.search(r'(\d+)[/\\](\d+)[/\\](\d+)\.txt$', txt_path)
    if not m:
        print(f"パス形式が想定外: {txt_path}")
        return
    z, x, y = m.groups()
    
    out_dir = os.path.join(output_root, z, x)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{y}.png")

    with open(txt_path, "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]

    img = Image.new("RGB", (256, 256))
    for y_px, row in enumerate(lines):
        for x_px, val in enumerate(row):
            try:
                elev = float(val)
                color = elevation_to_rgb(elev)
            except:
                color = NODATA_RGB
            img.putpixel((x_px, y_px), color)

    img.save(out_path, "PNG")

for z in range(1, 15):
    tiles = get_tiles_japan(z)
    for tile in tiles:
        txt_file = download_dem_tile(tile)
        if txt_file:
            print(f"処理中: {txt_file}")
            convert_txt_to_terrain_rgb(txt_file)