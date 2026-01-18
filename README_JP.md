このワークショップでは、LangChainを使用してシンプルなAIエージェントを構築します。AIエージェントを構築する際の基本コンポーネントであるLLM（大規模言語モデル）、ツール、ミドルウェアについて見ていきます。

## 前提条件

- Hugging Face Hubのアカウント、または[他のAIプロバイダー](https://docs.langchain.com/oss/python/integrations/providers/overview)のアカウント
- 中級程度のPython経験
- AIおよび自然言語処理（NLP）の概念に関する基礎知識

## LangChainの紹介

LangChainは、AIエージェントを構築するためのPythonライブラリです。様々なLLMや他のAIツールに接続するための、シンプルで一貫したインターフェースを提供します。

このワークショップでは、`/src`フォルダにあるAIエージェントのスケルトン（骨組み）から開始します。これは簡単に始められる基本的なテンプレートに過ぎず、後でさらに機能を追加することができます。

各章には、サンプルエージェントを構築するためのステップバイステップの指示があります。しかし、使い慣れてきたら、機能を改善したり修正したりするために、独自のコードを書くことをお勧めします。

## 第1章 - LLMへの接続

LangChainを使用する利点は、OpenAI、Anthropic、Hugging Faceなど、多くの人気プロバイダーが提供する多種多様なLLMに接続するための複雑さを抽象化してくれることです。

すでにサポートされているプロバイダーのアカウントをお持ちの場合は、自由に使用してください。ただし、ほとんどのプロバイダーはAPIサービスの使用に対して料金を請求することに注意してください。使用を決定する前に価格表を確認してください。

有料のプロバイダーを使用したくない場合は、AIプロバイダーとしてHugging Face Hubを使用できます。この方法では、オープンソースのLLMをローカルで使用することになります。これには、他の要件に加えてPyTorchやTensorflowをローカルにインストールする必要がある場合があります。

まず、LangChainが提供する[`create_agent`](https://reference.langchain.com/python/langchain/agents/?_gl=1*baxhnz*_gcl_au*Mzg1NzM1NDUxLjE3NjUyMDk4OTg.*_ga*MTk1ODUyNzE1Ny4xNzY1MjA5ODk4*_ga_47WX3HKKY2*czE3Njg2OTU0MjAkbzIwJGcxJHQxNzY4Njk1NDQ4JGoyMiRsMCRoMA..#langchain.agents.create_agent)を使用してエージェントを作成します。

エージェントの作成を開始するには、モデル、ツール、システムプロンプトを指定します。

- モデル: LangChainによって推論されるか（例: "gpt-5"）、または「プロバイダー名:モデル名」の形式（例: "openai:gpt-5"）でモデルプロバイダー名を指定できます。[こちら](https://reference.langchain.com/python/langchain/models/?_gl=1*12ht130*_gcl_au*Mzg1NzM1NDUxLjE3NjUyMDk4OTg.*_ga*MTk1ODUyNzE1Ny4xNzY1MjA5ODk4*_ga_47WX3HKKY2*czE3Njg2OTU0MjAkbzIwJGcxJHQxNzY4Njk1ODAyJGoyNCRsMCRoMA..#langchain.chat_models.init_chat_model(model))を参照してください。
- ツール: ツールは`@tool`デコレータを使用して作成できます。この例では、次の章で`get_weather_info`と`follow_up`の2つのツールを作成します。
- システムプロンプト: これはエージェントに役割を与え、エージェントに期待される動作について明確な指示を与えるためのものです。例えば今回のケースでは、エージェントに特定の場所の気象情報を提供するように指示します。また、`get_weather_info`も参照します。

では、`agent.py`内のコメントに従って、この章の空欄を埋めてください。

## 第2章 - エージェントへのツールの追加

AIエージェントとシンプルなチャットボットの大きな違いの一つは、ツールを使用して拡張できることです。これらのツールは、エージェントがユーザーの要求した特定のタスクを完了するのを助けます。

この章では、エージェントにツールを追加します。どのようなツールをエージェントに持たせるかは、あなた次第です。通常、これらのツールは特定のタスクを完了するために使用されます。例えば、エージェントが特定の場所の最新の天気予報を取得できるようにしたいとします。その場合、天気検索ツールをエージェントに追加します。もう一つの便利なツールは、ユーザーからフォローアップ情報を取得する方法を提供することです。

LangChainでのツールの作成は非常に簡単です。関数に`@tool`デコレータを追加するだけで、LangChainはそれをエージェント内のツールとして認識できます。

`agent.py`内のコメントに従って、ツールの空欄を埋めてください。

これでエージェントをテストできます。オプションとして、結果の辞書から出力のメッセージ部分のみを抽出して表示したい場合があります。これは`parse_result`を使用して行うことができます。

## 第3章 - ミドルウェアの追加

LangChainを使用するもう一つの利点は、エージェントにミドルウェアを簡単に追加できる方法を提供していることです。ミドルウェアは、エージェントへの入力と出力を傍受して修正するために使用できるコードの一部です. 利用可能なミドルウェアの一覧については[こちら](https://docs.langchain.com/oss/python/langchain/middleware/built-in)をご覧ください。独自のミドルウェアを作成することもできます。カスタムミドルウェアの作成方法については[こちら](https://docs.langchain.com/oss/python/langchain/middleware/custom)をご覧ください。

この例では、モデルに送信されるメッセージが長すぎる場合に備えて、単に[SummarizationMiddleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization)を追加します。これは、エージェントとユーザーの間で何度もやり取りが行われる場合に非常に役立ちます。

ドキュメントの[例](https://docs.langchain.com/oss/python/langchain/middleware/built-in#summarization)に従って、エージェントにミドルウェアを追加してください。

章が終わったら、エージェントにさらにツールやミドルウェアを追加するなど、追加機能を追加してもよいでしょう。また、独自のエージェントを作成して、全く別のタスクを実行してみることもできます。

---

## このワークショップを支援する

このワークショップはCheukによって作成され、誰でも使用できるようにオープンソース（MITライセンス）として公開されています。[GitHub Sponsor](https://github.com/sponsors/Cheukting)を通じてCheukの活動をスポンサーすることを検討してください。