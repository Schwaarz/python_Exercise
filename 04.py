#encoding:utf-8
#2006年培养学员8万人，
# 每年增长25%，请问按此增长速度，
# 到哪一年培训学员人数将达到20万人？
year=2006
people=8
while 1==1:
    if people>=20:
        break
    else:
        people=people*1.25
        year=year+1

print("在%d年将达到20万以上"%year)
