import pandas as pd

def clean_vgsales(input_file="vgsales.csv", output_csv="vgsales_clean.csv", output_xlsx="vgsalesclean.xlsx"):
    print(f"Đang đọc dữ liệu từ '{input_file}'...")
    if input_file.endswith(".csv"):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)

    initial_rows = len(df)
    print(f"Số dòng ban đầu: {initial_rows:,}")

    # 1. Chuẩn hóa chuỗi văn bản (cắt khoảng trắng thừa)
    text_cols = ["Name", "Platform", "Genre", "Publisher"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    # 2. Chuẩn hóa kiểu dữ liệu số cho doanh số
    sale_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    for col in sale_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").round(2)

    # 3. Chuẩn hóa cột Year
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    # 4. Loại bỏ các dòng có giá trị bị thiếu (Missing values)
    null_counts = df.isna().sum()
    print("Số lượng giá trị khuyết thiếu trước khi xử lý:")
    print(null_counts[null_counts > 0])

    df_cleaned = df.dropna(how="any").copy()

    # 5. Chuyển đổi Year sang kiểu số nguyên int64
    df_cleaned["Year"] = df_cleaned["Year"].astype("int64")

    # 6. Sắp xếp dữ liệu theo Global_Sales giảm dần
    df_cleaned = df_cleaned.sort_values("Global_Sales", ascending=False).reset_index(drop=True)

    # 7. Xuất file kết quả
    if output_csv:
        df_cleaned.to_csv(output_csv, index=False)
        print(f"Đã lưu file CSV sạch: {output_csv}")

    if output_xlsx:
        df_cleaned.to_excel(output_xlsx, index=False, engine="openpyxl")
        print(f"Đã lưu file Excel sạch: {output_xlsx}")

    final_rows = len(df_cleaned)
    removed_rows = initial_rows - final_rows
    print(f"Hoàn thành: Giữ lại {final_rows:,} dòng (đã loại {removed_rows:,} dòng lỗi/thiếu).")

    return df_cleaned

if __name__ == "__main__":
    clean_vgsales()
