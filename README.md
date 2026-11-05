# Kono Radio

AI・テクノロジー・セキュリティなどのニュースを声で届ける、個人運営の実験的なWebラジオ局です。

このリポジトリは [monoradio102/myradio](https://github.com/monoradio102/myradio) をベースにしています。MIT License のプログラムと、テンプレート付属のキャラクターパックを利用しています。

## 現在の状態

- 局名・ロゴ・公開URL・日本語設定は変更済み
- テンプレートのサンプル放送は除去済み
- **初回放送の台本と音声は未制作です。** `episodes.json` が空のため、現時点では放送を再生できません
- コメントは未設定です。元の局の giscus のIDは引き継いでいません
- 毎日のニュース収集・台本作成・音声合成・配信の自動化は未実装です

## ローカルでの表示

```sh
git clone https://github.com/kono0/kono-radio.git
cd kono-radio
python -m http.server 8000
```

ブラウザで `http://localhost:8000` を開きます。音声がない現状では「放送なし」の表示になります。

## 初回の放送を追加する

1. `docs/formats.md` に従い、`episodes/YYYY-MM-DD-ja.json` を作成する。各ニュースの出典URLは実在確認する。
2. 台本の読み上げ用テキストから利用規約を守った日本語TTSで音声を作り、`audio/YYYY-MM-DD-ja.mp3` に配置する。
3. **実際の音声に合わせて** `seconds`, `lines_timed`, `segments` を記入する（適当な時刻は入れない）。
4. `episodes.json` に日付とタイトル、実測の長さを登録する。
5. 音声は `main` にコミットしない（`.gitignore` 対象）。公開環境で音声が見つかるよう `tools/publish.sh` から発行する。

## GitHub Pages公開

台本と実音声を揃えたあとに、リポジトリのローカル作業環境から `bash tools/publish.sh` を実行し、Settings → Pages → Build and deployment の Source を **Deploy from a branch**、Branch を **gh-pages / (root)** にします。

公開URL（予定）：https://kono0.github.io/kono-radio/

注意：`tools/publish.sh` は `gh-pages` ブランチに強制pushします。すでに公開ブランチ上に独自の変更がある場合は実行前に確認してください。

## データ構成

- `station.json` 局名・公開URL・音声保存期間・言語など
- `episodes.json` 放送一覧
- `episodes/` 台本（Gitで管理）
- `audio/` 生成した放送音声（mainでは管理しない）
- `character/` キャラクターと表情差分
- `index.html` ブラウザ用プレーヤー

詳しい仕様は [AGENTS.md](AGENTS.md)、[docs/formats.md](docs/formats.md)、[元テンプレート](https://github.com/monoradio102/myradio) を参照してください。
