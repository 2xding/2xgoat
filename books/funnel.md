# Faceless Book Account: Starter Kit

## 1. Account name (placeholder: `@1percentpages`)
Pick one, then check that it's free on TikTok, Instagram and as a domain:
- `@1percentpages`: "1% better" (Atomic Habits) + books
- `@quietcompound`: compounding, calm, a bit premium
- `@readrichbroke`: relatable for students
- `@pagesthatpay`: money-book angle
- `@thestackedshelf`: habit stacking + bookshelf

Bio: `books that actually change habits 📚 | free habit + reading tracker ↓`

---

## 2. Free Notion template: "The 1% Tracker"
Build it in Notion (~30 min), then **Share → Publish → allow "Duplicate as template"**.

**Pages:**
1. **Start Here:** a 3-line "how to use", plus a link back to your TikTok.
2. **Reading List:** database with Title, Author, Status (To read / Reading / Done), Rating, Key idea (1 line), Date finished. Pre-fill 12 books: Atomic Habits, The Psychology of Money, Deep Work, Eat That Frog, The 5 Second Rule, I Will Teach You to Be Rich, Rich Dad Poor Dad, The Millionaire Next Door, Can't Hurt Me, Mindset, The Almanack of Naval Ravikant, Show Your Work.
3. **Book Notes template:** "Big idea", "3 quotes", "1 thing I'll do this week", "Did I actually do it? ☐".
4. **Habit Tracker:** database with one row per day and checkbox columns (Read 10 pages, Deep work block, Move 20 min, No phone first hour, Journal), plus a formula column for daily %.
5. **Habit Stacking Builder:** a table with "After I… / I will… / Where / Start date".

No affiliate links inside the template. Keep those in emails and your link-in-bio.

---

## 3. Landing page (Kit)
**Headline:** The 1% Tracker: a free Notion system for reading more and building habits that stick

**Bullets:**
- 📚 Reading list pre-loaded with 12 life-changing books
- ✅ Daily habit tracker that shows your progress %
- 🧱 Habit-stacking builder from Atomic Habits

**Button:** Send me the tracker

**Consent line (required by CASL, Canada's anti-spam law; keep it under the button):**
> By signing up you'll get the tracker plus my weekly book & habit emails from [Your name / 1percentpages]. Unsubscribe anytime.

**Kit setup:** Landing page → Form → Automation: "Subscribes to form" → send Email 1 immediately → Emails 2–5 on the delays below.

---

## 4. Welcome sequence (5 emails)
Affiliate links go where it says `[link]`. Always add the line "(affiliate link: I earn a small commission at no cost to you)."

**Email 1: immediately**
Subject: your 1% Tracker is here
> Here's your tracker: [NOTION LINK]
> Click "Duplicate" (top right) to copy it into your own Notion.
> One tip: don't start with all 5 habits. Pick one. Tick it for 7 days. Then add another.
> Tomorrow I'll send the one idea that made habits finally stick for me.

**Email 2: day 2**
Subject: the sentence that makes habits stick
> "After I [current habit], I will [new habit]."
> That's habit stacking from *Atomic Habits* [link]. Your brain already runs your existing habits on autopilot, so attach the new one to it.
> Open the Habit Stacking Builder page and write one tonight.

**Email 3: day 4**
Subject: why most people who read self-help don't change
> They read 30 books and apply 0 ideas.
> Rule: one book → one action → one week. Use the "1 thing I'll do this week" box in Book Notes.
> Start with the book that fits your biggest problem:
> - Procrastinating → *Eat That Frog* [link]
> - Broke / bad with money → *The Psychology of Money* [link]
> - Can't focus → *Deep Work* [link]

**Email 4: day 6 (the offer)**
Subject: I turned 12 books into a 30-day plan
> The tracker helps you log. The **1% Workbook** tells you exactly what to do each day for 30 days: one idea from each of 12 books, turned into daily exercises, prompts and check-ins.
> It's $12 (launch price $9 until Sunday).
> [BUY LINK]
> If you're happy with the free tracker, that's cool too. The emails keep coming either way.

**Email 5: day 9**
Subject: quick check-in
> How many days have you ticked so far? Hit reply and tell me. I read every one.
> P.S. The 1% Workbook is still here if you want the full 30-day plan: [BUY LINK]

After email 5, send a weekly email: one book, one idea, one action, and an occasional link.

---

## 5. Money stages
| Stage | When | What |
|---|---|---|
| Affiliate | Day 1 | Amazon.ca Associates links in bio + emails |
| $9–12 workbook | ~200 subscribers | Pitched in Email 4, automatic for everyone |
| $29–49 "30-Day Reset" | ~1,000 subscribers | Launch 1× every 1–2 months |
| Sponsors / UGC | Now (UGC) · ~10k followers (sponsors) | Headway, Blinkist-type apps, habit/journal brands |

---

## 6. Posting routine
- 1–3 slideshows per day, rotating the 3 formats: **list**, **one-lesson**, **story / hot take**.
- To render: edit `books/posts.json`, run `python3 books/render.py`, and upload `books/out/<id>/*.png` in TikTok's **Photo** mode. Use the `caption` field from the JSON.
- Every 2 weeks, check which formats got the most **saves and shares** and make more of those.
- Before posting, check any stat or quote in your slides against the book.
