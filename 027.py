url = "http://sharebook.kr"
print(url[-2::])


# . 기준으로 split 후 뒤에 있는 리스트 요소 호출 가능

split_url= url.split(".")
print(split_url[-1])