import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Thiết lập thẩm mỹ cho biểu đồ
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'Segoe UI, DejaVu Sans, Arial'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

os.makedirs('charts', exist_ok=True)
df = pd.read_csv('vgsales_clean.csv')

# -------------------------------------------------------------
# 1. Top 10 game bán chạy nhất toàn cầu (bar chart)
# -------------------------------------------------------------
plt.figure(figsize=(12, 6.5))
top10 = df.head(10).copy().sort_values('Global_Sales', ascending=True)

# Hiển thị tên game kèm Platform
labels = [f"{name} ({plat})" for name, plat in zip(top10['Name'], top10['Platform'])]
colors = sns.color_palette("mako", len(top10))

bars = plt.barh(labels, top10['Global_Sales'], color=colors, edgecolor='none', height=0.65)
plt.title('Top 10 Game Bán Chạy Nhất Toàn Cầu (Global Sales)', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
plt.xlabel('Doanh số toàn cầu (Triệu bản)', fontsize=12, labelpad=10, color='#334155')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.8, bar.get_y() + bar.get_height()/2, f'{width:.2f}M',
             va='center', ha='left', fontsize=10.5, fontweight='600', color='#0f172a')

plt.xlim(0, max(top10['Global_Sales']) * 1.1)
plt.tight_layout()
plt.savefig('charts/1_top_10_games.png', dpi=300)
plt.close()
print("1. Đã tạo charts/1_top_10_games.png")

# -------------------------------------------------------------
# 2. Doanh số theo thể loại (Genre) - Tổng và Trung bình
# -------------------------------------------------------------
genre_stats = df.groupby('Genre')['Global_Sales'].agg(['sum', 'mean', 'count']).sort_values('sum', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Tổng doanh số
sns.barplot(x=genre_stats['sum'], y=genre_stats.index, palette='crest', ax=ax1)
ax1.set_title('Tổng Doanh Số Theo Thể Loại (Triệu bản)', fontsize=13, fontweight='bold', color='#1e293b')
ax1.set_xlabel('Tổng doanh số (Triệu bản)', fontsize=11, color='#334155')
ax1.set_ylabel('')
for bar in ax1.patches:
    width = bar.get_width()
    ax1.text(width + 15, bar.get_y() + bar.get_height()/2, f'{width:,.0f}M',
             va='center', ha='left', fontsize=9.5, color='#0f172a', fontweight='600')
ax1.set_xlim(0, genre_stats['sum'].max() * 1.15)

# Doanh số trung bình mỗi đầu game
genre_avg_sorted = genre_stats.sort_values('mean', ascending=False)
sns.barplot(x=genre_avg_sorted['mean'], y=genre_avg_sorted.index, palette='flare', ax=ax2)
ax2.set_title('Doanh Số Trung Bình Mỗi Đầu Game Theo Thể Loại', fontsize=13, fontweight='bold', color='#1e293b')
ax2.set_xlabel('Doanh số trung bình / game (Triệu bản)', fontsize=11, color='#334155')
ax2.set_ylabel('')
for bar in ax2.patches:
    width = bar.get_width()
    ax2.text(width + 0.015, bar.get_y() + bar.get_height()/2, f'{width:.2f}M',
             va='center', ha='left', fontsize=9.5, color='#0f172a', fontweight='600')
ax2.set_xlim(0, genre_avg_sorted['mean'].max() * 1.15)

plt.suptitle('Phân Tích Doanh Số Theo Thể Loại Game (Genre)', fontsize=15, fontweight='bold', y=0.98, color='#0f172a')
plt.tight_layout()
plt.savefig('charts/2_genre_sales.png', dpi=300)
plt.close()
print("2. Đã tạo charts/2_genre_sales.png")

# -------------------------------------------------------------
# 3. Xu hướng doanh số theo năm (line chart)
# -------------------------------------------------------------
yearly = df[df['Year'] <= 2016].groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

plt.figure(figsize=(14, 6.5))
plt.plot(yearly.index, yearly['Global_Sales'], label='Toàn Cầu (Global)', color='#0284c7', linewidth=3.2, marker='o', markersize=5)
plt.plot(yearly.index, yearly['NA_Sales'], label='Bắc Mỹ (NA)', color='#10b981', linewidth=2, linestyle='--')
plt.plot(yearly.index, yearly['EU_Sales'], label='Châu Âu (EU)', color='#f59e0b', linewidth=2, linestyle='-.')
plt.plot(yearly.index, yearly['JP_Sales'], label='Nhật Bản (JP)', color='#ef4444', linewidth=2, linestyle=':')
plt.plot(yearly.index, yearly['Other_Sales'], label='Khu vực khác', color='#8b5cf6', linewidth=1.8, linestyle='-')

# Đánh dấu giai đoạn hoàng kim (2006 - 2010)
plt.axvspan(2006, 2010, color='#fde047', alpha=0.25, label='Kỷ nguyên hoàng kim (Peak Era: 2006-2010)')

peak_year = yearly['Global_Sales'].idxmax()
peak_sales = yearly['Global_Sales'].max()
plt.annotate(f'Đỉnh cao: {peak_year} ({peak_sales:.1f}M bản)',
             xy=(peak_year, peak_sales), xytext=(peak_year - 5, peak_sales + 40),
             arrowprops=dict(arrowstyle='->', lw=1.5, color='#0369a1'),
             fontsize=11, fontweight='bold', color='#0369a1',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#e0f2fe', edgecolor='#0284c7'))

plt.title('Xu Hướng Doanh Số Bán Game Toàn Cầu & Khu Vực Theo Năm (1980 - 2016)', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
plt.xlabel('Năm phát hành', fontsize=12, labelpad=10, color='#334155')
plt.ylabel('Doanh số (Triệu bản)', fontsize=12, labelpad=10, color='#334155')
plt.xticks(range(1980, 2017, 3), rotation=45)
plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=10.5, loc='upper left')
plt.tight_layout()
plt.savefig('charts/3_yearly_trend.png', dpi=300)
plt.close()
print("3. Đã tạo charts/3_yearly_trend.png")

# -------------------------------------------------------------
# 4. Top nhà phát hành (Publisher) theo tổng doanh số
# -------------------------------------------------------------
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True)

plt.figure(figsize=(12, 6.5))
colors_pub = sns.color_palette("viridis", len(top_publishers))
bars_pub = plt.barh(top_publishers.index, top_publishers.values, color=colors_pub, height=0.65)

plt.title('Top 10 Nhà Phát Hành Game Có Doanh Số Cao Nhất Toàn Cầu', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
plt.xlabel('Tổng doanh số toàn cầu (Triệu bản)', fontsize=12, labelpad=10, color='#334155')

for bar in bars_pub:
    width = bar.get_width()
    plt.text(width + 15, bar.get_y() + bar.get_height()/2, f'{width:,.1f}M',
             va='center', ha='left', fontsize=10, fontweight='600', color='#0f172a')

plt.xlim(0, top_publishers.max() * 1.15)
plt.tight_layout()
plt.savefig('charts/4_top_publishers.png', dpi=300)
plt.close()
print("4. Đã tạo charts/4_top_publishers.png")

# -------------------------------------------------------------
# 5. So sánh doanh số giữa các khu vực theo thể loại
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 7.5), gridspec_kw={'width_ratios': [2.2, 1]})

genre_regional = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
genre_regional['Total'] = genre_regional.sum(axis=1)
genre_regional = genre_regional.sort_values('Total', ascending=True).drop(columns=['Total'])

genre_regional.plot(kind='barh', stacked=True, ax=ax1, color=['#3b82f6', '#10b981', '#ef4444', '#a855f7'], width=0.7)
ax1.set_title('Cơ Cấu Doanh Số Từng Khu Vực Theo Thể Loại', fontsize=13, fontweight='bold', color='#1e293b')
ax1.set_xlabel('Doanh số (Triệu bản)', fontsize=11, color='#334155')
ax1.set_ylabel('')
ax1.legend(['Bắc Mỹ (NA)', 'Châu Âu (EU)', 'Nhật Bản (JP)', 'Khu vực khác'], loc='lower right', frameon=True)

# Biểu đồ tròn thị phần toàn cầu
total_regional = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
wedges, texts, autotexts = ax2.pie(
    total_regional,
    labels=['Bắc Mỹ', 'Châu Âu', 'Nhật Bản', 'Khác'],
    autopct='%1.1f%%',
    startangle=140,
    colors=['#3b82f6', '#10b981', '#ef4444', '#a855f7'],
    explode=(0.04, 0.04, 0.04, 0.04),
    wedgeprops=dict(width=0.6, edgecolor='white', linewidth=2)
)
for at in autotexts:
    at.set_color('white')
    at.set_fontweight('bold')
    at.set_fontsize(10.5)

ax2.set_title('Tỷ Trọng Thị Phần Doanh Số Các Khu Vực', fontsize=13, fontweight='bold', color='#1e293b')

plt.suptitle('So Sánh Doanh Số Giữa Các Khu Vực (NA / EU / JP / Other)', fontsize=15, fontweight='bold', y=0.98, color='#0f172a')
plt.tight_layout()
plt.savefig('charts/5_regional_comparison.png', dpi=300)
plt.close()
print("5. Đã tạo charts/5_regional_comparison.png")

# -------------------------------------------------------------
# 6. Phân bố doanh số theo Platform (Nền tảng bán chạy nhất)
# -------------------------------------------------------------
plt.figure(figsize=(14, 6.5))
top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(15)

palette_plat = sns.color_palette("Spectral", len(top_platforms))
bars_plat = plt.bar(top_platforms.index, top_platforms.values, color=palette_plat, edgecolor='none', width=0.7)

plt.title('Top 15 Nền Tảng (Platform) Có Doanh Số Game Lớn Nhất Toàn Cầu', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
plt.xlabel('Nền tảng console/hệ máy', fontsize=12, labelpad=10, color='#334155')
plt.ylabel('Tổng doanh số (Triệu bản)', fontsize=12, labelpad=10, color='#334155')
plt.xticks(rotation=45)

for bar in bars_plat:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 12, f'{height:,.0f}M',
             ha='center', va='bottom', fontsize=9, fontweight='600', color='#0f172a')

plt.ylim(0, top_platforms.max() * 1.12)
plt.tight_layout()
plt.savefig('charts/6_platform_sales.png', dpi=300)
plt.close()
print("6. Đã tạo charts/6_platform_sales.png")

print("Hoàn tất tạo toàn bộ 6 biểu đồ chất lượng cao!")
