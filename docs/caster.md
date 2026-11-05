# Kono Radio キャスターデザイン

採用するキャスターは、会話で指定された海をテーマにした青白い少女の設定画を基準とします。

- 銀色〜淡い青紫の長いウェーブ髪、両側のまとめ髪
- 錨のマークが入ったヘッドホン
- ヒトデのヘアアクセサリー、青いリボン、海をイメージした小物
- 白と水色・紺を基調とするオーバーサイズの上着
- 青い目、元気な表情

## 現在の素材

元の画像は **複数の三面図・表情を含む設定資料** なので、`character/base.png` としてそのまま使うと放送中に設定画全体が表示されます。まず、左のキャラクター部分を切り出し、放送用の `character/base.jpg` を生成してください。

```bash
python -m pip install Pillow
python tools/make_kono_character.py /path/to/reference.png
```

このコマンドは `character/base.jpg` と `character/character.json` を出力します。生成ファイルをコミットし、`station.json` の `character.thumbnail` を `character/base.jpg` に変更すると放送画面へ反映されます。

**注意：** 設定資料そのものは必要ないため公開リポジトリに追加しなくても構いません。元の `character/base.png` と `character/mouth_*.png` 等は旧キャラの素材で、新キャラには重ねません。口パク・まばたき用の差分は後で同じ構図にそろえて作成してください。

現時点では静止画になりますが、Webプレーヤーの `sprites` モードで表示可能です。キャラパックの既存仕様は [formats.md](formats.md) を参照してください。
