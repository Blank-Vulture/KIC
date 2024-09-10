# スライド17のfavorite_languages辞書
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# 投票に参加する予定の人のリスト（すでに辞書に載っている名前と載っていない名前を含む）
people_to_poll = ["jen", "mike", "sarah", "anna", "phil"]

# リストをループさせて、投票状況を確認
for person in people_to_poll:
    if person in favorite_languages:
        print(f"{person.title()}さん、回答してくれたことに感謝します。")
    else:
        print(f"{person.title()}さん、ぜひ投票してください！")
