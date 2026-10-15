# Chunks × FSI English Trainer

## 專案目的
把美國國務院的公開英文情境教材，編排為可長期反覆練習的課程：**Chunks → 替換 → 堆疊 → 轉換 → 問答 → 完整對話**。

此專案**不是**美國國務院或 Foreign Service Institute 官方系統，也不是把 GitHub 上的程式碼直接在 ChatGPT 內執行。ChatGPT 可讀取課程 JSON、根據 `TEACHING_RULES.md` 提供教學及互動卡片；Web App 則可作為獨立的日常訓練介面。

## 目錄

```
index.html                         # 手機優先的靜態 Web App（可放 GitHub Pages／Netlify）
TEACHING_RULES.md                  # AI 語言教練的教學規則
curriculum/index.json              # 課程索引
curriculum/lessons/                 # 每堂課獨立 JSON
  lesson-01-ordering-a-meal.json   # 完成的首堂示範課
 tests/validate_lesson.py          # 教材格式和練習一致性檢查
```

## 課程來源
- U.S. Department of State — *Everyday Conversations: Learning American English*
- 目前已編寫 Lesson 01：餐廳點餐，**對應官方 Dialogue 2-1: Ordering a Meal（第 24 頁）**。
- [官方教材首頁](https://americanenglish.state.gov/resources/everyday-conversations-learning-american-english)
- [官方 PDF](https://americanenglish.state.gov/files/ae/resource_files/b_dialogues_everyday_conversations_english_lo_0.pdf)
- [原始課文 MP3](https://americanenglish.state.gov/files/ae/resource_files/dialogue_2-01_ordering_a_meal.mp3)

> 教材設計與新例句為本專案重新編寫。保留原始來源，不將改編題目描述為官方逐字內容。朗讀按鈕使用瀏覽器 TTS，與教材 MP3 是不同的來源。

## 使用
在支援靜態網站的 HTTPS 服務部署整個資料夾即可。根目錄 `index.html` 會讀取相對路徑的 `curriculum/index.json` 和課程 JSON。離線用 `file://` 直接開可能觸發瀏覽器 fetch 安全限制；可用 `python3 -m http.server 8080` 進行本機預覽。

## 限制
- 語音來自瀏覽器內建 TTS；無須語音辨識或 API 金鑰。
- 暫無雲端帳號／跨裝置同步，練習紀錄存在使用者瀏覽器 localStorage。
- UI 提供的是逐句對話和自評，不是即時 AI 自由生成對話，也不能自動評判說話品質。
- 首版只完成一堂課；其餘教材必須逐堂製作與檢查後才能標示 ready。

## 日文教材來源與使用
- 課程來源：《大家來學日文》教學影片；使用者透過 NotebookLM 的「報告」功能生成第二課整理文件，並提供給本專案。
- 網站目前提供 **English：10 堂**、**日本語：1 堂（第 2 課）**。沒有提供的課程不會捏造或以其他教材替代。
- 日文第 2 課包括指示詞、名詞修飾詞「この／その／あの」、助詞「の」、所有格、疑問／否定句以及交換物品情境；另編堆疊練習和三輪完整對話。
- 此為依使用者的 NotebookLM 報告重新編排的訓練教材，**非《大家來學日文》官方教材**，亦未獨立比對原影片或核驗 NotebookLM 報告中的日文音高標註。
- 日文朗讀使用瀏覽器內建 **ja-JP** 語音；中文操作說明保留，兩個語言的進度與自評紀錄以不同課程鍵分開儲存。
- 在 GitHub 上編輯 `curriculum/index.json` 和 `curriculum/lessons/*.json` 即可增修課程。新增語言課程必須包含 `language_track`、`language`、各練習區塊和來源標註。

