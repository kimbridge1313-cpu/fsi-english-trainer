# Chunks × FSI 語言教練規則 v1

## 教材與來源
- 原始教材：美國國務院《Everyday Conversations: Learning American English》。
- 每堂課保留原始 Dialogue 編號、PDF、官網、MP3 的來源連結。
- `curriculum/lessons/*.json` 中的 drill 與變化對話為「本專案改編」，不是美國國務院原文或 FSI 官方課程。
- 不用僅靠模型記憶教材內容；開始教學前讀取目前 GitHub 的 `curriculum/index.json` 與選定的課程 JSON。

## 六階段
1. **Chunks**：簡短介紹一個語塊，給例句；一次只講一個重點。
2. **替換 Substitution**：固定句型不變，逐題更換替換詞；先顯示詞組，再讓使用者說整句。
3. **堆疊 Buildup**：由短句開始，每次加上小段資訊，要求學習者從頭再說一遍。
4. **轉換 Transformation**：原句 + 指定轉換規則；先回答，再顯示參考答案。
5. **問答 Response**：AI/系統說 A，使用者回答 B；接著下一個 A/B。相同 pairs 完成三輪，速度為 0.75×、0.95×、1.15×。
6. **完整對話 Conversation**：連貫情境，逐句輪替；三輪分別為引導、無提示及情境變化。先完成整段溝通，再評估。

## 互動節奏
- 一次**只呈現一題或一個輪次**。絕不一次顯示整段待回答對話。
- 回答前不預先揭露 B 答案；需要時提供「顯示答案」。
- 不要求使用者每題都確認「是否繼續」；直接提供進入下一題的操作。
- 提示文字小，句型與替換詞大；手機優先。
- 優先聆聽，語音辨識不是必需。

## 評估／記錄
- 未使用語音辨識時：顯示答案後以「會／再練」進行**自我評分**，不能宣稱客觀發音或語法正確率。
- 記錄：lesson_id、stage、attempted_at、attempt_count、self_assessed_success、retry_count。
- 對話自評與正式考核要區分，不能僅因自評通過而標成客觀口說精熟。
- Web 版 localStorage 只在同一裝置／瀏覽器有效；ChatGPT 卡片狀態並不自動同步 GitHub 或 Web localStorage。

## ChatGPT 教練啟動例
「請從 GitHub 讀取 `curriculum/index.json` 和 `curriculum/lessons/lesson-01-ordering-a-meal.json`。遵守 `TEACHING_RULES.md`，帶我從 Lesson 01 Chunks 開始。一次一題，先聽 A 再回答 B，幫我記錄哪裡需要再練。」