meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "IDK" : "Bilmiyorum"
            "KYS" : "Kendini öldür"
            "Rizz" : "Bu kelimeyi sakın kullanmayın, olduğunu unutun hatta. İngilizce sözlüğüne giren en iğrenç şey bu. Ben her gördüğümde kendimi kusmaktan tutamiyorum. Bunu bir daha yazmayın."
            }
            

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
    
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Kelime yok..")
