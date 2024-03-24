タスクリスト
- [x] 1. Claspをインストールする
  - ターミナルまたはコマンドプロンプトで以下のコマンドを実行:
    ```
    npm install -g @google/clasp
    ```

- [x] 2. Claspでログインする
  ```
  clasp login
  ```

- [x] 3. GASプロジェクトを作成または既存プロジェクトをクローンする
  - 新規作成:
    ```
    clasp create --title "test" --type standalone
    ```
  - 既存プロジェクトのクローン:
    ```
    clasp clone <スクリプトID>
    ```

- [x] 4. ローカルでコードを編集する
  - 以下の簡単なコード例を参考に、お好みのコードエディタで編集してください。
    ```javascript
    function myFunction() {
      Logger.log('こんにちは、Google Apps Script!');
    }
    ```

- [x] 5. 編集したコードをGASにアップロードする
  ```
  clasp push
  ```

- [x] 6. GAS上で実行や動作確認をする
  ```
  clasp open
  ```
  - GASエディタが開くので、そこで実行や動作確認ができます。

- [x] 7. ローカルからスクリプトを実行する
  - ローカル環境からGoogle Apps Scriptを実行するには、以下の手順を実行してください。
    1. `clasp run` コマンドを使用して、ローカルから直接スクリプトを実行します。この機能を使用するには、Google Cloud PlatformのプロジェクトでAPIを有効にし、適切な権限を設定する必要があります。
    2. 実行したい関数名をコマンドに引数として渡します。例えば、`myFunction` を実行する場合は、以下のように入力します。
       ```
       clasp run myFunction
       ```
    3. 関数が実行され、結果がターミナルに表示されます。`Logger.log` を使用している場合、その出力を直接ターミナルで確認することはできませんが、ログを確認する別の方法を検討してください。

- [ ] 8. APIクレデンシャルの問題を解決する
  - `clasp run` コマンドを使用する際に「Could not read API credentials. Are you logged in locally?」というエラーが発生した場合、以下の手順で解決できます。
    1. Google Cloud Platform (GCP) コンソールにアクセスし、使用しているプロジェクトを選択します。
    2. APIとサービス > 認証情報 に移動します。
    3. 「認証情報を作成」ボタンをクリックし、「サービスアカウント」を選択します。
    4. サービスアカウントを作成し、必要なロールを付与します（例: プロジェクト > エディタ）。
    5. サービスアカウントの詳細ページで、「キーを追加」 > 「新しいキーを作成」を選択し、JSONキーを生成します。
    6. 生成されたJSONキーをダウンロードし、安全な場所に保存します。
    7. ターミナルまたはコマンドプロンプトで、ダウンロードしたJSONキーのパスを `GOOGLE_APPLICATION_CREDENTIALS` 環境変数として設定します。
       ```
       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
       ```
    8. この設定後、再度 `clasp run` コマンドを実行してみてください。問題が解決しているはずです。