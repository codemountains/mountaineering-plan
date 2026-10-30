# 登山計画 プラグイン

ChatGPT / Codex 向けの、登山計画を支援するスキル同梱プラグインです。プラグインのルートはこの `plugin/` ディレクトリです。MCP サーバー、API キー、外部サービスへのログインは不要です。最新情報の確認には、利用環境の Web 検索・資料閲覧機能が必要です。

## 構成

```text
plugin/
├── plugin.json
├── .agents/plugins/marketplace.json
├── skills/mountaineering-plan/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── project-instructions.md
│       └── mountaineering-plan.md
└── README.md
```

`plugin.json` は Agent Plugins 形式のマニフェストです。`skills/` がスキルの探索先で、表示情報は `extensions.com.openai` に定義しています。配布時に必要な指示・資料はこのディレクトリ内で完結します。

## ローカルで使う

このリポジトリのルートから、プラグイン対応の Codex CLI で次を実行します。

```sh
codex plugin marketplace add ./plugin
codex plugin add mountaineering-plan@mountaineering-plan-local
```

CLI の `plugin add` がない環境では、marketplace を追加後、ChatGPT デスクトップアプリを再起動し、Plugins Directory のソース「登山計画」からインストールします。ローカル marketplace の利用可否はクライアント・組織設定によって異なります。

インストール後は新しい会話で、`@` メニューから「登山計画」を選択します。プラグインとスキルの表示名は、どちらも「登山計画」です。`@登山計画` と入力して候補から利用するプラグインまたはスキルを選択してください。

Codex CLI では、次のように内部名でスキルを指定します。

```text
$mountaineering-plan
2026-11-07 に公共交通で岩手山への日帰り登山を検討しています。
出発駅、経験、装備、帰宅希望時刻など、必要な条件を確認して計画してください。
```

日付・山・出発地・経験・携行装備・帰宅期限は実際の条件に置き換えます。気象や交通だけの個別質問にも使えます。

登録状況は次で確認できます。

```sh
codex plugin list --marketplace mountaineering-plan-local
```

配布設定の `source.path` は `./` です。これは marketplace のルートである `plugin/` を指し、`.agents/plugins/` からの相対パスではありません。このローカル登録は公開ディレクトリへの公開ではありません。

## Web 版で作成済みのプラグインに反映する

新規作成する場合は、[Plugin Creator を使った作成手順](../docs/create-plugin-with-plugin-creator.md)を参照してください。

ローカルの変更は、Plugin Creator で作成済みの Web 版プラグインには自動反映されません。Web 版の Plugins から対象プラグインの Edit Plugin を開き、`skills/mountaineering-plan/agents/openai.yaml` を添付して次のように依頼してください。

```text
プラグインと、含まれる登山計画用スキルの表示名を、両方とも「登山計画」にしてください。
添付した openai.yaml をスキルの表示設定として反映し、
@ メニューから「登山計画」を選択できるようにしてください。
プラグインとスキルの内部名は mountaineering-plan にそろえ、
既存の判断手順と参照資料を保持してください。
```

保存後、新しい会話で `@登山計画` と入力し、候補からスキルを選択できるか確認します。このリポジトリでの設定検証と、Web 版での表示・呼び出し確認は別です。

## 旧名からの移行

ファイル名・スキルのディレクトリ名・プラグインとスキルの内部名は `mountaineering-plan` に統一しています。CLI の呼び出し名は `$mountaineering-plan`、インストール時の識別子は `mountaineering-plan@mountaineering-plan-local` です。

旧名でインストール済みの場合、新しい識別子は別プラグインとして扱われます。改名後のリポジトリから「ローカルで使う」のコマンドで登録・インストールし、動作確認後、不要な旧プラグインをプラグイン管理画面から削除してください。ルートディレクトリを移動した場合も、新しい場所で marketplace を登録し直してください。

以前の ChatGPT プロジェクト向け構成を利用していた場合も、今後の更新はこのプラグインのスキルに集約します。Plugin Creator で作成した Web 版では、同梱資料の差し替えと参照先の更新も依頼してください。

GitHub のリポジトリ URL は現在の公開先を記載しています。ローカルのルートディレクトリ名の変更とは別に管理します。

## 資料を更新する

原本はこのプラグイン内の次の2ファイルです。直接編集し、変更をコミットしてください。

- [基本指示](skills/mountaineering-plan/references/project-instructions.md)
- [詳細資料](skills/mountaineering-plan/references/mountaineering-plan.md)

リポジトリ直下の旧原本と同期スクリプトは廃止しました。詳細資料の改訂時は版番号・更新日も更新し、`SKILL.md` の参照先と必要な節・付録が維持されていることを確認してください。

スキルの適用条件・資料の読み方は `skills/mountaineering-plan/SKILL.md`、スキルの表示名は `skills/mountaineering-plan/agents/openai.yaml`、プラグインの表示情報・バージョンは `plugin.json` で管理します。リリース時はプラグインのバージョンも更新します。資料の版番号とは別管理です。

インストール済みプラグインはキャッシュから読み込まれます。更新後は marketplace を更新し、アプリを再起動して新しい会話で確認してください。

```sh
codex plugin marketplace upgrade mountaineering-plan-local
```

## 回答の確認

インストール後は詳細資料の付録Aの条件を試し、未確認情報を確認済みにしないこと、日付不足や検索不可を適切に扱うこと、公式閉鎖を NO-GO とすること、制約ごとの撤退時刻とバッファが整合することを確認します。ファイルの検証だけでは、実際のモデルによる回答品質やアプリでの読み込みは保証できません。

## 仕様の参照先

- [Package your plugin（OpenAI 公式）](https://developers.openai.com/plugins/build/plugins)
- [Build skills（OpenAI 公式）](https://developers.openai.com/plugins/build/skills)
- [スキルの表示メタデータ（OpenAI 公式）](https://developers.openai.com/plugins/deploy/submission-errors#skill-agent-metadata-errors)

2026-10-26 に確認。CLI コマンドは Codex CLI 0.163.0 のヘルプでも確認しています。
