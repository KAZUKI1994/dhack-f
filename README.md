# dhack-f
This is the f team. 
Our team name is *"Hickeys"*.
私たちは、「ヒッキーズ」です。DIT主催の同志社大学生限定ハッカソンDHACKS用のGitHub

#Data Table
##バイト情報データベースフィールド
| label            | var         | field         | input[type] | detail                   |
|------------------|-------------|---------------|-------------|--------------------------|
| タイトル         | title       | CharField     | text        | 学内バイト募集タイトル   |
| 募集者           | publisher   | CharField     | text        |                          |
| 募集者電話       | pub_phone   | IntegerField  | tel         |                          |
| 募集者メール     | pub_mail    | EmailField    | email       |                          |
| 募集内容         | content     | TextField     | textarea    | 500文字以内              |
| 募集条件         | condition   | CharField     | text        | 例：男性1年など          |
| 募集校地         | canvas      | CharField     | checkbox    | 今出川or京田辺           |
| 場所             | location    | CharField     | text        | 校舎・教室               |
| 募集期間（開始） | work_start  | DateField     | date        | 治験バイトを募集する期間 |
| 募集期間（終了） | word_finish | DateField     | date        | 募集締め切り期間         |
| 報酬種類         | money_kind  | CharField     | radio       | 時給or固定給             |
| 報酬（金額）     | money_amout | IntegerField  | number      | 金額                     |
| アイキャッチ画像 | top_image   | FilePathField | radio       |                          |

