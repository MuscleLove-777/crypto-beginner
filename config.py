"""クリプト入門ナビ - ブログ固有設定

仮想通貨・DeFi・NFTを初心者目線で徹底解説するブログ。
YMYL×金融分野対策: 断定表現禁止・免責事項必須・金融庁登録業者優先
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

# ブログ基本情報
BLOG_NAME = "クリプト入門ナビ"
BLOG_DESCRIPTION = (
    "仮想通貨・DeFi・NFTを初心者目線で徹底解説。"
    "リスク管理から実践トレードまで、失敗しない暗号資産の始め方"
)
BLOG_URL = "https://musclelove-777.github.io/crypto-beginner"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/crypto-beginner"

# カテゴリ設定
TARGET_CATEGORIES = [
    "仮想通貨の基礎知識",
    "取引所の選び方・比較",
    "DeFi入門",
    "NFT・メタバース",
    "トレード戦略",
    "リスク管理・セキュリティ",
    "税金・確定申告",
    "最新ニュース・トレンド",
]

# テーマカラー（ゴールド×ダーク系 - クリプトっぽい配色）
THEME = {
    "primary": "#b8860b",       # ダークゴールデンロッド
    "accent": "#f5a623",        # ゴールドオレンジ
    "gradient_start": "#b8860b",
    "gradient_end": "#d4a017",
    "dark_bg": "#0d0d0d",       # ほぼブラック
    "dark_surface": "#1a1a2e",  # ダークネイビー
    "light_bg": "#fdf8ef",      # アイボリー系
    "light_surface": "#ffffff",
}

# 記事生成設定
MAX_ARTICLE_LENGTH = 3000       # 1記事あたりの目安文字数
ARTICLES_PER_DAY = 3            # 1日の投稿数
SCHEDULE_HOURS = [7, 12, 19]    # 投稿時刻（7時・12時・19時）

# Gemini API設定
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

# SEO最適化設定
ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70              # 最低SEOスコア（100点満点中）
MIN_KEYWORD_DENSITY = 1.0       # キーワード密度の下限（%）
MAX_KEYWORD_DENSITY = 3.0       # キーワード密度の上限（%）
META_DESCRIPTION_LENGTH = 120   # メタディスクリプション文字数上限
ENABLE_INTERNAL_LINKS = True

# アフィリエイトリンク設定
AFFILIATE_LINKS = {
    "国内取引所": [
        {
            "service": "bitFlyer",
            "url": "https://bitflyer.com/ja-jp/",
            "description": "国内最大級の仮想通貨取引所。金融庁登録済み。初心者に使いやすいUI",
        },
        {
            "service": "Coincheck",
            "url": "https://coincheck.com/ja/",
            "description": "アプリDL数No.1。500円から購入可能。金融庁登録済み",
        },
        {
            "service": "GMOコイン",
            "url": "https://coin.z.com/jp/",
            "description": "GMOグループ運営。手数料無料で送金可能。金融庁登録済み",
        },
    ],
    "海外取引所": [
        {
            "service": "Binance",
            "url": "https://www.binance.com/ja",
            "description": "世界最大の暗号資産取引所。豊富なアルトコイン取扱い",
        },
        {
            "service": "Bybit",
            "url": "https://www.bybit.com/ja-JP/",
            "description": "デリバティブ取引に強い。日本語サポート充実",
        },
    ],
    "ハードウェアウォレット": [
        {
            "service": "Ledger",
            "url": "https://www.ledger.com/ja",
            "description": "世界で最も売れているハードウェアウォレット。セキュリティ最高峰",
        },
        {
            "service": "Trezor",
            "url": "https://trezor.io/",
            "description": "オープンソースのハードウェアウォレット。透明性が高い",
        },
    ],
    "書籍・教材": [
        {
            "service": "Amazon 仮想通貨書籍",
            "url": "https://www.amazon.co.jp/s?k=%E4%BB%AE%E6%83%B3%E9%80%9A%E8%B2%A8+%E5%85%A5%E9%96%80",
            "description": "仮想通貨入門から実践まで幅広い書籍",
        },
        {
            "service": "楽天ブックス 暗号資産",
            "url": "https://books.rakuten.co.jp/search?sitem=%E6%9A%97%E5%8F%B7%E8%B3%87%E7%94%A3",
            "description": "暗号資産・ブロックチェーン関連書籍をポイントで",
        },
    ],
}
AFFILIATE_TAG = "musclelove07-22"

# Google AdSense設定
ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")

# ダッシュボード設定
DASHBOARD_PORT = 8100
