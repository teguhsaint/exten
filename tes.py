from BingImageCreator import ImageGen

auth_cookie = "16uU6nOiYSCw58gLDaNGDCozUB8ywUP3TBicXHrV5YwCfXFwDC_KJQFHsV23uaodDKZ8d5T7zfO2QS-i4jWKQjnLSZA0YolgYHf8knXi8k2TZeyCBhsNRV3_cmUVgvoubpsH7Gqi3P_ftb2teQSrP4Xgj7e3cqTcqlxGePxxRnajUClPGV2gcrMfc5weUcF6XOUtgjSOSeOkFnhF-SkxJ5A"
img_gen = ImageGen(auth_cookie,auth_cookie)

prompt = input("Prompt : ")

image_links = img_gen.get_images(f"\"{prompt}\"")
output_dir = "kreasi"
img_gen.save_images(image_links, output_dir)