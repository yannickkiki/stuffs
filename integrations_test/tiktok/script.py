from TikTokApi import TikTokApi
api = TikTokApi()

results = 10

trending = api.trending(count=results)

for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok['desc'])

print(len(trending))
